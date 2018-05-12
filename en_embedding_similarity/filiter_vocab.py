# @Author : bamtercelboo
# @Datetime : 2018/3/24 16:43
# @File : filiter_vocab.py
# @Last Modify Time : 2018/3/24 16:43
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  filiter_vocab.py
    FUNCTION : None
    REFERENCE: http://www.wordvectors.org/filterVocab.py
"""

import sys
import os
from optparse import OptionParser


def filter_vocab(in_path, vocab_path, out_path):
    d = {}
    for line in open(vocab_path, 'r'):
        d[line.strip()] = 0

    if os.path.exists(out_path):
        os.remove(out_path)

    file = open(out_path, "w")
    for line in open(in_path):
        if line.strip().split()[0] in d:
            file.write(line)
            print(line.strip())
    file.close()


if __name__ == "__main__":
    print("English word embedding evaluation filter vocab")

    parser = OptionParser()
    parser.add_option("--vector", dest="vector", help="input vector file")
    parser.add_option("--output", dest="output", help="output vector file")
    (options, args) = parser.parse_args()

    input = options.vector
    output = options.output

    try:
        filter_vocab(in_path=input, vocab_path="./data/filter/fullVocab.txt", out_path=output)
        print("All Finished.")
    except Exception as err:
        print(err)




