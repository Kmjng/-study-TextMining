# -*- coding: utf-8 -*-
"""
 matplotlib 환경설정 
  - 한글과 음수 부호 시각화 방법 
"""
import random  
import matplotlib.pyplot as plt 

dir(random)
'''
gauss(mu, sigma) : 정규분포 난수 생성 
randint(a,b) : a~b 사이 랜덤 정수 생성 
random() : 0~1 사이 랜덤 실수 생성 
uniform(a,b) : a~b 랜덤 실수 생성 (균등분포)
seed(정수) : seed값이라고 하며, 동일한 난수 생성
'''
 
# 1. 차트 dataset 생성 
# 표준정규분포 
# 대부분의 값이 -3부터 3 사이에 있을 것으로 기대됨
data = [random.gauss(0,1) for i in range(100)]  # 난수 100개 
len(data)
print(data) # -3 ~ 3
max(data) # 2.4757514607109017
min(data) # -3.1083113764129937

#표준정규분포도 (histogram) ★★★
plt.hist(data, bins=20, density=True, alpha=0.6, color='g')
plt.title('Standard Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 2. 정규분포 시각화 
plt.plot(data)  
plt.title('standard normal distribution random number') 
plt.xlabel('index')
plt.ylabel('random number')
plt.show() 


# 차트에서 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'

# 음수 부호 지원
plt.rcParams['axes.unicode_minus'] = False

# 3. 정규분포 시각화 : 한글 적용  
plt.plot(data)  # 시각화(선 그래프)
plt.title('표준 정규분포 난수') 
plt.xlabel('색인')
plt.ylabel('난수')
plt.show() 

