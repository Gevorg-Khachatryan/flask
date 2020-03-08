from app import db
from datetime import datetime


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    email = db.Column(db.String(60))
    password = db.Column(db.String(30))
    age = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name, surname, email, password, age):
        self.name = name
        self.surname = surname
        self.password = password
        self.email = email
        self.age = age


