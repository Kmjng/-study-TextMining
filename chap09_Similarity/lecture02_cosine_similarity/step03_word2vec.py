# -*- coding: utf-8 -*-
"""
step03_word2vec.py

유사 단어 검색 

1. pip install gensim
2. word2vec 개요 
  - 중심단어와 주변단어 벡터 간의 연산으로 유사단어 예측
3. word2vec 유형 
  1) CBOW : 주변단어 학습 -> 중심단어 예측 
  2) SKIP-Gram : 중심단어 -> 주변단어 예측 
"""

from gensim.models import Word2Vec # model 
import nltk
nltk.download('punkt') # nltk data download
from nltk.tokenize import word_tokenize # 문장 -> 단어 token
from nltk.tokenize import sent_tokenize # 문단 -> 문장 token
import pandas as pd # csv file


'''
https://www.kaggle.com/rounakbanik/the-movies-dataset
movies_metadata.csv : 파일 다운로드 
'''

# 1. dataset load 
path = r'C:\ITWILL\3_TextMining\data'
data = pd.read_csv(path + '/movies_metadata.csv')
print(data.info())


# 2. 변수 선택 & 전처리 
df = data[['title', 'overview']]
df = df.dropna(axis = 0) # 결측치 제거 


# 3. token 생성 
# 1) overview 단어 벡터 생성 
overview = df['overview'].tolist() # column -> list변환 

# 2) 문장 -> 단어
result = [word_tokenize(row) for row in overview ] 


# 4. word2vec 
model = Word2Vec(sentences=result, window=5, min_count=1, sg=1) 


# 5. 유사 단어 검색 
word_search = model.wv.most_similar(['husband']) 
