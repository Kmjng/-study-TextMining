# -*- coding: utf-8 -*-
"""
  서브플롯(subplot) 차트 시각화 
  서브플롯만들 때, ‘피규어 객체’를 만들어준다.
  fig객체 = plt.figure(figsize = (x픽셀값,y픽셀값)) 
  plt객체 = fig객체.add_subplot()
"""

import random # data 생성 
import matplotlib.pyplot as plt # data 시각화 


# 1. subplot 생성 

# figure 객체 생성 .figure()
fig = plt.figure(figsize = (10, 5)) # 차트 크기 지정 
dir(fig)
'''
add_subplot
legend
suptitle
set_title
'''

# subplot 객체 생성 .add_subplot() 
x1 = fig.add_subplot(2,2,1) # 2행2열 중 1 객체
x2 = fig.add_subplot(2,2,2) # 2행2열 중 2 객체
x3 = fig.add_subplot(2,2,3) # 2행2열 중 3 객체  
x4 = fig.add_subplot(2,2,4) # 2행2열 중 4 객체 

# 2.차트 데이터 생성 
data1 = [random.gauss(mu=0, sigma=1) for i in range(100)]
data2 = [random.randint(1, 100) for i in range(100)] # 1 ~ 100
cdata = [random.randint(1, 4) for i in range(100)] # 1 ~ 4


# 3. 각 격자에 차트 크리기 
x1.hist(data1) # 히스토그램 
x2.scatter(data1, data2, c=cdata) # 산점도 
x3.plot(data2) # 기본 차트 
x4.plot(data1, data2, 'g--') # 기본 차트 : 선 색과 스타일 
# plt.show()

# figure 수준 제목 ★★★
# suptitle() 
fig.suptitle('super title',fontsize=20)


# subplot 수준 제목 ★★★
x1.set_title('hist')
x2.set_title('scatter')
x3.set_title('plot default')
x4.set_title('plot line style')
plt.show()

############################
# 2개 y축 갖는 그래프 
# add_subplot() 로 두 그래프 나타내고
# twinx() 으로 축 하나 더 그려준다.
############################

fig = plt.figure() # 차트 객체 생성
axes = fig.add_subplot() # subplot 객체 생성
axes2 = axes.twinx() # subplot 객체2 생성 (근데 twinx)

x = [1,2,3,4]

y = [2,4,6,8]
y2 = [4,6,1,9]

axes.bar(x, y, color='green', label='bar')
axes2.plot(x, y2, color='red', label='plot', linestyle='--')



# 범례 하나에 넣기
# get_legend_handles_labels() 메소드 
dir(axes)
'''
get_legend_handles_labels()
'''
bars, labels = axes.get_legend_handles_labels()
plots, labels2 = axes2.get_legend_handles_labels()

axes.legend(bars + plots, labels + labels2, loc='upper left')
plt.show()

'''
plt.legend()
axes.legend(loc='upper left')
axes.legend(loc='upper right')
plt.show()
'''