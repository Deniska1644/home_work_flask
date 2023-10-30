from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    context = {
        'title': 'основное меню'
    }
    return render_template('main.html',**context)


@app.route('/woman/')
def woman():
    context = {
        'title' : 'Девушкам'
    }
    return render_template('woman.html', **context)


@app.route('/man/')
def man():
    context = {
        'title' : 'Мужчинам'
    }
    return render_template('man.html',**context)


@app.route('/boy/')
def boy():
    context = {
        'title' : 'Мальчикам'
    }
    return render_template('boy.html',**context)


@app.route('/girl/')
def girl():
    context = {
        'title' : 'девочкам'
    }
    return render_template('girl.html',**context)


@app.route('/accessory/')
def accessory():
    context = {
        'title' : 'Аксессуары'
    }
    return render_template('accessory.html',**context)


if __name__ == '__main__':
    app.run()
