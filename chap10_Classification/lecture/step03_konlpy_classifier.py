# -*- coding: utf-8 -*-
"""
한글문서를 대상으로 한 문서분류기   
"""

import pandas as pd # csv file 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.preprocessing import LabelEncoder 

from sklearn.naive_bayes import MultinomialNB 
from sklearn.metrics import accuracy_score, confusion_matrix  

from konlpy.tag import Okt # 한글 형태소분석기 
okt = Okt() # 객체 생성  


### 1. csv file 가져오기 : cafe에서 다운로드 
path = r"C:\ITWILL\3_TextMining\data"
movie_review = pd.read_csv(path + '/daum_movie_reviews.csv', encoding='utf-8')

print(movie_review.info())
'''
RangeIndex: 14725 entries, 0 to 14724
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   review  14725 non-null  object  : 영화 후기 
 1   rating  14725 non-null  int64   : 점수(1~10)
 2   date    14725 non-null  object  : 작성 날짜
 3   title   14725 non-null  object  : 영화 제목 
'''
print(movie_review.head())


### 2. 변수 선택  
new_df = movie_review[['review', 'title']]  
new_df.shape 


# y변수 : 영화제목 6개 
title = new_df.title

# x변수 : 영화 감상평 
review = new_df.review



### 3. 변수 전처리 

# y변수 : 레이블 인코딩 
y = LabelEncoder().fit_transform(title)

# X변수 : DTM  
tfidf = TfidfVectorizer(tokenizer=okt.nouns, max_features=4000, min_df=5, max_df=0.5)
'''
tokenizer = okt.nouns : 한글 형태소분석기 
max_features = 4000 : 최대 사용할 단어개수 
min_df=5 : 너무 희소하게 나오는 단어는 제거
max_df=0.1 : 너무 자주 나타나는 단어는 제거
'''
DTM = tfidf.fit_transform(review)
DTM = DTM.toarray()



### 4. 훈련셋/테스트셋 split
from sklearn.model_selection import train_test_split  

X_train, X_test, y_train, y_test = train_test_split(
            DTM, y, test_size=0.25, random_state=0)



### 5. NB model
nb = MultinomialNB()
model = nb.fit(X = X_train, y = y_train)

y_pred = model.predict(X = X_test)  
y_true = y_test

acc = accuracy_score(y_true, y_pred)
print('NB 분류정확도 =', acc)

con_mat = confusion_matrix(y_true, y_pred)
print(con_mat)
