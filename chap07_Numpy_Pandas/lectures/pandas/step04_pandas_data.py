# -*- coding: utf-8 -*-
"""
DataFrame 참조 
.iloc[행][열]
.iloc[행,열]
df명[열]
df명[열][행] # 여기서 행은 인덱스가 아니라 '행의 명칭'을 가져옴 ★★★

    array(배열)에서는 [행,열],[행][열] 이 가능했음
    ※ 물론, 배열에서는 대괄호 안에 숫자만 들어감 
"""

import pandas as pd 


### 1. DF 칼럼(열) 선택 
path = r'C:/ITWILL/3_TextMining/TextMining/data' # 경로 변경 

emp = pd.read_csv(path + "/emp.csv", encoding='utf-8')
print(emp.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   No      5 non-null      int64 
 1   Name    5 non-null      object
 2   Pay     5 non-null      int64
'''

print(emp)
'''
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
'''
# 1) 단일 칼럼 
no = emp.No # 방법1
name = emp['Name'] # 방법2
print(emp['Name'][4]) # >> 김유신


# 2) ★★★ 복수 칼럼 : 중첩 list 
no_pay = emp[['No','Pay']]
print(emp[:,0]) # >> DataFrame에서는 이렇게 하면 안됨 
print(emp.iloc[:,0:2]) # >> 이거는 연속된 칼럼 혹은 행만 가져올 수 있음
print(emp.iloc[1::2][0:2])


### 2. DataFrame 행 선택 

# 1) 정수 색인 : iloc
emp.iloc[0] # 1행 
emp.iloc[:3] # 1~3행

# 2) 명칭 색인 : loc
emp.loc[0] # 1행 
emp.loc[:3] # 1~4행

# 3) 조건식으로 행 선택 
pay350 = emp[emp.Pay > 350] 



### 3. 행열 선택 

# 1) 정수 색인 : iloc 
emp.iloc[0:3, 0:3] # 연속 열 선택 # 0,1,2
emp.iloc[0:3, [0,2]] # 비연속 열 선택  

# 2) 명칭 색인 : loc 
emp.loc[0:3, 'No':'Pay'] # 연속 열 선택 # 0,1,2,3
emp.loc[0:3, ['No','Pay']] # 비연속 열 선택 ★★★

# 1,3,5행, 1,3,5 열 원소만 출력하기 
emp.iloc[0::2,0::2]
emp.iloc[[0,2,4],[0,2]]

emp.loc[[0,2,4],['No','Pay']]
emp.loc[0::2,'No'::2]

'''
    No  Pay
0  101  150
2  103  500
4  105  400
'''