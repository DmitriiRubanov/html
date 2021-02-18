from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def start():
    return "<center><h1>Миссия Колонизация Марса</h1><center>"


@app.route('/index')
def index():
    return "<center><h1>И на Марсе будут яблони цвести!</h1><center>"


@app.route('/promotion')
def promotion():
    return """<center><h1>Человечество вырастает из детства.</h1><center>
    <div>
    <center><h1>Человечеству мала одна планета.</h1><center>
    <div>
    <center><h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1><center>
    <div>
    <center><h1>И начнем с Марса!</h1><center>
    <div>
    <center><h1>Присоединяйся!</h1><center>"""


@app.route('/image_mars')
def image_mars():
    return """<title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    </br>
    <img src="/static/img/mars.jpg">
    </br>
    Вот она какая, красная планета.
    """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
