'''
템플릿 페이지에서 GET과 POST 동시에 전송되는 자료 받기
'''

from flask import Flask, render_template, request # request import

app = Flask(__name__)


@app.route('/') # 시작 페이지
def index() :
    return render_template('/step03/main.html') # 템플릿 파일
   

@app.route('/receive', methods=['GET','POST']) # get, post 방식 
def receive() :    
    if request.method=='POST' : # post 방식 
        name = request.form['uname'] # 파라미터 받기  
        age = request.form['age']
        results = "[post 방식] 사용자 정보 : " + name + ', ' + age         
    if request.method == 'GET':  # get 방식 
        name = request.args.get('uname')
        age = request.args.get('age')
        results = "[GET 방식] 특정사용자 정보: "+ name+','+age
        # 여기서 name, age는 url_for의 name, age
    return render_template('step03/result.html',result= results)
    
if __name__ == '__main__':
    app.run(port=80)







