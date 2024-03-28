# -*- coding: utf-8 -*-
"""
1. DataFrame의 요약통계량 
2. 상관계수
"""

import pandas as pd # 별칭 

# 실습용 DataFrame 생성   
name = ['hong', 'lee', 'kim', 'park']
age = [35, 45, 55, 25]
pay = [250, 350, 450, 250]
gender = pd.Series(['M', 'M', 'F', 'F'])

frame = pd.DataFrame(data ={'name':name, 
                      'age': age, 
                      'pay': pay,
                      'gender':gender}, columns=['name','age','pay','gender'])
print(frame)
frame.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3   => 관측치
Data columns (total 4 columns):   => 변수(변인)
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    4 non-null      object : 문자형 (범주형x)
 1   age     4 non-null      int64  : 숫자형(연속)
 2   pay     4 non-null      int64  : 숫자형(연속)
 3   gender  4 non-null      object : 문자형(범주형)
dtypes: int64(2), object(2)
memory usage: 260.0+ bytes
'''

# 1. DataFrame의 요약통계량 ★★★
desc = frame.describe() # 대상: 숫자형 칼럼
print(desc)
'''
             age         pay
count   4.000000    4.000000
mean   40.000000  325.000000
std    12.909944   95.742711
min    25.000000  250.000000
25%    32.500000  250.000000
50%    40.000000  300.000000
75%    47.500000  375.000000
max    55.000000  450.000000
'''
Q3 = desc.loc['75%']
Q1 = desc.loc['25%']
IQR = Q3-Q1 
IQR 
'''
age     15.0
pay    125.0
dtype: float64
'''
frame.age.plot(kind ='box')


# 전체 사원의 나이와 급여 평균 
frame[['age','pay']].mean(axis = 0) # 열 내에서 계산 

frame[['age','pay']].mean(axis =1) # 행 내에서 계산
frame


# 산포도 : 분산, 표준편차 
frame[['age','pay']].var() # axis = 0
frame[['age','pay']].std() # axis = 0


# 2. 빈도 분석 
# 빈도수 : 집단변수 
frame['gender'].value_counts()

# 유일값 
frame['gender'].unique()
# array(['M', 'F'], dtype=object)


# 3. 상관관계 
frame[['age','pay']].corr()
'''
         age      pay
age  1.00000  0.94388
pay  0.94388  1.00000
'''


