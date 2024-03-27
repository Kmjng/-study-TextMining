# -*- coding: utf-8 -*-
"""
 연속형 변수 시각화 : 산점도, 히스토그램, box-plot  
"""

import random # 난수 생성 
import statistics as st # 별칭 : 통계 함수 
import matplotlib.pyplot as plt # 별칭 : data 시각화 

# 차트에서 한글, 음수 부호 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


# 그래프 자료 생성 
data1 = range(-3, 7) # -3 ~ 6 # 이산형
data2 = [random.random() for i in range(10)]  #연속형 ??

# 1. 산점도 그래프 : 단일 색상 
# plt.scatter(x=, y=, c=, marker=, ) 
# c는 산점도에서 각 점의 색상을 지정하는 데 사용되는 매개변수 
plt.scatter(x=data1, y=data2, c='r', marker='o')
plt.title('scatter plot')
plt.show()


# 군집별 산점도 : 군집별 색상 적용 
cdata = [random.randint(1, 4) for i in range(10)]  # 난수 정수 
print(cdata)
# >> [1, 4, 3, 1, 2, 2, 2, 2, 2, 2]
plt.scatter(x=data1, y=data2, c=cdata, marker='o')
plt.title('scatter plot')
plt.show()


# 2. 히스토그램 그래프   
data3 = [random.gauss(mu=0, sigma=1) for i in range(1000)] 
print(data3) # 표준정규분포 

# 난수 통계 
# statistics 라이브러리 
dir(st)
'''
mean: 평균 
median : 중위수 
mode : 최빈수 
sqrt : 제곱근 
pstdev : 모집단의 표준편차 (sigma)
pvariance :모집단의 분산 - n으로 나눔 
stdev : 표본 표준편차 (s)
variance : 표본 분산 - n-1으로 나눔 
'''

st.mean(data3)
st.stdev(data3) 


# 정규분포 시각화 
# histogram 사용함 
# 연속형변수 사용, 계급으로 나누어 표현함 
plt.hist(data3, label='hist1') # 기본형 
plt.hist(data3, bins=20, histtype='stepfilled', label='hist2') 
# ★★★ 두 스케일이 다른이유는, 계급수(bins)를 달리하면서 
# 빈도수가 달라지기 때문 ★★★
# bins = 계급 개수 (default = 10 )
plt.legend(loc = 'best') # 범례 # loc = 레전드위치 
plt.show()
'''
loc 속성
best 
lower left/right
upper left/right
center 
'''


# 3. 박스 플롯(box plot)  : 기초통계 & 이상치(outlier) 제공 
# plt.boxplot() 
data4 = [random.randint(a=45, b=85) for i in range(100)]  

plt.boxplot(data4)
plt.show()

dir(st)
'''
quantiles : 사분위수 정보 
'''
st.quantiles(data4)
# >> [57.0, 66.0, 76.0]
# 제1, 제2, 제3
# 제2분위수는 중간값(median)

# 상한값 하한값 구하기 

# 정상 범주 
q3 = 76
q1 = 57
IQR = q3-q1

outlier_step = IQR*1.5
minval = q1 - outlier_step # 하한값 minval 
maxval = q3 + outlier_step # 상한값 maxval
