# -*- coding: utf-8 -*-
'''
문3) 다음 두 기업의 주가를 시계열 자료로 이용하여 시각화하시오.

    <시각화 결과> exam03.pdf 참고             
'''

import pandas as pd # 날짜 자료 생성 
import numpy as np # 수치 자료 생성 
import matplotlib.pyplot as plt # 시각화 

np.random.seed(1234) # 시드값 적용 (동일한 난수를 제공한다.)
 
# 두 기업 주식 자료 생성 : 2년치 주식 가격 

# 년도(x축 데이터) 
# 날짜 변수. pandas 제공
# pd.date_ragne(start=,end=,freq=)
date = pd.date_range(start='2009-01-01', end='2010-12-31', freq='D') 

help(np.random.randn)
APPLE = np.cumsum(np.random.randn(len(date))) + 100 # 애플사 주가 
MS = np.cumsum(np.random.randn(len(date))) + 120 # 마이크로소프트사 주가 


# 주식 가격 데이터 시각화
fig = plt.figure(figsize=(10, 5)) # 차트 크기 

chart = fig.add_subplot()

chart1 = chart.plot(date, APPLE , label='APPLE')
chart2 = chart.plot(date, MS, label='MS')

dir(chart1)


plt.legend()
plt.xlabel('기간 (2009년~2010년)')
plt.ylable('주식가격')
plt.suptitle('애플 vs 마이크로소프트 주가 변동 현황')
plt.show()


# random 관련 
# np.random.rand(m.n)
# 0~1 균일분포 표준정규분포 난수
# np.random.randn(m,n)
# 평균0, 표준편차1의 가우시안 표준정규분포 난수
# m*n matrix 표현
