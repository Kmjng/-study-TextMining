# -*- coding: utf-8 -*-
"""
간단한 문서 분류기(simple texts classifier) 
"""

import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer # DTM 
from sklearn.naive_bayes import MultinomialNB # Naive Bayes model
from sklearn.metrics import confusion_matrix, accuracy_score # model 평가도구 
# ★★★ confusion_matrix : 혼동행렬
# ★★★ accuracy_score : 분류정확도


# 1. dataset 만들기 
target = [1,0,1,0,1,0,1,0,1,0] # y변수 : 정답(1:부정, 0:긍정)
texts = [
    "I don't like rainy days.",
    "I love spending time with my family.",
    "She isn't feeling well today.",
    "She is an incredibly talented musician.",
    "They haven't finished their homework yet.",
    "They have accomplished so much in their careers.",
    "He can't stand the cold weather.",
    "He always has a positive attitude.",
    "We didn't enjoy the movie at all.",
    "We had a fantastic time on our vacation." ] # x변수 : DTM 화 할 것

train_set = pd.DataFrame({'target' : target, 'texts' : texts})

# 훈련용 데이터셋  
print(train_set)
'''
   target                                             texts
0       1                          I don't like rainy days.
1       0              I love spending time with my family.
2       1                     She isn't feeling well today.
3       0           She is an incredibly talented musician.
4       1         They haven't finished their homework yet.
5       0  They have accomplished so much in their careers.
6       1                  He can't stand the cold weather.
7       0                He always has a positive attitude.
8       1                 We didn't enjoy the movie at all.
9       0          We had a fantastic time on our vacation.
'''


# 테스트용 데이터셋    
test_texts = ["I don't like chocolate ice cream.",    
              "She isn't going to the party tonight.",
              "I love spending time with my family.",
              "They didn't finish their homework on time."]
# 실제 정답
test_target= [1,1,0,1] # 최종적으로 정답은 이렇게 나와야함 


# 2. 훈련용 X, y변수 만들기  

# 1) 훈련용 y변수 
y_train  = train_set.target 
y_train.shape # (10,) 
 
# 2) 훈련용 X변수 (DTM으로 변경하고 배열화해서 저장해야함)
texts = train_set.texts
type(texts) #  >> pandas.core.series.Series
obj = TfidfVectorizer()
dtm = obj.fit_transform(texts) # ★
# ★★★대문자 X 사용하는 이유는 2차원 행렬(희소행렬)이기 때문에 
X_train = dtm.toarray()
X_train.shape # (10,53) 10개의 문장, 53개의 단어 ★★★

# 3. Naive Bayes 분류기 (훈련세트 10개 문장 이용)
nb = MultinomialNB()
model = nb.fit(X_train, y_train)
dir(model)
'''
predict() : y 예측치(Predicted target values for X.)
         X : array-like of shape (n_samples, n_features)
             The input samples.
score() : 평가점수
'''
help(model.predict)


# 테스트용 문장 예측하기
dtm_test = obj.transform(test_texts) # ★
X_test = dtm_test.toarray() 
X_test.shape # (4, 53) 4개의 문장을 53개의 단어에 대한 출현 비율 

y_predict = model.predict(X= X_test) 
print(y_predict) # [1 1 0 1]

# 모델 평가 (혼동행렬 confusion_matrix 사용)
# y_true, y_pred 두개의 인수가 들어간다. 
# y_true는 실제값 
con_mat = confusion_matrix(y_true = test_target, y_pred = y_predict)
print(con_mat)
'''0 1
0[[1 0]
1 [0 3]]
    칼럼이 예측에 대한 T/F
    행축은 실제 T/F  
    주대각선이 정분류율
'''
# 모델 평가 (방법2) (분류정확도 accuracy_score) 
# 평가셋 데이터에 대한 예측값과 실제값을 비교해 정확도를 계산
score = accuracy_score(y_true = test_target, y_pred= y_predict)
print(score) # >> 1.0

# 모델 평가 (방법3) 나이브베이즈 분류기 자체 기능 
# 훈련셋, 평가셋 둘다 사용 가능 
# X_test에 대해 분류기로 예측하고 실제값과 비교한다.
# 그래서 y 인자에 실제 y값이 들어간다. 
model.score(X=X_train, y=y_train ) # >> 1.0
model.score(X=X_test, y=test_target ) # >> 1.0
