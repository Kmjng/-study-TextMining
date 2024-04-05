# -*- coding: utf-8 -*-
"""
step03 관련 문제 

문2) 사원목록에서 '사원명'을 클릭하면 해당 부서 정보가 출력되도록 하시오. 

   조건1> 템플릿(templates) 파일 작성 위치 : templates\exam03 폴더
   조건2> 사원목록을 나타내는 페이지 : emp_list.html
   조건3> 부서 정보가 출력되는 페이지 : dept_info.html 
   조건4> 전송 방식 : get 방식 
   조건5> 부서 정보(부서번호, 부서명, 부서위치) 
          10, '기획실', '서울시'   
          20, '연구실', '대전시'
          30, '영업부', '싱카폴'
        
   
   기타 : 출력결과는 강의자료에서 확인     
"""


from flask import Flask, render_template, request  


app = Flask(__name__)


@app.route('/') # 시작 페이지
def input() :
    return render_template('/exam03/emp_list.html') # 사원목록 


@app.route('/deptInfo', methods=['GET']) # get 방식 : 부서번호 받기  
def info(dno) : #deptInfo에 dno 로 들어감 
    dno =request.args.get('dno')    # dno를 시작페이지에서 받고
    dno = int(dno) # 파라미터로 받은 dno가 string이라 바꿔줘야함
    if dno ==30:
        dname ='영업부'
        loc ='싱가폴'
    elif dno ==10:
        dname ='기획부'
        loc ='서울'
    elif dno == 20:
        dname = '연구실'
        loc = '대전시'
    return render_template('/exam03/dept_info.html',dno = dno, dname=dname, loc=loc ) # 부서정보  

if __name__ == '__main__':
    app.run(port=80)
    
