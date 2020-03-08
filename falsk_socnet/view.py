from flask import  request, render_template, redirect
from app import app
from app import db
from models import Users


@app.route('/')
def loginpage():
    return render_template('signin.html', message='')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        us = db.session.query(Users).filter_by(name=request.form['name'], password=request.form['password']).all()
        if len(us) == 0:
            user = Users(request.form['name'],
                         request.form['surname'],
                         request.form['email'],
                         request.form['password'],
                         request.form['age'])
            db.session.add(user)
            db.session.commit()
            return render_template('signin.html', message='You are registrated')
        return render_template('signin.html', message='wrong password or email')
    return redirect('/')


@app.route('/login', methods=['POST', 'GET'])
def login():
    us = db.session.query(Users).filter_by(name=request.form['name'], password=request.form['password']).all()
    if len(us) == 0:
        return render_template('signin.html', message='wrong password or name')
    elif len(us) == 1:
        return render_template('homepage.html', name=us[0].name, surname=us[0].surname)

    return 'you are registrated'

