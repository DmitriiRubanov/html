from flask import Flask, url_for, request, render_template

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


@app.route('/index/<title>')
def inde(title):
    if title:
        return render_template('base.html', title=title)
    else:
        return render_template('base.html', title='Заголовок')


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
                  <h1 style="color:rgb(255,0,0)">Жди нас, Марс!</h1>
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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
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
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <center><h1>Анкета претендента</h1></center>
<center><h4>на участие в миссии</h4></center>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
<div>
                                        <label for="form_check"> </label>
                                    <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                                        </div>
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее образование</option>
                                            <option>Бакалавриат</option>
<option>Специалитет</option>
<option>Магистратура</option>
<option>Подготовка кадров высшей квалификации</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form_check">Какие у вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="1" value="1" checked>
                                          <label class="form-check-label" for="1">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="2" value="2">
                                          <label class="form-check-label" for="2">
                                            Пилот
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="3" value="3">
                                          <label class="form-check-label" for="3">
                                            Cтроитель
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="4" value="4">
                                          <label class="form-check-label" for="4">
                                            Экзобиолог
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="5" value="5">
                                          <label class="form-check-label" for="5">
                                            Врач
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="6" value="6">
                                          <label class="form-check-label" for="6">
                                            Инженер по терраформированию
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="7" value="7">
                                          <label class="form-check-label" for="7">
                                            Климатолог
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="8" value="8">
                                          <label class="form-check-label" for="8">
                                            Специалист по радиационной защите
                                          </label>
                                        </div>
</div>
<div class="form-group">
                                        <label for="form_check">Укажите пол</label>
                                        <div class="form-check">
<input class="form-check-input" type="radio" name="sex" id="male" value="male">
                                          <label class="form-check-label" for="male">
                                            Мужчина
                                          </label>
                                        </div>
<div class="form-check">
<input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женщина
                                          </label>
                                        </div>
</div>
<div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
<div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
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
<h1>Результаты отбора</h1>
    <h3>Претендента на участие в миссии {nickname}:</h3>
<div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
</div>
<h3>Составляет {rating}!</h3>
<div class="alert alert-warning" role="alert">
                      Желаем удачи!
</div>
</body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
