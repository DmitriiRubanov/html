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


@app.route('/promotion_image')
def promotiom_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                  <h1>Жди нас, Марс!</h1>
</br>
    <img src="/static/img/mars.jpg">
    </br>
                    <div class="alert alert-secondary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
