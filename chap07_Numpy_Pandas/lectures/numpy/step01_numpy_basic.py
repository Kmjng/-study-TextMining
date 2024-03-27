# -*- coding: utf-8 -*-
"""
저수준 자료구조 : list, dict
고수준 자료구조 : numpy, pandas - 다양한 분석도구 제공


Numpy 패키지 
  - 수치 과학용 데이터 처리 목적으로 사용 
  - 다차원 배열, 고속 연산  
  - 수학/통계 함수 제공 
  - 행렬 연산(broadcast연산) 가능 ★★ -> list와 차이점
  
  배열(array)의 다양한 색인
  - [행][열]
  - [행,열]
  - 3차원일 경우, [x,y,z] 
  
  주의 : pandas에서는 [열][행]
"""

import numpy as np # 별칭 

# 1. list 배열 vs 다차원 배열 
a =[1,2,3,4,5]
b = np.array(a) 
type(a) # >> class 'list'
type(b) # >> class 'numpy.ndarray'



# 1) list 배열
lst = [1, 2, 3, 3.5] # 정수와 실수 자료형 # 서로다른 자료형
type(lst[0]) # >> int
type(lst[3]) # >> float
sum(lst) # 외부 함수 

# 2) 다차원 배열 
arr = np.array(lst) # array([list])  
# >> [1, 2, 3, 3.5] 동일한 자료형으로 저장됨 (float)
type(arr[0]) # >> numpy.float64
type(arr[3]) # >> numpy.float64
arr.sum() # 자체 제공 
arr2 = np.array([3,4,'a'])
type(arr2[0]) # >> numpy.str_
type(arr2[2]) # >> numpy.str_

# 2. array() : 다차원 배열 생성 

# 1) 단일 list  
lst1 = [3, 5.2, 4, 7]
print(lst1) # 단일 리스트 배열 

# list -> 다차원배열
arr1d = np.array(lst1) 
print(arr1d.shape) # 자료구조 확인

# 2) 중첩list -> 2차원 배열 

lst2 = [[1,2,3,4], [5,6,7,8]]
print(lst2)

# list -> 다차원배열
arr2d = np.array(lst2) 
print(arr2d.shape) # 자료구조 확인
# >> (2,4) 
print(arr2d[0][1:3]) # >> [2 3]

# 3중 중첩 list -> 3차원배열 
lst3 =[[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]]
arr3d = np.array(lst3)
print(arr3d.shape) # >> (2,2,4) # (면,행,열) ★★★★
# 주의: (2,4,2)가 아님 
print(arr3d)
'''
# 1면
[[[1 2 3 4]
  [5 6 7 8]]
# 2면
 [[1 2 3 4]
  [5 6 7 8]]]
'''

# 3. broadcast 연산 : 배열 간 사칙연산  
# lst1 = [3, 5.2, 4, 7]
# lst2 = [[1,2,3,4], [5,6,7,8]]
print(0.5 * arr1d)

print(0.5 * arr2d)

print(arr1d * arr2d) 
'''
[[ 3.  10.4 12.  28. ]
 [15.  31.2 28.  56. ]]
'''


'''
예) 표본 분산 = sum((X-산술평균)**2) / n-1
'''
X =[1,5,3,5.6,7]
x =np.array(X)
dir(x)
'''
var -> 모분산 메소드
'''
x_bar = x.mean() 
var = sum((x-x_bar)**2)/(len(x)-1)
print(var) # >> 5.512
var_x = x.var()
print(var_x) # >> 4.409599 >> n으로 나눔 (모분산)

# 4. zeros or ones 
# 영행렬 만드는 메소드 (괄호 안에 차원 튜플로 들어간다.★★★)
zerr = np.zeros( (3, 10) ) # 3행10열 
print(zerr) # 희소행렬 : doc(3) vs word(10) 빈도수 


onearr = np.ones( (3, 10) ) # 3행5열 
print(onearr)

# 1~30 
cnt = 0 
for i in range(3):
    for j in range(10): 
        cnt += 1
        zerr[i,j] =cnt
        #zerr[i][j] =cnt
print(zerr)
