import os
from app import app

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'rtms2023'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/rtms'