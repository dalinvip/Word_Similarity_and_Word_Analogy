
##  English word embedding evaluation  ##

paper([Community Evaluation and Exchange of Word Vectors at wordvectors.org](http://www.aclweb.org/anthology/P14-5004)) , set up a system ([http://www.wordvectors.org/](http://www.wordvectors.org/)) for word vector evaluation, this code is the[ background code](https://github.com/mfaruqui/eval-word-vectors) changes are integrated, and the code contains thirteen  similarity file.

## Requirements ##

>python 3.6 (+numpy package)


## Usage ##

#### First steps: filter vocab ####

	python -u filiter_vocab.py --vector  vector_file --output filtered_vector_file
	like:
	python -u filiter_vocab.py --vector vector_file  --output ./embed/filtered.txt

default vocab file  from the [http://www.wordvectors.org/fullVocab.txt](http://www.wordvectors.org/fullVocab.txt), now save in the path of `./data/filter/fullVocab.txt`.

#### Evaluating on multiple word sim tasks ####

	python all_wordsim.py --vector vector_file --similarity ./data/en
	like: 
	python all_wordsim.py --vector ./embed/filtered.txt --similarity ./data/en

The default value for the similarity option is `./data/en`, so can evaluate english word embedding follows:

	python all_wordsim.py --vector vector_file
	like: 
	python all_wordsim.py --vector ./embed/filtered.txt

#### Evaluating on one word sim task ####

	python wordsim.py --vector vector_file --similarity ./data/en/EN-MTurk-771.txt
	like: 
	python wordsim.py --vector ./embed/filtered.txt --similarity ./data/en/EN-MTurk-771.txt


## Outputs ##

![](https://i.imgur.com/UKm4oTP.jpg)


## Question ##

    if you have any question, you can open a issue or email bamtercelboo@{gmail.com, 163.com}.

    if you have any good suggestions, you can PR or email me.
