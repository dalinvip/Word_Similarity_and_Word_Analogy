# @Author : bamtercelboo
# @Datetime : 2018/4/24 15:10
# @File : find_wordSimilarity.py
# @Last Modify Time : 2018/4/24 15:10
# @Contact : bamtercelboo@{gmail.com, 163.com}


"""
    FILE :  find_wordSimilarity.py
    FUNCTION : None
"""

import os
import sys
import numpy as np
from math import sqrt
from optparse import OptionParser


class Similarity(object):
    def __init__(self, vector_file):
        self.vector_file = vector_file
        self.vector_dict = {}
        self.read_vector(self.vector_file)

    def read_vector(self, path):
        assert os.path.isfile(path), "{} is not a file.".format(path)
        embedding_dim = -1
        with open(path, encoding='utf-8') as f:
            for line in f:
                line_split = line.strip().split(' ')
                if len(line_split) == 1:
                    embedding_dim = line_split[0]
                    break
                elif len(line_split) == 2:
                    embedding_dim = line_split[1]
                    break
                else:
                    embedding_dim = len(line_split) - 1
                    break

        with open(path, encoding='utf-8') as f:
            lines = f.readlines()
            all_lines = len(lines)
            index = 0
            for index, line in enumerate(lines):
                values = line.strip().split(' ')
                if len(values) == 1 or len(values) == 2:
                    continue
                if len(values) != int(embedding_dim) + 1:
                    print("\nWarning {} -line.".format(index + 1))
                    continue
                # self.vector_dict[values[0]] = np.array([float(i) for i in values[1:]])
                self.vector_dict[values[0]] = np.array(list(map(float, values[1:])))
                # self.vector_dict[values[0]] = list(map(float, values[1:]))
                if index % 2000 == 0:
                    sys.stdout.write("\rreading with the {} lines, all {} lines.".format(index + 1, all_lines))
            sys.stdout.write("\rreading with the {} lines, all {} lines.".format(index + 1, all_lines))
        print("\nembedding words {}, embedding dim {}.".format(len(self.vector_dict), embedding_dim))

    def vector_len(self, v):
        return sqrt(sum([x * x for x in v]))

    def dot_product(self, v1, v2):
        assert len(v1) == len(v2)
        return sum([x * y for (x, y) in zip(v1, v2)])

    def cosine_similarity(self, v1, v2):
        """
        Returns the cosine of the angle between the two vectors.
        Results range from -1 (very different) to 1 (very similar).
        """
        return self.dot_product(v1, v2) / (self.vector_len(v1) * self.vector_len(v2))

    def sorted_by_similarity(self, words, base_vector):
        """Returns words sorted by cosine distance to a given vector, most similar first"""
        words_with_distance = [(self.cosine_similarity(base_vector, words[w]), w) for w in words]
        # We want cosine similarity to be as large as possible (close to 1)
        return sorted(words_with_distance, key=lambda t: t[0], reverse=True)

    def print_related(self, text):
        base_word = self.find_word(text, self.vector_dict)
        sorted_words = [word for (dist, word) in self.sorted_by_similarity(self.vector_dict, self.vector_dict[base_word]) if word.lower() != base_word.lower()]
        print(', '.join(sorted_words[:10]))

    def find_word(self, text, words):
        try:
            if text in words:
                return text
        except Exception as err:
            print("word {} not contains in embedding file, please try others.".format(text))


if __name__ == "__main__":
    print("Word Similarity Evaluation")

    # vector_file = "./Data/zhwiki_skipgram.100d.1w.source"

    parser = OptionParser()
    parser.add_option("--vector", dest="vector", help="vector file")
    (options, args) = parser.parse_args()
    vector_file = options.vector

    similarity = Similarity(vector_file=vector_file)
    while True:
        try:
            print("Enter word >> ", end="")
            target = input()
            if target == "exit":
                break
            similarity.print_related(target)
        except Exception as err:
            print("word [{}] not contains in embedding file, please try others.".format(target))
    print("Finished.")

