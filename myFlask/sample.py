# -*- coding: utf-8 -*-
"""
Flask 앱(application) 샘플 

Flask 설치 필요 
 > pip install flask
"""

from flask import Flask 

# 1. 애플리케이션(app) 객체 생성 
app = Flask(__name__)  # 생성자 object 생성 
dir(Flask)

dir(app)
'''
route(url) : 요청 url 받는 메소드 
run(host, port) : 서버 실행 메소드
run(host ='127.0.0.1', port = 5000 )
'''
# 3. 서버 요청 & 응답 
# 함수장식자 @app.route() 사용
# 외부에서 기본 url이 들어오면 응답한다. 
@app.route("/") # 요청할 url 설정("/" 는 기본 url임)
def hello() : # 응답 함수 정의
    return "hello flask" # 브라우저로 응답할 내용  

 
# 프로그램 시작점 
if __name__ == '__main__' :
    #app.run() # 2. 애플리케이션(app) 실행 : 서버 동작  
    app.run(host='127.0.0', port = 5000)
#...  * Running on http://127.0.0.1:5000 ... #서버 시작주소(기본주소)
#★★★ 위 기본 url을 브라우저로 들어가면 hello() 함수 내용을 웹으로 볼 수 있음
# 위 기본 url은 로컬 주소임