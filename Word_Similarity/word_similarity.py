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
import numpy as np
from scipy.spatial.distance import cosine
from scipy.stats import spearmanr
from optparse import OptionParser


class Similarity(object):
    def __init__(self, vector_file, similarity_file):
        self.vector_file = vector_file
        self.similarity_file = similarity_file
        self.vector_dict = {}
        self.read_vector(self.vector_file)
        if self.similarity_file is "":
            self.Word_Similarity(similarity_name="./Data/wordsim-240.txt", vec=self.vector_dict)
            self.Word_Similarity(similarity_name="./Data/wordsim-297.txt", vec=self.vector_dict)
        else:
            self.Word_Similarity(similarity_name=self.similarity_file, vec=self.vector_dict)

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
                    print("Warning {} -line.".format(index + 1))
                    continue
                self.vector_dict[values[0]] = np.array(list(map(float, values[1:])))
                if index % 2000 == 0:
                    sys.stdout.write("\rHandling with the {} lines, all {} lines.".format(index + 1, all_lines))
            sys.stdout.write("\rHandling with the {} lines, all {} lines.".format(index + 1, all_lines))
        print("\nembedding words {}, embedding dim {}.".format(len(self.vector_dict), embedding_dim))

    def Word_Similarity(self, similarity_name, vec):
        rank = []
        num = 0
        with open(similarity_name, encoding='utf8') as fr:
            for i, line in enumerate(fr):
                w1, w2, _ = line.split()
                try:
                    sim = cosine(vec[w1], vec[w2])
                    rank.append((i, sim))
                except Exception:
                    print('something is wrong with the {}-th line'.format(i + 1))
                num += 1

        rank_sorted = sorted(rank, key=lambda x: x[1])
        rank_pos = [x[0] for x in rank_sorted]
        try:
            corr, _ = spearmanr(rank_pos, range(num))
        except Exception:
            corr, _ = spearmanr(rank_pos, sorted(rank_pos))
        finally:
            print('The correlation is {} for task {}'.format(
                corr, similarity_name)
            )


if __name__ == "__main__":
    print("Word Similarity Evaluation")

    # vector_file = "./Data/zhwiki_substoke.100d.source"
    # similarity_file = "./Data/wordsim-240.txt"
    # Similarity(vector_file=vector_file, similarity_file=similarity_file)

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


