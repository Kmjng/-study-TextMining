# -*- coding: utf-8 -*-
"""
코사인 유사도를 이용한 문서 군집화

sklearn말고 nltk로 만들어보자 

"""

from nltk.cluster import KMeansClusterer # 군집화 
from nltk.corpus import stopwords # 불용어 #★ for preprocessing
from nltk.tokenize import word_tokenize # 토큰 생성 #★ for preprocessing
from nltk.stem import PorterStemmer # 어근 처리 #★ for preprocessing
from nltk.cluster.util import cosine_distance # 코사인 거리계산 
from sklearn.feature_extraction.text import TfidfVectorizer # 문서 벡터화

# NLTK 데이터셋 설치
import nltk
nltk.download('stopwords') # 불용어 데이터
nltk.download('punkt') # token 생성 


# 1. 테스트 문서(documents)
documents = [
    "I love to watch movies",
    "I like reading books",
    "I enjoy playing sports",
    "I love traveling"
]


# 2. 전처리 함수: 소문자 변환, 토큰화, 불용어 제거, 어간 추출
def preprocess(text):
    tokens = word_tokenize(text.lower())  # 소문자 변환 & 토큰화
    stop_words = stopwords.words("english")  # 영어 불용어(인칭,전치사)
    # 단어(token) 선별 작업 : 영문 불용어 제외  
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]  
    # 어근 처리: 분사 or 동명사 => 원형 동사
    stemmer = PorterStemmer()  # 어근 처리 
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    return stemmed_tokens

result = [preprocess(doc) for doc in documents]
print(result)
'''
[['love', 'watch', 'movi'], ['like', 'read', 'book'],
 ['enjoy', 'play', 'sport'], ['love', 'travel']]
'''
# 3. DTM(TF-IDF) 만들기 (희소행렬화를 통해 수치화한다.)
vectorizer = TfidfVectorizer(tokenizer=preprocess) # 토큰(단어) 생성기  
# tokenizer = : 쪼개는 방법 지정
# 주의: 함수 호출 시 괄호 x 
DTM = vectorizer.fit_transform(documents) # DTM  
DTM_arr = DTM.toarray() # numpy 배열 변경  
print(DTM_arr)
'''
[[0.         0.         0.         0.48693426 0.61761437 0.
  0.         0.         0.         0.61761437]
 [0.57735027 0.         0.57735027 0.         0.         0.
  0.57735027 0.         0.         0.        ]
 [0.         0.57735027 0.         0.         0.         0.57735027
  0.         0.57735027 0.         0.        ]
 [0.         0.         0.         0.6191303  0.         0.
  0.         0.         0.78528828 0.        ]]
'''
DTM_arr.shape # (4,10) 

# 4. K-Means 군집화
#  ★★★ 코사인거리 계산 방법으로 군집화 하겠다.
num_clusters = 2  # 군집 개수 
kmeans_clusterer = KMeansClusterer(num_clusters, distance=cosine_distance, repeats=25)
'''
num_clusters : 군집수 지정
distance : 유사도 거리 계산 방법 지정 
repeats : 반복학습 수 지정
'''
assigned_clusters = kmeans_clusterer.cluster(DTM_arr, assign_clusters=True)
assigned_clusters # [0, 1, 1, 0] (1,4)2,3번째 문서가 비슷

# 5. K-Means 군집화 결과 : 각 문서의 군집화 결과 
for index, document in enumerate(documents):
    cluster_num = assigned_clusters[index]
    print(f"Document: {document},  Cluster: {cluster_num}")
    
'''
Document: I love to watch movies,  Cluster: 0
Document: I like reading books,  Cluster: 1
Document: I enjoy playing sports,  Cluster: 1
Document: I love traveling,  Cluster: 0
'''
