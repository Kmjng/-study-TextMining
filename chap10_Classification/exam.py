# -*- coding: utf-8 -*-
"""
문) 각 단계별로 Naive Bayes 학습모델을 만들고 평가셋으로 평가하시오.
    <조건> X변수 : reviews 칼럼, y변수 : label 칼럼 
    
    긍정/부정 분류 모델
"""

import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer # DTM
from sklearn.naive_bayes import MultinomialNB # nb model
from sklearn.metrics import accuracy_score, confusion_matrix # 평가 도구 

# 1. dataset load 
path = r'C:/ITWILL/3_TextMining/TextMining/data'
data = pd.read_csv(path + '/movie_reviews.csv')
print(data.info())
'''
 0   reviews  1492 non-null   object : X변수 
 1   title    1492 non-null   object
 2   label    1492 non-null   int64  : y변수 
''' 
data.shape # (1492, 3) # 1492개의 데이터셋

# 2. X, y변수 준비 
X = data.reviews # 영문 자연어 
y = data.label # 1 긍정, 0 부정
# 데이터셋 전체 희소행렬화(임베딩)
obj = TfidfVectorizer()
dtm = obj.fit_transform(X)
X = dtm.toarray() 
X.shape # (1492, 34945) 
y.shape # (1492,)


# 3. 훈련셋/평가셋 분류(80% vs 20%) 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2)

# 4. model 학습 : 훈련셋 
nb = MultinomialNB() 
model = nb.fit(X= X_train, y= y_train) # train 데이터로 훈련 학습 

# 5. model 평가 : 평가셋 
X_test.shape # (299, 34945)
y_predict = model.predict(X_test) # 평가셋 예측


# 1) 혼동행렬 
con_mat = confusion_matrix(y_true = y_test, y_pred = y_predict) # y_predict는 위에서 예측한 거
print(con_mat)
''' 0   1
0[[106  44]  실제 부정문 : 150
1 [ 15 134]] 실제 긍정문 : 149 
균등비율로 구성되어 있음

'''
# 2) 분류정확도 
acc = accuracy_score(y_true= y_test, y_pred = y_predict)
print(acc) # 0.802675585284281

# 재현율 구해보기 
recall = 134/(134+15)
print(recall) # 0.8993288590604027
