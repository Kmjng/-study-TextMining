# -*- coding: utf-8 -*-
"""
유사 문서 찾기  

<작업절차>
 1. 자연어 -> 문서단어행렬(DTM) 변경 -> 단어집 생성
 2. 코사인 유사도 적용     
"""

# 문서단어행렬(DTM)
from sklearn.feature_extraction.text import TfidfVectorizer # 단어생성기 
# 코사인 유사도 
from sklearn.metrics.pairwise import cosine_similarity 


# 문장(자연어)
sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
] #  밑의 비교문서(query)는 2번 문서와의 유사도가 높아 보인다. 

print(sentences)
len(sentences) # 3


# 1. 대상 문서(자연어) -> DTM(문서단어행렬:희소행렬) 변경
# 1) 단어생성기 
obj = TfidfVectorizer() 
type(obj) # >> sklearn.feature_extraction.text.TfidfVectorizer
# 2) 생성된 단어 확인 
fit = obj.fit(sentences) # 원문을 fit객체로 반영
type(fit) # >> sklearn.feature_extraction.text.TfidfVectorizer

voca = fit.vocabulary_ # 단어집 
print(voca)
'''
{'mr': 14, 'green': 5, 'killed': 11, 'colonel': 2, 'mustard': 15, 
 'in': 9, 'the': 24, 'study': 23, 'with': 30, 'candlestick': 1, 
 'is': 10, 'not': 17, 'very': 25, 'nice': 16, 'fellow': 3, 'professor': 21, 
 'plum': 20, 'has': 6, 'plant': 19, 'his': 8, 'miss': 13, 'scarlett': 22, 
 'watered': 27, 'while': 29, 'he': 7, 'was': 26, 'away': 0, 'from': 4, 
 'office': 18, 'last': 12, 'week': 28}
'''
help(fit.vocabulary_) # class dict(object)
help(fit.vocabulary) # class NoneType(object)

# 3) 문서단어행렬(DTM)
sents_dtm = obj.fit_transform(sentences) # 원문을 fit_transform객체로 반영
type(sents_dtm) # >> scipy.sparse._csr.csr_matrix

# 4) scipy -> numpy array
sents_dtm_arr = sents_dtm.toarray()
print(sents_dtm_arr)
'''
[[0.         0.22058288 0.22058288 0.22058288 0.         0.26055961
  0.         0.         0.         0.16775897 0.22058288 0.22058288
  0.         0.         0.44116577 0.22058288 0.22058288 0.22058288
  0.         0.         0.         0.         0.         0.16775897
  0.44116577 0.22058288 0.         0.         0.         0.
  0.22058288]
 [0.         0.         0.         0.         0.         0.26903992
  0.45552418 0.         0.34643788 0.34643788 0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.34643788 0.34643788 0.34643788 0.         0.34643788
  0.         0.         0.         0.         0.         0.
  0.        ]
 [0.27054288 0.         0.         0.         0.27054288 0.15978698
  0.         0.27054288 0.20575483 0.         0.         0.
  0.27054288 0.27054288 0.         0.         0.         0.
  0.27054288 0.20575483 0.20575483 0.20575483 0.27054288 0.
  0.         0.         0.27054288 0.27054288 0.27054288 0.27054288
  0.        ]]
'''
sents_dtm_arr.shape # >> (3, 31)


# 2. 코사인 유사도 적용 

# 1) 검색 쿼리(search query)
query = ['green plant in his study'] # 검색 문장 

# 2) 희소행렬(DTM)
query_dtm = obj.transform(query) 
# 함수 주의 : fit_transform이 아님 ★★★
# (1,5) 행렬이 아닌, 기준문서인 obj객체의 (3, 31)행렬에 맞춰 확인하기 위해 transform()메소드를 사용

type(query_dtm) # >> scipy.sparse._csr.csr_matrix

# 3) scipy -> numpy array
query_dtm_arr = query_dtm.toarray()
query_dtm_arr
'''
array([[0.        , 0.        , 0.        , 0.        , 0.        ,
        0.361965  , 0.        , 0.        , 0.46609584, 0.46609584,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.46609584,
        0.        , 0.        , 0.        , 0.46609584, 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        ]])
'''
query_dtm_arr.shape # > (1, 31)

# 4) 코사인 유사도 계산 
sim = cosine_similarity(query_dtm_arr, sents_dtm_arr)
print(sim) # >> [[0.25069697 0.74327606 0.24964024]]
# 해석: 비교문서 query가 기준문서의 2번째 문장과 유사도가 0.74로 가장 높다. 

# 5) 모양 변경 
sim = sim.reshape(3)
print(sim) # >> [0.25069697 0.74327606 0.24964024]


# 6) 내림차순 정렬 : 유사도 높은 순(내림차순)으로 index 정렬
# 인덱스를 반환 ★★★ 
sim_idx = sim.argsort()[::-1] 
print(sim_idx) # >> [1 0 2] 

for idx in sim_idx:
    print(f"유사도: {round(sim[idx],3)}\nsentence: {sentences[idx]}\n") # 기준문서[idx]

'''
유사도: 0.743
sentence: Professor Plum has a green plant in his study.

유사도: 0.251
sentence: Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.

유사도: 0.25
sentence: Miss Scarlett watered Professor Plum's green plant while he was away from his office last week.
'''

############################
# 두 벡터 간 코사인 유사도 식 
# linagl.norm()
# 벡터객체.T # 전치행렬
# np.dot()
############################
import numpy as np 
# 1. ||A|| 벡터 크기 (norm) 
A =np.array([[1,3,5,6,7]]) # A 벡터
#  numpy에서는 1차원 배열을 다룰 때 일관성을 유지하기 위해 '중첩 리스트'를 사용하는 것이 좋다
A_norm= np.linalg.norm(A) #선형대수 메소드
# >> 10.954451150103322

# 2. ||B|| 벡터 크기 (norm)
B = np.array([[5,3,5,2,5]]) # B벡터
B_norm= np.linalg.norm(B) # >> 9.38083151964686

# 3. A와 B의 행렬곱 (행렬하나를 전치행렬화한다.)
A.shape # (1,5)
B.shape # (1,5)
np.dot(A, B.T) # >> array([[86]])
sim = np.dot(A,B.T) / (A_norm*B_norm)
print(sim) # >> [[0.83688636]]
