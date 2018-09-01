from flask import Flask, url_for, request

app = Flask(__name__)

#简单的获取URL
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

#REST获取带参数的URL
@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

#使用url_for方法自定义URL
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

#直接获取request对象
@app.route('/getReq')
def getReq():
    return request.method