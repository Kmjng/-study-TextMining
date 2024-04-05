'''
템플릿 페이지에서 GET/POST 전송 자료 받기

<<작업순서>>
 1. 시작 페이지 : get방식 전송 or post 방식 전송   
 2. Flask 앱 : get방식 or post방식의 파라미터 받고 & 브라우저에 출력 
'''

from flask import Flask, render_template, request # request : 파라미터 받기 

app = Flask(__name__)


@app.route('/') # 시작 페이지
def index() :
    return render_template('/step03/post_method.html') # 시작 페이지
# => post방식으로 할 경우 
'''
     <form  method="post" action= "/login">
      <table border="1">....</form>
'''
''' 
index() 첫화면에서 render하는 template이 post방식이면 
get방식으로 request하고, method 면 method 방식으로 request 함
'''
@app.route('/login', methods=['GET', 'POST'])    
def login() :    
    if request.method == 'GET' :
        uid = request.args.get('uid')
        return f'get 방식 -> 사용자 아이디 : {uid}'
        
    if request.method=='POST' : # post 방식 
        uid = request.form['uid']
        pwd = request.form['pwd']
        return f'post 방식 <br> 사용자 아이디 : {uid} <br> 사용자 비번 : {pwd}'

if __name__ == '__main__':
    app.run(port=80)

