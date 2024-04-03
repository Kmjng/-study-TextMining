# -*- coding: utf-8 -*-
"""
k평균 이용 : 문서 클러스터링
(k-means)  
거리 계산 방법은 '유클리드 거리'가 default임
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

# 예제 문서 데이터
documents = [
    "I don't like rainy days.",
    "She isn't feeling well today.",
    "They haven't finished their homework yet.",
    "He can't stand the cold weather.",
    "We didn't enjoy the movie at all.",
    "I love spending time with my family.",
    "She is an incredibly talented musician.",
    "They have accomplished so much in their careers.",
    "He always has a positive attitude.",
    "We had a fantastic time on our vacation."
]

doc2 = ["I'm tired of studying", "I don't wanna study",'I like lying at home',
        'welcome to my home', 'stop studying','home sweete home'
        ]

# TF-IDF 벡터화
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
#
tfidf_matrix2 = vectorizer.fit_transform(doc2)

# K-평균 클러스터링 수행
num_clusters = 2
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(tfidf_matrix)
#
kmeans.fit(tfidf_matrix2)
dir(kmeans)
'''
labels_ : 분류된 라벨 보여주는 속성 
'''
print(kmeans.labels_)
# >> [0 0 1 0 0 0 0 1 0 0] 10개의 문서에 대해 보여줌 

# numpy의 where 메소드 
# np.where(조건식) : 조건식에 맞는 배열요소 인덱스 반환 

# 클러스터 결과 출력
for i in range(num_clusters):
    cluster = np.where(kmeans.labels_ == i)[0] # 조건식의 True인 요소의 인덱스 반환
    print(f"Cluster {i+1}:")
    for doc_index in cluster :
        print(f" - {doc2[doc_index]}")       

'''
documents
Cluster 1:
 - I don't like rainy days.
 - She isn't feeling well today.
 - He can't stand the cold weather.
 - We didn't enjoy the movie at all.
 - I love spending time with my family.
 - She is an incredibly talented musician.
 - He always has a positive attitude.
 - We had a fantastic time on our vacation.
Cluster 2:
 - They haven't finished their homework yet.
 - They have accomplished so much in their careers.
'''

'''
doc2 
Cluster 1:
 - I'm tired of studying
 - I don't wanna study
 - stop studying
Cluster 2:
 - I like lying at home
 - welcome to my home
 - home sweete home
'''
