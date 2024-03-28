# -*- coding: utf-8 -*-
"""
문1) 다음과 같은 data와 base를 대상으로 numpy의 broadcast 연산 방식을 적용하여     
     유클리드 거리계산식으로 두 자료의 거리를 단계별로 구하시오.
"""

import random # 난수 생성 
from statistics import sqrt # 제곱근(루트)
random.seed(100) # 난수 seed값 지정(난수 고정) 

### 단계1. data 생성 
# 1) 적용데이터셋 5개
data = [[round(random.random(),5), round(random.random(),5)] for i in range(5)]
# 5행2열 

# 2)기준데이터셋 1개 
base = [round(random.random(),5), round(random.random(),5)]

print('data :', data) # data : [[0.14567, 0.45493],[],,,,]
print('base : ', base) # base :  [0.77078, 0.70551]


# 유클리드 거리계산식 = sqrt( sum((p - q)^2) )

import numpy as np

# 단계1 : data -> q, base -> p 변수로 numpy 배열 만들기 
q = np.array(data)
p = np.array(base)
print(q.shape) # >> (5,2) 
print(q)
# ★★★ 참고로, 1차원 배열의 인덱스는 한개이다. ★★★ 
# 단계2 : 차의 제곱 : (p - q)^2
diff = (q-p)**2 
print(diff) 
'''
[[0.00150699 0.073984  ]
 [0.00085498 0.02979421]
 [0.4769698  0.06228019]
 [0.52256995 0.0517335 ]
 [0.03108169 0.13701843]]
'''
# 단계2 : 합 : sum((p - q)^2)
# numpy의 sum()을 사용해야 broadcast 연산이 가능하다. ★★★
# 따라서 내장함수가 아닌 numpy라이브러리 메소드로 사용한다. 
# 행 단위로 연산하고자 할 때
# axis = 0 => 열 내에서 연산
# axis = 1 => 행 내에서 연산

diff_sum = diff.sum(axis = 1)
diff_sum1 = np.sum(diff, axis =1) # 동일한 방법
print(diff_sum) 
print(diff_sum1)
'''
[0.07549099 0.03064919 0.53924999 0.57430345 0.16810012]
'''

# 단계3 : 제곱근 : sqrt(sum((p - q)^2))
# 각각에 제곱근 해준다. 
# statistics가 아닌 numpy 라이브러리의 메소드로 사용한다.
distance = np.sqrt(diff_sum)
distance1 = diff_sum.sqrt() # 안됨

print('두 점의 거리 =', distance) 

# 산점도 시각화
import matplotlib.pyplot as plt 
q_x = [q[i][0] for i in range(5)]
q_y = [q[i][1] for i in range(5)]
plt.scatter(x= q_x, y= q_y, label='q')
plt.scatter(x=p[0], y=p[1], c='blue', label='p')
plt.legend()
plt.show()

