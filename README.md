
##  Word Similarity  and Word Analogy ##

- Based on the `wordsim-240` and `wordsim-296`, chinese word similarity script.

- Based on the `analogy.txt`, chinese word analogy script.

- English word embedding evaluation([en_embedding_similarity](https://github.com/bamtercelboo/Word_Similarity_and_Word_Analogy/tree/master/en_embedding_similarity))

## Requirement ##

- python: `3.6.1`

## English word embedding evaluation Usage ##

- About how to evaluate the english word embedding, see  [en-embedding-similarity-README](https://github.com/bamtercelboo/Word_Similarity_and_Word_Analogy/tree/master/en_embedding_similarity) for details.

## Word Similarity Usage ##

	Word Similarity Accuracy:
	    if you want to evaluate your similarity file:
	        python word_similarity.py --vector embed_path  --similarity similar_file  

	    if you want to evaluate on default file (wordsim-240 and wordsim-296)
	        python word_similarity.py --vector embed_path

	Find Top 10 similar words:
	    python find_wordSimilarity.py --vector embed_path


## Word Analogy Usage ##

	Word Analogy Accuracy:
	    if you want to evaluate your analogy file:
	        python word_analogy.py --vector  embed_path --analogy analogy_file

	    if you want to evaluate on default file (analogy.txt that from chen)
	        python word_analogy.py --vector embed_path

	Find the closest analogy:
	    python find_wordAnalogy.py --vector embed_path

## Word Similarity  Output ##

1、Rho Score  

![](https://i.imgur.com/8w20K4H.jpg)

2、 Top 10 similar words  
 
	Enter word >> 男人
	女人, 中年男人, 女孩, 敢爱敢恨, 爱管闲事, 失婚, 男士们, 少妇, 女们, 憨直
	Enter word >> 中国
	大陆, 内地, 我国, 华中地区, 中国民间文艺家协会, 江浙沪, 华南地区, 中国政府, 中医药学会, 中华人民共和国
	
- output top ten, the most similar In the front
	
## Word Analogy  Output ##

1、Word Analogy Accuracy:
	
	Category: city
	Total count: 175
	Accuracy: 0.8
	Mean rank: 4.942857142857143

	Category: family
	Total count: 272
	Accuracy: 0.5661764705882353
	Mean rank: 21.47426470588235

	Category: capital
	Total count: 677
	Accuracy: 0.7562776957163959
	Mean rank: 2.224519940915805

	Total acc: 0.7170818505338078
	Total mean rank: 7.306049822064057
	Total number: 1124  


2、Find the closest analogy  

	Enter three word >> 男人 女人 男孩
	[男人 - 女人] is like [男孩 - 女孩]
	Enter three word >> 北京 上海 纽约
	[北京 - 上海] is like [纽约 - 布鲁克林]


## Question ##

- if you have any question, you can open a issue or email bamtercelboo@{gmail.com, 163.com}.

- if you have any good suggestions, you can PR or email me.
