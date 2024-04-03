# -*- coding: utf-8 -*-
"""
- render_template 함수
    : templates 이용한 url 요청과 응답
    render_template()함수를 통해 제작한 html 파일 내용으로 응답
"""

from flask import Flask, render_template  

# 1. 애플리케이션(app) 생성 
app = Flask(__name__)  


# 3. 서버 요청 & 응답
@app.route("/")  # 요청 받는 역할 
def index() :   # 요청에 따른 응답 (함수 내용 실행)
    return render_template('/step01/index.html')  
            # 해당함수는 /위에 templates라는 폴더를 지칭함 ★
            # 'templates/경로/*.html'

# 3.2. 서버요청2 (info 요청)
# http://127.0.0.1:80/info
# ★요청마다 route를 만들어줘야 함
@app.route("/info")  # 요청 받는 역할 
def info() :
    return render_template('/step01/info.html')
# 프로그램 시작점 
if __name__ == '__main__' :
    app.run(host = '127.0.0.1', port =80) # 2. 애플리케이션(app) 실행
    '''
    host : 서버 url
    port : 서버 포트번호 
    http://127.0.0.1:80
    
    '''  
    