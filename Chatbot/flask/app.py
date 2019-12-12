from datetime import datetime
from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/')
# def hello_world():
#     return '어서와~~ㅎ'

@app.route('/mulcam')
def mulcam():
    return '20층 스카이라운지!'

@app.route('/dday')
def dday():
    today = datetime.now()
    new_year = datetime(2020,1,1)
    result = new_year - today
    return f'<h1>더 성숙해지기까지{result.days}일 남았습니다!</h1>'

# 인사하는 페이지
@app.route('/greeting/<string:name>')
def greeting(name):
    # return f'반갑습니다, {name}님!'
    return render_template('greeting.html',html_name = name)

# 세제곱 결과를 돌려주는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    result = number**3
    # return f'{number}의 세제곱의 값은 {number**3} 입니다.'
    return render_template('cube.html',number=number,result=result)

# 인원 수에 맞게 메뉴를 추천해주는 페이지
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['보쌈수육정식','고추잡채덮밥','돼지불백','샐러드','히레카츠']
    order = random.sample(menu,people)
    return str(order)

# 영화
@app.route('/movie')
def movie():
    movies = ['나이브스 아웃','조커','앤드게임']

    return render_template('movie.html',movies=movies)


@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html',age = age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

# 사용자로부터 입력받을 페이지를 렌더링 해줌.
@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

# 요청을 받은 뒤 데이텅를 가공해서 사용자에게 응답해줌.
@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')
    feature = ['미모','정력','고독함','힘','지식','운','재력']
    feature_list = random.sample(feature,3)
    number1 = random.randrange(1,100)
    number2 = random.randrange(1,100)
    return render_template('godmademe.html',feature_list=feature_list,name=name,number1=number1,number2=number2)


# app.py 가장 하단에 위치
# 1. 앞으로 flask run 으로 서버를 켜는게 아니라,
# pyhon app.py로 서버를 실행한다.
# 2. 내용이 바뀌어도 서버를 껐다 켜지 않아도 된다.
if __name__ == '__main__':
    app.run(debug=True)