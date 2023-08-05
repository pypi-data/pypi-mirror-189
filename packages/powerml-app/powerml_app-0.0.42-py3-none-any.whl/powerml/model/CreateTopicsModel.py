from math import ceil
from powerml import PowerML
from powerml.utils.constants import MAX_TEMPLATE_TOKENS
import re
from collections import Counter, defaultdict
import random
from tqdm import tqdm
import sys
import os
import nltk
from nltk.stem import WordNetLemmatizer

class CreateTopicsModel:
    '''
    This model removes duplicates and attempts to generate topics relevant
    to topic_type.
    '''

    def __init__(
            self,
            config={},
            max_output_tokens=256,
            random_seed=None):
        

        if random_seed is not None:
            random.seed(random_seed)
        self.model = PowerML(config, "unblocked/create-topics/v2")
        self.messages = []
        self.num_subsamples = 10
        self.sample_size = 20
        self.max_output_tokens = max_output_tokens
        self.memo_topics = {}

    def fit(self, documents, topic_type):
        """
        Parameters
        ----------
        documents : Dict{"<ID>": "<doc>"}
            A list of text documents which discuss various topics
        topic_type : str
            A description of the topics to be extracted from the documents
        """
        self.topic_type = topic_type
        self.message_ids = [key for key in documents]
        self.messages = documents
        self.num_samples = len(self.messages)
        self.num_subsamples = ceil(self.num_samples / self.sample_size)

    def predict(self):
        """
        Returns
        -------
        list[{
            "name": str,
            "score": float,
        }] : a list of dictionaries with generated topic names and scores
        """
        # If get_topics has been called on the same messages array
        # Then use the previous results
        hash_docs = hash(frozenset(self.messages))
        if hash_docs in self.memo_topics:
            return self.memo_topics[hash_docs]

        sample_index = 0
        topic_counter = Counter()
        print("Learning topics...")
        queue = random.sample(range(self.num_samples), self.num_samples)
        topic_to_docs = defaultdict(set)
        for _ in tqdm(range(self.num_subsamples), ncols=0):
            if sample_index > self.num_samples:
                break
            prompt = self.__prompt_format(self.topic_type)
            start_index = sample_index
            examples, sample_index = self.__subsample(
                queue, sample_index, self.sample_size)
            end_index = sample_index
            prompt = self.__add_examples(examples, prompt)
            output = self.model.predict(
                prompt, max_tokens=self.max_output_tokens, temperature=0.7)
            topics = self.__parse_output(output)
            for topic in topics:
                topic_to_docs[topic].update([self.message_ids[index] for index in queue[start_index:end_index]]) 
            topic_counter.update(topics)
            sorted_topics = self.__sort_topics(topic_counter)
        topics = self.__get_topics(sorted_topics, topic_to_docs)
        topics = self.__deduplicate_topics(topics)
        self.memo_topics[hash_docs] = topics
        return topics

    def __count_tokens(self, string):
        return len(string) // 4

    def __prompt_format(self, topic_type):
        prompt_dict = {"{{topic_type}}": topic_type}
        for i in range(self.sample_size):
            key = "{{example" + str(i + 1) + "}}"
            prompt_dict[key] = ""
        return prompt_dict

    def __add_examples(self, examples, prompt, max_total_tokens=MAX_TEMPLATE_TOKENS):
        prompt_dict = prompt
        for i, example in enumerate(examples):
            key = "{{example" + str(i + 1) + "}}"
            prompt_dict[key] = example
            if self.__count_tokens(str(prompt_dict)) > max_total_tokens - self.max_output_tokens:
                prompt_dict[key] = ""
                break
        return prompt_dict

    def __parse_output(self, output):
        list_pattern = re.compile(r"\d+\.\s")
        # include enumerated list prompt
        items = list_pattern.sub("", f'1. {output}')
        parsed = []
        for i in items.split('\n'):
            ii = i.split(',')
            stripped = [iii.strip().replace('.', '') for iii in ii if iii]
            parsed.extend(stripped)
        return parsed
    
    def __subsample(self, shuffled_indices, start_index, sample_size):
        examples = []
        token_count = 0
        end_index = min(start_index + sample_size, self.num_samples)
        for index in range(start_index, end_index):
            shuffled_index = shuffled_indices[index]
            token_count += self.__count_tokens(self.messages[self.message_ids[shuffled_index]])
            if token_count > MAX_TEMPLATE_TOKENS:
                return examples, index
            examples.append(self.messages[self.message_ids[shuffled_index]])
        return examples, index

    def __sort_topics(self, topic_counter):
        return sorted(topic_counter.items(), key=lambda x: x[1], reverse=True)

    def __get_topics(self, sorted_topics, topic_to_docs):
        # Return and save all topics
        return [{"name": elt, "score": count / self.num_subsamples, "documents": sorted(topic_to_docs[elt])} for elt, count in sorted_topics]
    
    def __deduplicate_topics(self, topics_with_scores):
        # This is a hack to silence printed message on import
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        nltk.download('wordnet')
        lemmatizer = WordNetLemmatizer()
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        related_topics = defaultdict(list)
        for topic in topics_with_scores:
            related_topics[lemmatizer.lemmatize(topic['name'].lower())].append(topic)
        filtered_topics_with_scores = []
        for topic_name in related_topics:
            keywords = list({related_topic['name'] for related_topic in related_topics[topic_name]})
            score = sum([related_topic['score'] for related_topic in related_topics[topic_name]])
            documents = sorted({document for related_topic in related_topics[topic_name] for document in related_topic['documents']})
            filtered_topics_with_scores.append({'name': topic_name, 'score': score, 'keywords': keywords, 'documents': documents})
        filtered_topics_with_scores = sorted(filtered_topics_with_scores, key=lambda x: x['score'], reverse=True)
        return filtered_topics_with_scores

    @staticmethod
    def deduplicate_topics_with_keywords(topics_with_scores):
        # This is a hack to silence printed message on import
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        nltk.download('wordnet')
        lemmatizer = WordNetLemmatizer()
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        related_topics = defaultdict(list)
        for topic in topics_with_scores:
            related_topics[lemmatizer.lemmatize(topic['name'].lower())].append(topic)
        filtered_topics_with_scores = []
        for topic_name in related_topics:
            keywords = list({keyword for related_topic in related_topics[topic_name] for keyword in related_topic['keywords']})
            score = sum([related_topic['score'] for related_topic in related_topics[topic_name]])
            documents = sorted({document for related_topic in related_topics[topic_name] for document in related_topic['documents']})
            filtered_topics_with_scores.append({'name': topic_name, 'score': score, 'keywords': keywords, 'documents': documents})
        filtered_topics_with_scores = sorted(filtered_topics_with_scores, key=lambda x: x['score'], reverse=True)
        return filtered_topics_with_scores
