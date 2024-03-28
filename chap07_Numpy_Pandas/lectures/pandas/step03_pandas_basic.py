# -*- coding: utf-8 -*-
"""
Series & DataFrame

1. Series 자료 특징 
 - 1차원 구조
 - index와 value 구성

2. DataFrame 자료구조 특징 
 - 2차원 행렬구조(DB의 Table 구조와 동일함)
 - 칼럼 단위 상이한 자료형 
"""

import pandas as pd 


# 1. Series 객체 생성

ages = [35, 45, 55, 25]
ser = pd.Series(ages) 
print(ser) 
dir(ser)
'''
statistics와 마찬가지로, pandas에서도 mean() 메소드 지원함.
'''

# 색인 추출
ser.index # >> RangeIndex(start=0, stop=4, step=1)
# 값 추출 
ser.values # >> array([35, 45, 55, 25], dtype=int64)

# 평균 
ser.mean() 
# pandas 기본차트 제공
ser.plot() 
ser.plot(kind='bar') # 유형 지정도 가능 
# 더 

# 2. DataFrame 객체 생성 

# 1) list와 dict 이용  
names = ['hong', 'lee', 'kim', 'park']
ages = [35, 45, 55, 25]
pays = [250, 350, 450, 250]

frame = pd.DataFrame({'name':names, 'age': ages, 'pay': pays})
print(frame)

frame.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3  => 행 길이 ★
Data columns (total 3 columns):  => 열 길이 ★
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    4 non-null      object  => 문자열
 1   age     4 non-null      int64   => 결측치 유무 파악 가능
 2   pay     4 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 228.0+ bytes
'''

# 행 이름과 열이름 
frame.index
frame.columns

# DataFrame에서의 칼럼 추가 
# Series 클래스 이용한다.

gender = pd.Series(['M','M','F','F'])
frame['gender'] = gender



# 2) numpy 객체 이용
# arange(n): 0~n-1까지의 수 ★★★ (range()와 비슷한 역할)
# reshape(m,n): 행렬 구조 바꿔줌

import numpy as np
help(np.arange)
'''
np.arange(3,7)
    array([3, 4, 5, 6])
np.arange(3,7,2)
    array([3, 5])
'''
data = np.arange(12).reshape(3, 4)
print(data)

# 배열data를 DataFrame으로
frame2 = pd.DataFrame(data, columns=['a','b','c','d']) # 칼럼명 지정 
print(frame2)
'''
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''
data[:,0] # 1열 선택 
# >> array([0, 4, 8])

frame2['a'] # 1열 선택 
'''
0    0
1    4
2    8
Name: a, dtype: int32
'''
frame2.iloc[:,0] # 위와 동일
frame2.loc[:,'a'] # 동일

# 행 단위 평균 => 열 보존 => axis = 1
data.mean(axis = 1) 
frame2.mean(axis = 1)

# 행 이름, 열 이름 변경 
frame2.index =['i','j','k'] # 인덱스(행 이름)★★★ 변경 
print(frame2)
frame2.columns = ['aa,','bb','cc','dd']
'''
   aa,  bb  cc  dd
i    0   1   2   3
j    4   5   6   7
k    8   9  10  11
'''
