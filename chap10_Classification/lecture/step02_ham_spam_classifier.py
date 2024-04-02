# -*- coding: utf-8 -*-
"""
Naive Bayes 분류기
"""

from sklearn.naive_bayes import MultinomialNB # Naive Bayes model
from sklearn.metrics import accuracy_score, confusion_matrix # 평가 
import pickle

# 1. file save : chap09 (step03_Tfidf_sparse_matrix.py)에서 작성된 파일 
path = r"C:/ITWILL/3_TextMining/TextMining/data"
file = open(path + "/spam_train_test.pkl", mode='rb')
spam_train_test = pickle.load(file=file)
file.close()


X_train, X_test, y_train, y_test = spam_train_test # 그때 spam_train_test에 리스트 원소 4개로 넣었음
X_train.shape # (3901, 5000)
X_test.shape # (1673, 5000)
y_test.shape # (1673,)

#######################
### 2. NB model
#######################
# 1) 모델 학습 : 훈련셋 데이터 
model = MultinomialNB().fit(X = X_train, y = y_train) # model 학습 

# 2) 모델 평가를 위해 평가셋 이용 
y_predict = model.predict(X=X_test)
y_predict # 1 or 0 

# 3) 모델 평가 도구 : 혼동행렬 
con_mat = confusion_matrix(y_true = y_test, y_pred=y_predict) 
print(con_mat)
'''
[[1473   0]
 [  52  148]]

ham메세지 1473개 100%  
spam메세지 148/(52+148) : 진짜 스팸 중 맞춘 것 = 민감도(재현율) = 0.74
spam 메세지를 74% 밖에 맞추지 못함 (민감도가 좋지 못하다..)
'''

# 3) 평가도구 : accuracy_score  (정확도)
score = accuracy_score(y_true = y_test, y_pred= y_predict)
print(score) # 0.9689181111775254
print((1473+148)/(1473+148+52))

'''
정확도가 높게 나왔지만, 
ham과 spam 각각 1473, 200개..
★★★ 데이터 불균형으로 인해 정확도(Accuracy)로 객관적으로 평가하기 어렵다. 
혼동행렬을 보면 알 수 있음 
True(spam) 의 민감도(재현율)가 좋지 못하므로 
F1 score 를 확인해본다. 
'''

# 평가방법 : 정밀도, 재현율(민감도), F1 점수 

# precision = TP/(TP+FP)
p  = 148/148  # 1.0

# recall = TP/(TP+FN)
r = 148/(52+148)  # 0.74

# F1 score = 2*(p*r)/(p+r)
f1 = 2*(p*r)/(p+r)
print(f1) # 0.8505747126436781
