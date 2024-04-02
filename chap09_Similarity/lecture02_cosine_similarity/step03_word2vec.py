# -*- coding: utf-8 -*-
"""
step03_word2vec.py

유사 단어 검색 

1. pip install gensim
2. word2vec 개요 
  - 중심단어와 주변단어 벡터 간의 연산으로 유사단어 예측
3. word2vec 유형 
  1) CBOW : 주변단어 학습 -> 중심단어 예측 
  2) SKIP-Gram : 중심단어 -> 주변단어 예측 ★
    Skip-gram의 학습량이 더 크기 때문에 임베딩 품질이 더 좋다
        ex) i love you -> (i,love), (i,you) : window =2 의 예시 (중심단어1, 주변단어1)
    
"""

from gensim.models import Word2Vec # model 
import nltk
nltk.download('punkt') # nltk data download
from nltk.tokenize import word_tokenize # 문장 -> 단어 token
from nltk.tokenize import sent_tokenize # 문단 -> 문장 token
import pandas as pd # csv file


'''
https://www.kaggle.com/rounakbanik/the-movies-dataset
movies_metadata.csv : 파일 다운로드해도 된다. 
'''

# 1. dataset load 
path = r'C:/ITWILL/3_TextMining/TextMining/data'
data = pd.read_csv(path + '/movies_metadata.csv')
print(data.info())


# 2. 변수 선택 & 전처리 
df = data[['title', 'overview']] # 두개의 칼럼만 쓴다. 

# 결측치 확인 
df.isnull() # 일일히 확인 어렵 ; 
df.isnull().sum() # isnull이 True인 경우 sum 해서 보여준다.
'''
title         6
overview    954
dtype: int64
'''
# 결측치 제거 ★
df = df.dropna(axis = 0)


# 3. token 생성 
# 1) overview 단어 벡터 생성 
overview = df['overview'].tolist() 
# tolist() # column -> list변환 

type(overview) # >> class 'list'

overview[0] # 첫번째 문장 원문

# 2) 문장 -> 단어 
# word_tokenize() 메소드
# string을 단어 쪼개서 리스트에 넣음
result = [word_tokenize(row) for row in overview ]  # 중첩리스트일것

result[0] # 첫번째 문장의 단어 벡터
'''
['Led',
 'by',
 'Woody',
 ',',
 'Andy',
 "'s",
 'toys',
 'live',
 'happily',
 'in',
 'his',
 'room',
 'until',
 'Andy',
 "'s",
 'birthday',
 'brings',
 'Buzz',
 'Lightyear',
 'onto',
 'the',
 'scene',
 '.',
 'Afraid',
 'of',
 'losing',
 'his',
 'place',
 'in',
 'Andy',
 "'s",
 'heart',
 ',',
 'Woody',
 'plots',
 'against',
 'Buzz',
 '.',
 'But',
 'when',
 'circumstances',
 'separate',
 'Buzz',
 'and',
 'Woody',
 'from',
 'their',
 'owner',
 ',',
 'the',
 'duo',
 'eventually',
 'learns',
 'to',
 'put',
 'aside',
 'their',
 'differences',
 '.']
'''
# 4. word2vec # gensim 라이브러리 
model = Word2Vec(sentences=result, window=5, min_count=1, sg=1) 
# 참고로 result 리스트는 원소 하나에 문장이 쪼개진 단어들이 들어가 있음
'''
파라미터 설명 
sentences : 학습을 위한 단어 벡터 
window : 1회 학습할 단어 수, window = 5이면 주변단어4개 
min_count : 최소 단어 빈도수 제한 
sg : 사용하고자 할 알고리즘 (0: CBOW, 1: SKIP-Gram)
'''
dir(model)
'''
 'window',
 'workers',
 'wv']  
wv 메소드는 Word2Vec 모델에서 단어 벡터를 관리하는 기능을 제공
'''
help(model.wv) 

word_search2 = model.wv['husband']
print(word_search2) # 단어벡터가 출력됨 (고차원 벡터) 
'''
 "husband"이라는 단어의 벡터는 해당 단어의 의미를 수치적으로 표현하며, 
 이러한 표현은 주변 단어와의 관계를 고려하여 형성
'''

# 5. 유사 단어 검색  
word_search = model.wv.most_similar(['husband']) # (유사단어, 유사도)
print('Top5 word: ', word_search[:5]) 
'''
Top5 word:  
    [('boyfriend', 0.843079149723053), 
     ('lover', 0.823157787322998), ('fiancé', 0.8062788844108582), 
     ('fiance', 0.7966833710670471), ('mother', 0.7867057919502258)]'''


# 함수로 만들기 

def ws(keyword): 
    ws = model.wv.most_similar([keyword])
    return ws[:5]


print('Top5 word: ',ws(input('keyword input: ')))
