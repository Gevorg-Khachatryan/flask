from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# from models import Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1111@localhost/socnet'
db = SQLAlchemy(app)


