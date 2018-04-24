# @Author : bamtercelboo
# @Datetime : 2018/4/24 15:10
# @File : find_wordAnalogy.py
# @Last Modify Time : 2018/4/24 15:10
# @Contact : bamtercelboo@{gmail.com, 163.com}


"""
    FILE :  find_wordAnalogy.py
    FUNCTION : None
"""

import os
import sys
import numpy as np
from math import sqrt
from optparse import OptionParser


class Analogy(object):
    def __init__(self, vector_file):
        self.vector_file = vector_file
        self.vector_dict = {}
        self.read_vector(self.vector_file)

    def read_vector(self, path):
        assert os.path.isfile(path), "embedding path is not a file."
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
                if index % 2000 == 0:
                    sys.stdout.write("\rHandling with the {} lines, all {} lines.".format(index + 1, all_lines))
            sys.stdout.write("\rHandling with the {} lines, all {} lines.".format(index + 1, all_lines))
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

    def find_word(self, text, words):
        try:
            if text in words:
                return text
            else:
                print("word [{}] not contains in embedding file, please try others.".format(text))
        except Exception as err:
            print("word {} not contains in embedding file, please try others.".format(text))

    def closest_analogies(self, left2, left1, right2, words):
        word_left1 = self.find_word(left1, words)
        word_left2 = self.find_word(left2, words)
        word_right2 = self.find_word(right2, words)
        left1_vec, left2_vec, right2_vec = self.vector_dict[word_left1], self.vector_dict[word_left2], self.vector_dict[word_right2]
        vector = np.add(np.subtract(left1_vec, left2_vec), right2_vec)
        closest = self.sorted_by_similarity(words, vector)[:10]
        return [(dist, w) for (dist, w) in closest if not self.is_redundant(word_left2, word_left1, word_right2, w)]

    def is_redundant(self, left2, left1, right2, word):
        """
        Sometimes the two left vectors are so close the answer is e.g.
        "shirt-clothing is like phone-phones". Skip 'phones' and get the next
        suggestion, which might be more interesting.
        """
        return (
                left1.lower() in word.lower() or
                left2.lower() in word.lower() or
                right2.lower() in word.lower())

    def print_analogy(self, left2, left1, right2):
        analogies = self.closest_analogies(left2, left1, right2, self.vector_dict)
        if len(analogies) == 0:
            print(f"[{left2} - {left1}] is like [{right2} - ?]")
        else:
            (dist, w) = analogies[0]
            print(f"[{left2} - {left1}] is like [{right2} - {w}]")


if __name__ == "__main__":

    # vector_file = "./Data/zhwiki_skipgram.100d.1w.source"

    parser = OptionParser()
    parser.add_option("--vector", dest="vector", help="vector file")
    (options, args) = parser.parse_args()
    vector_file = options.vector

    analogy = Analogy(vector_file=vector_file)
    while True:
        try:
            print("Enter three word >> ", end="")
            target = input()
            target = target.split()
            if len(target) == 1 and target[0] == "exit":
                break
            if len(target) != 3:
                print("please enter three words.")
                continue
            analogy.print_analogy(target[0], target[1], target[2])
        except Exception as err:
            print("please try again.")
    print("Finished.")
