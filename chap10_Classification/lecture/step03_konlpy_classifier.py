# -*- coding: utf-8 -*-
"""
한글문서를 대상으로 한 문서분류기   
"""

import pandas as pd # csv file 
from sklearn.feature_extraction.text import TfidfVectorizer #DTM 생성기
from sklearn.preprocessing import LabelEncoder # 10진수 인코딩 

from sklearn.naive_bayes import MultinomialNB # 분류모델 생성
from sklearn.metrics import accuracy_score, confusion_matrix # 모델 평가  

from konlpy.tag import Okt # 한글 형태소분석기 
okt = Okt() # 객체 생성  


### 1. csv file 가져오기 : cafe에서 다운로드 
path = r"C:/ITWILL/3_TextMining/TextMining/data"
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
 3   title   14725 non-null  object  : 영화 제목   => y변수
'''
print(movie_review.head())


### 2. 변수 선택  
new_df = movie_review[['review', 'title']]  
new_df.shape  # (9773, 2)


# y변수 : 영화제목 6개 
title = new_df.title
title.unique()
'''
array(['인피니티 워', '라라랜드', '곤지암', '범죄도시', 
       '택시운전사', '코코'], dtype=object)
'''
# x변수 : 영화 감상평 
review = new_df.review

### 3. 변수 전처리 
# y변수 : 레이블 인코딩 
y = LabelEncoder().fit_transform(title)# 오름차순으로 10진수 인코딩 
y # >> array([3, 3, 3, ..., 4, 4, 4]) 

df1 = pd.DataFrame({'title':title,'y':y})
df1.y.unique() # array([3, 1, 0, 2, 5, 4])

# X변수 : DTM  
tfidf = TfidfVectorizer(tokenizer=okt.nouns, max_features=4000, min_df=5, max_df=0.5)
'''
tokenizer = okt.nouns : 한글 형태소분석기로 쪼개겠다.
(★★★영문의 경우 굳이 안써도 되는데 한글의 경우 형태소 분석기를 선택해 줘야함)
max_features = 4000 : 최대 사용할 단어개수 
min_df=5 : 너무 희소하게 나오는 단어는 제거
max_df=0.5 : 너무 자주 나타나는 단어는 제거 (50% 정도 들어가면 제거한다.)
'''
DTM = tfidf.fit_transform(review) # review 칼럼 원문 객체 반영하고 변환
DTM = DTM.toarray()
DTM.shape # (9773, 2072) # 남아있는 단어 2072 개 



### 4. 훈련셋/테스트셋 split
from sklearn.model_selection import train_test_split  

X_train, X_test, y_train, y_test = train_test_split(
            DTM, y, test_size=0.25, random_state=0) 
# train_test_split() 인자에 학습시킬 데이터를 넣는다.(DTM, y)
# parameter 중, random_state = 0 : 학습, 훈련데이터 똑같은 내용으로 fix (시드값)
# y_test는 X_test에 대한 정답지

### 5. NB model
nb = MultinomialNB()
model = nb.fit(X = X_train, y = y_train)

y_pred = model.predict(X = X_test)  
y_true = y_test

acc = accuracy_score(y_true, y_pred)
print('NB 분류정확도 =', acc)
# >> NB 분류정확도 = 0.7184942716857611

con_mat = confusion_matrix(y_true, y_pred)
print(con_mat)
'''
정확도는 72% 가량 나왔는데, 자세히 확인해보면 이렇다. 
     0   1   2   3   4   5
0[[260   2  32  45   0  46]
1 [ 21 165  20  22   1  62]
2 [ 16   0 368  41   1  51]
3 [ 33   3  32 363   0  68]
4 [  3  11  10  24  82  75]  => '코코'
5 [ 10   7  25  27   0 518]]  => '택시운전사' 영화 리뷰 분류가 잘됐다.
'''

