'''
문4) bmi.csv 파일의 자료를 이용하여 각 단계별로 통계 분석을 수행하시오.
'''

import pandas as pd 


# 1. DF 칼럼 선택 : 칼럼 선택 목적 
path = r'C:/ITWILL/3_TextMining/TextMining/data' # 경로 변경 

bmi = pd.read_csv(path + "/bmi.csv", encoding='utf-8')
print(bmi.info())

bmi.shape # >> (20000, 3)
print(bmi)
# 단계1 : height와 weight 요약통계
desc = bmi.describe()
print(desc)
# 단계2 : height와 weight 표준편차 
bmi[['height','weight']].std() # default가 칼럼내에서 계산
'''
height    14.677064
weight    13.250776
dtype: float64
'''
# 단계3 : height와 weight 상관계수 
bmi[['height','weight']].corr()
'''
          height    weight
height  1.000000  0.009072
weight  0.009072  1.000000
'''
# 상관계수 상수 
bmi['height'].corr(bmi.weight)
# >> 0.009072004787653649

# 단계4 : label 빈도수 
bmi['label'].value_counts()
'''
label
normal    7677
fat       7425
thin      4898
Name: count, dtype: int64
'''