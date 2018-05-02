# @Author : bamtercelboo
# @Datetime : 2018/4/23 19:00
# @File : word_similarity.py
# @Last Modify Time : 2018/4/23 19:00
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  word_similarity.py
    FUNCTION : None
"""

import os
import sys
import logging
import numpy as np
from optparse import OptionParser
from scipy import linalg, stats


class Similarity(object):
    def __init__(self, vector_file, similarity_file):
        self.vector_file = vector_file
        self.similarity_file = similarity_file
        self.vector_dict = {}
        self.result = {}
        self.read_vector(self.vector_file)
        if self.similarity_file is "":
            self.Word_Similarity(similarity_name="./Data/wordsim-240.txt", vec=self.vector_dict)
            self.Word_Similarity(similarity_name="./Data/wordsim-297.txt", vec=self.vector_dict)
        else:
            self.Word_Similarity(similarity_name=self.similarity_file, vec=self.vector_dict)
        self.pprint(self.result)

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
                    # print("Warning {} -line.".format(index + 1))
                    logging.info("Warning {} -line.".format(index + 1))
                    continue
                self.vector_dict[values[0]] = np.array(list(map(float, values[1:])))
                if index % 2000 == 0:
                    sys.stdout.write("\rHandling with the {} lines, all {} lines.".format(index + 1, all_lines))
            sys.stdout.write("\rHandling with the {} lines, all {} lines.".format(index + 1, all_lines))
        print("\nembedding words {}, embedding dim {}.".format(len(self.vector_dict), embedding_dim))

    def pprint(self, result):
        from prettytable import PrettyTable
        x = PrettyTable(["Dataset", "Found", "Not Found", "Score (rho)"])
        x.align["Dataset"] = "l"
        for k, v in result.items():
            x.add_row([k, v[0], v[1], v[2]])
        print(x)

    def cos(self, vec1, vec2):
        return vec1.dot(vec2)/(linalg.norm(vec1)*linalg.norm(vec2))

    def rho(self, vec1, vec2):
        return stats.stats.spearmanr(vec1, vec2)[0]

    def Word_Similarity(self, similarity_name, vec):
        pred, label, found, notfound = [], [], 0, 0
        with open(similarity_name, encoding='utf8') as fr:
            for i, line in enumerate(fr):
                w1, w2, score = line.split()
                if w1 in vec and w2 in vec:
                    found += 1
                    pred.append(self.cos(vec[w1], vec[w2]))
                    label.append(float(score))
                else:
                    notfound += 1
        file_name = similarity_name[similarity_name.rfind("/") + 1:].replace(".txt", "")
        self.result[file_name] = (found, notfound, self.rho(label, pred))


if __name__ == "__main__":
    print("Word Similarity Evaluation")

    # vector_file = "./Data/zhwiki_substoke.100d.source"
    # vector_file = "./Data/zhwiki_cbow.100d.source"
    # similarity_file = "./Data/wordsim-297.txt"
    # Similarity(vector_file=vector_file, similarity_file=similarity_file)
    # Similarity(vector_file=vector_file, similarity_file="")

    parser = OptionParser()
    parser.add_option("--vector", dest="vector", help="vector file")
    parser.add_option("--similarity", dest="similarity", default="", help="similarity file")
    (options, args) = parser.parse_args()

    vector_file = options.vector
    similarity_file = options.similarity

    try:
        Similarity(vector_file=vector_file, similarity_file=similarity_file)
        print("All Finished.")
    except Exception as err:
        print(err)


