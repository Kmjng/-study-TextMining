'''
문2) 우리나라 전체 중학교 2학년 여학생의 평균 몸무게는 52kg이고 편차는 5kg로 알려졌다. 
     모집단에서 2,000명의 여학생을 무작으로 추출하여 표본을 생성하고 시각화하시오.
     <조건1> 히스토그램으로 표본 시각화 
     <조건2> 표본의 통계 구하기 : 표본평균, 표본표준편차, 표본표준오차
            표본표준오차(SE) = 표준편차(s) / √ 표본크기(n)  
            
    <시각화 결과> exam02.pdf 참고         
'''

import random # 표본 생성 
import matplotlib.pyplot as plt # 표본 시각화 
import statistics as st # 표본 통계 : 표본평균, 표본표준편차, 표본표준오차 



# 단계1 : 표본 생성 
weight = [random.gauss(mu=52, sigma=5) for i in range(2000)] # 모집단에서 2,000명의 여학생 표본 몸무게 


# 단계2 : 표본 시각화
plt.hist(weight, bins=100)
plt.xlabel('표준편차')
plt.ylabel('몸무게 빈도수')
plt.show()

# 단계3 : 표본 통계 : 표본평균, 표본표준편차, 표본표준오차 
m = st.mean(weight)
s = st.stdev(weight)
se = st.stdev(weight)/st.sqrt(2000)
print(f'평균={m}\n표본표준편차={s}\n표본표준오차={se}')
# 추출된 표본이 모집단을 대표할 정도로 충분히 큰지를 판단하는 데 도움
'''
평균=51.95601483305341
표본표준편차=5.193309541615715
표본표준오차=0.11612593163251012
'''