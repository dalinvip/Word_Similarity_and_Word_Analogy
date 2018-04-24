
##  Word Similarity  and Word Analogy ##

- Based on the `wordsim-240` and `wordsim-296`, chinese word similarity script.

- Based on the `analogy.txt`, chinese word analogy script.

## Requirement ##

- python: `3.6.1`

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

	Enter word >> 男人
	女人, 中年男人, 女孩, 敢爱敢恨, 爱管闲事, 失婚, 男士们, 少妇, 女们, 憨直
	Enter word >> 中国
	大陆, 内地, 我国, 华中地区, 中国民间文艺家协会, 江浙沪, 华南地区, 中国政府, 中医药学会, 中华人民共和国
	
- output top ten, the most similar In the front
	
## Word Analogy  Output ##

	Enter three word >> 男人 女人 男孩
	[男人 - 女人] is like [男孩 - 女孩]
	Enter three word >> 北京 上海 纽约
	[北京 - 上海] is like [纽约 - 布鲁克林]

- output top one


## Question ##

    if you have any question, you can open a issue or email bamtercelboo@{gmail.com, 163.com}.

    if you have any good suggestions, you can PR or email me.
