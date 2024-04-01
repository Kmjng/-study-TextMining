# -*- coding: utf-8 -*-
"""
step02_similarity_recomm.py

유사 문서 검색 

영화 검색(추천) 시스템 : 코사인 유사도 기반  
"""

import pandas as pd # csv file 
from sklearn.feature_extraction.text import TfidfVectorizer # 희소행렬 
from sklearn.metrics.pairwise import cosine_similarity # 유사도 계산 

# 1. dataset load 
path = r'C:/ITWILL/3_TextMining/TextMining/data'
data = pd.read_csv(path + '/movie_reviews.csv')
print(data.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1492 entries, 0 to 1491
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   reviews  1492 non-null   object : 영화후기 
 1   title    1492 non-null   object : 영화제목  
 2   label    1492 non-null   int64  : 긍정/부정 
'''
print(data.head())
'''
reviews  ... label
0  every now and then a movie comes along from a ...  ...     1
1  you've got mail works alot better than it dese...  ...     1
2  moviemaking is a lot like being the general ma...  ...     1
3  on june 30 , 1960 , a self-taught , idealistic...  ...     1
4  one of my colleagues was surprised when i told...  ...     1

[5 rows x 3 columns]

'''


# 2. 문서단어행렬(DTM) : reviews 대상 

# 1) 단어생성기 
obj = TfidfVectorizer(stop_words='english') 

# 2) 희소행렬 
movie_dtm = obj.fit_transform(data['reviews']) # 또는 data.reviews 

# 3) scipy -> numpy array 
movie_dtm_arr = movie_dtm.toarray()
movie_dtm_arr.shape # >>  (1492, 34641) # 단어 수 34641 

# 4) 영화제목 칼럼 추출
title = data.title


# 3. 검색어 -> 영화 검색(추천)  
def movie_search(query) :
    # 1) query 작성
    query_data = [query] # list 변경 
    #입력한 키워드가 들어가서
    
    # 2) query DTM 
    query_dtm = obj.transform(query_data)
    query_dtm_arr = query_dtm.toarray() 
    
    # 3) 유사도 계산 
    sim = cosine_similarity(query_dtm_arr, movie_dtm_arr) #중첩리스트로 저장됨 ★★
    sim = sim.reshape(1492) # 1492 개의 행(문서 수)으로 reshape ★★
    
    # 4) 내림차순 정렬 : index 정렬 
    sim_idx = sim.argsort()[::-1]
        
    global title # 전역변수 사용 
    
    # 5) Top5 영화추천하기 
    for idx in sim_idx[:5] :
        print(f'similarity : {sim[idx]} \n movie title : {title[idx]}\n')
        

# 함수 호출     
movie_search(input('search query input : '))


