# -*- coding: utf-8 -*-
"""
코사인 유사도를 이용한 문서 군집화
"""



from nltk.cluster import KMeansClusterer # 군집화 
from nltk.corpus import stopwords # 불용어 
from nltk.tokenize import word_tokenize # 토큰 생성 
from nltk.stem import PorterStemmer # 어근 처리 
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
  
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]  
    stemmer = PorterStemmer()  # 어근 처리 
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    return stemmed_tokens

result = [preprocess(doc) for doc in documents]


# 3. DTM(TF-IDF) 만들기 
vectorizer = TfidfVectorizer(tokenizer=preprocess) # 토큰(단어) 생성기  
DTM = vectorizer.fit_transform(documents) # DTM  
DTM_arr = DTM.toarray() # numpy 배열 변경  


# 4. K-Means 군집화
num_clusters = 2  # 군집 개수 
kmeans_clusterer = KMeansClusterer(num_clusters, distance=cosine_distance, repeats=25)

assigned_clusters = kmeans_clusterer.cluster(DTM_arr, assign_clusters=True)


# 5. K-Means 군집화 결과 : 각 문서의 군집화 결과 
for index, document in enumerate(documents):
    cluster_num = assigned_clusters[index]
    print(f"Document: {document},  Cluster: {cluster_num}")
    
    
    
