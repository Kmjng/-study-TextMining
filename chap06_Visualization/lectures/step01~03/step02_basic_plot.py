# -*- coding: utf-8 -*-
"""
 - 기본 그래프 그리기 
"""

import matplotlib.pyplot as plt # data 시각화 


# 차트에서 한글과 음수 부호 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


# 1. 그래프 자료 생성 
data = range(-3, 7) 
print(data) # range(-3, 7) : [-3 -2 -1  0  1  2  3  4  5  6]
len(data) # 10

# 2. 기본 그래프 
# plot()에 인수 하나 들어가면 y축에 해당함
# 이때 x 축은 index 
plt.plot(data) # default => 선색 : 파랑, 스타일 : 실선 
plt.title('선 색 : 파랑, 선 스타일 : 실선 ')
plt.show()  # show()가 있어야 그래프 단위 나눠짐


# 3. 색상 : 빨강, 선스타일(+)
help(plt.plot)

# plot(x데이터, y데이터, 색상및마커)

plt.plot(data, 'r+') # red, +는 plus marker
plt.title('선 색 : 빨강, 선 스타일 : +')
plt.show()


# 4. x,y축 선스타일과 색상 
import random # 난수 생성 

data2 = [random.gauss(0, 1) for i in range(10)]  
plt.plot(data, data2) 
plt.show()

plt.plot(data, data2, 'ro') # red, 산점도
plt.show()
