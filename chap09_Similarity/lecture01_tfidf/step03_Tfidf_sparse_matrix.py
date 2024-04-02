# -*- coding: utf-8 -*-
"""
스팸 메시지 -> 문서단어행렬(DTM) 만들기 

1. csv file 가져오기 
2. texts, target 전처리 
3. max features
4. DTM (TFiDF 가중치 사용)
5. train/test split (데이터 세트 분류)
6. file save ( 파일 저장 )
"""

import pandas as pd # csv file 
from sklearn.feature_extraction.text import TfidfVectorizer 
import numpy as np

# 1. csv file 가져오기  
path = r"C:/ITWILL/3_TextMining/TextMining/data"
spam_data = pd.read_csv(path + '/spam_data.csv', header=None, encoding='utf-8')

print(spam_data)
'''
         0                                                  1
0      ham  Go until jurong point, crazy.. Available only ...
1      ham                      Ok lar... Joking wif u oni...
2     spam  Free entry in 2 a wkly comp to win FA Cup fina...
3      ham  U dun say so early hor... U c already then say...
4      ham  Nah I don't think he goes to usf, he lives aro...
   ...                                                ...
5569  spam  This is the 2nd time we have tried 2 contact u...
5570   ham                Will  b going to esplanade fr home?
5571   ham  Pity, * was in mood for that. So...any other s...
5572   ham  The guy did some bitching but I acted like i'd...
5573   ham                         Rofl. Its true to its name

[5574 rows x 2 columns]
'''
spam_data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5574 entries, 0 to 5573
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       5574 non-null   object => ham(0)/spam(1) 로 할 것임 (y변수)
 1   1       5574 non-null   object => msg => DTM(TFiDF) 처리할 것임 (x변수)
dtypes: object(2)
memory usage: 87.2+ KB
'''
# 2) target, texts 전처리 : 공백, 특수문자, 숫자  
target = spam_data[0]
target = np.array(target) # 배열화
print(target)
'''
['ham' 'ham' 'spam' ... 'ham' 'ham' 'ham']
'''

# 가변수(더미변수) 만들기 
target = [1 if t=='spam' else 0 for t in target]
print(target)
target = np.array(target)

# 전처리 전
texts = spam_data[1]
print(texts)

# << texts 전처리 함수 >> 
import string # texts 전처리
def text_prepro(texts): # 문단(sentences)
    # Lower case : 문단 -> 문장 -> 영문소문자 변경  
    texts = [x.lower() for x in texts]
    # Remove punctuation : 문단 -> 문장 -> 음절 -> 필터링 -> 문장  
    texts = [''.join(ch for ch in st if ch not in string.punctuation) for st in texts]
    # Remove numbers : 문단 -> 문장 -> 음절 -> 필터링 -> 문장 
    texts = [''.join(ch for ch in st if ch not in string.digits) for st in texts]
    # Trim extra whitespace : 문단 -> 문장 -> 공백 제거 
    texts = [' '.join(x.split()) for x in texts]
    return texts

texts = text_prepro(texts)
# 전처리 후 
print(texts)

# 3. max features : 문서단어행렬(DTM) 차원 결정 
fit = TfidfVectorizer().fit(texts) # 단어 생성기 
voca = fit.vocabulary_
len(voca) # >> 8603 : 전체 단어수 
# DTM으로 보면, (5574,8603).. 
# 크기가 크기 때문에 단어수를 줄인다. (메모리, 연산 효율을 위해)
max_features = 5000 # 전체 단어수 변경
# ★★★ feature => x변수 ★★


# 4. DTM : max features 지정 
tfidf = TfidfVectorizer(max_features = max_features, stop_words='english')
# max_features = max_feature >> 최대사용할 단어 수 
# 불용어를 제거한 후에 가장 중요한 5000개의 단어를 선택
# stop_words='english' >> 영문불용어를 제외한다.


# 문서단어 행렬(DTM)  
dtm = tfidf.fit_transform(texts)

# numpy array 변환 
dtm_arr = dtm.toarray()
print(dtm_arr)
'''
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
'''

# 5. train/test split
from sklearn.model_selection import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(
    dtm_arr, target, test_size=0.3)  # 30%을 test set로 
# x에 dtm_arr (문장수,빈도수) , 
# y에 target (0과 1)
dtm_arr.shape # >> (5574, 5000)

target.shape # >> (5574,)

x_train.shape # >> (3901, 5000) # 70 % 
y_train.shape # >> (3901,) 

x_test.shape # >> (1673, 5000) # 30 %
y_test.shape # >> (1673,) 

# 6. file save 
import pickle 

spam_train_test = [x_train, x_test, y_train, y_test]

file = open(path + "/spam_train_test.pkl", mode='wb')
pickle.dump(obj=spam_train_test, file=file) # pickle파일로 인코딩
# 배열을 인코딩하는 거니까 dumps말고 dump 사용
# 참고로 pickle은 dump만 씀 
file.close()

# pickle 파일 읽기
file2 = open(path + "/spam_train_test.pkl", mode='rb')
pickle.load(file2)
