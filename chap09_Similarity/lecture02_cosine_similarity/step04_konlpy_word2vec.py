# -*- coding: utf-8 -*-
"""
한글 문서 유사 단어 검색 (생략)
"""
import pandas as pd # csv file read
from gensim.models import Word2Vec # model 
import nltk # Natural Language Toolkit
nltk.download('punkt') # nltk data download
from nltk.tokenize import word_tokenize # sentence -> work token

'''
daum_news.csv : 2023.3.8. daum news 기사
'''
# 1. csv file 읽기
path = r'C:\ITWILL\3_TextMining\data'
daum_news = pd.read_csv(path + '/daum_news.csv')

type(daum_news) # pandas.core.frame.DataFrame(2차원:행,열)

# 2. 칼럼 선택
daum_news.info()
'''
Data columns (total 2 columns):
 #   Column    Non-Null Count  Dtype 
 0   title   20 non-null     object
 1   news    20 non-null     object -> 칼럼 선택 
'''

# 3. token 생성 

# 1) overview 단어 벡터 생성 
overview = daum_news['news'].tolist() # column -> list변환 
 

# 2) 문단(result) : 44,506 문장 -> 문장(result[idx]) > N 단어
result = [word_tokenize(row) for row in overview ] 
# [[단어벡터], ... [단어벡터]]


# 4. word2vec 
model = Word2Vec(sentences=result, window=5, 
                 min_count=1, sg=1) 
'''
sentences : 단어벡터 
window : 1회 학습할 단어수 
min_count : 단어 최소 빈도수 제한(빈도수 작은 단어 학습에서 제외) 
sg : 0-CBOW, 1-SKIP-Gram 
'''

# 5. 유사 단어 검색 
word_search = model.wv.most_similar(['김종민']) 
print('top5 :',  word_search[:5])

'''
top5 : [('김현정', 0.9880617260932922), ('.', 0.9873330593109131), ('한', 0.9873150587081909), ('>', 0.987032949924469), (',', 0.9861798882484436)]
'''



