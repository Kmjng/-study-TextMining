# -*- coding: utf-8 -*-
"""
- 이산형 변수 시각화 : 막대 그래프, 원 그래프 
"""
import matplotlib.pyplot as plt  

# 차트에서 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'
# 음수 부호 지원 
plt.rcParams['axes.unicode_minus'] = False


# 그래프 자료 생성 
data = [127, 90, 201, 150, 250] # 국가별 수출현황 
year = [2010, 2011, 2012, 2013, 2014] # 년도 


# 1. 세로막대 그래프 
# ★★★ x, height 
plt.bar(x = year, height=data) # 기본색상  
plt.title('국가별 수출현황')
plt.xlabel('년도별')
plt.ylabel('수출현황(단위 : 달러)')
plt.show()


# 2. 가로막대 그래프
# ★★★ y, width
plt.barh(y= year, width = data, color='blue')# 색상적용  
plt.title('국가별 수출현황')
plt.xlabel('수출현황(단위 : 달러)')
plt.ylabel('년도별')
plt.show()


# 3. 누적형 세로막대 그래프
# bar(x데이터, y1데이터, label='데이터셋 1',...)
# bar(x데이터, y2데이터, bottom = y1데이터, label ='데이터셋 2',..)
cate = ['A', 'B', 'C', 'D'] # 집단 
val1 = [15, 8, 12, 10]  # 첫 번째 데이터셋
val2 = [5, 12, 8, 15]  # 두 번째 데이터셋

plt.bar(cate, val1, label='데이터셋1', alpha=0.5)  
plt.bar(cate, val2, bottom=val1, label='데이터셋2', alpha=1)

plt.title('누적형 막대 그래프')
plt.xlabel('카테고리')
plt.ylabel('값')
plt.legend()  # 범례 추가
plt.show()



# 4. 원 그래프
# x = 값(비율로 보여줌), labels = 명목형 변수
labels = ['싱가폴','태국','한국','일본','미국'] 

plt.pie(x = data, labels = labels)
plt.show()

