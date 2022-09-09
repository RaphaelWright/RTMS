import os
import re
import datetime as dtt
from base64 import b64encode
from flask_login import LoginManager, login_required, login_user, UserMixin,current_user, logout_user, fresh_login_required
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    BooleanField,
    ValidationError,
)
from wtforms.validators import DataRequired, EqualTo, Length
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["SECRET_KEY"] = "my secret key that is very difficult for hackers to hack"

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:_*Dordala@2003_@localhost/rtms"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
  return Users.query.get(int(user_id))



class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True,)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telephone = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(200),  nullable=False)
    

    # create a return string
    # def __repr__(self):
    #     return "<Name %r>" % self.username



@app.route('/',methods=["POST","GET"])
def home():
  return render_template('index.html')



    
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template("contact.html")



@app.route('/loggout', methods=['GET', 'POST'])
@login_required
def loggout():
  logout_user()
  flash('You have been logged out')
  return redirect(url_for('login'))

# @fresh_login_required
@app.route('/dashboard',methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("dashboard.html")

    
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == "POST":
    username = request.form.get('username')
    password = request.form.get('password')
    user = Users.query.filter_by(username=username).first()
    if user:  
      if password==user.password:
        login_user(user)
        return redirect(url_for('dashboard'))

      else:
        flash('wrong password')
    else:
      flash('username not found')

  return render_template('index.html')


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
  if request.method == "POST":
    username = request.form.get('username')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('pemail')
    telephone = request.form.get('telephone')
    password = request.form.get('pwd')
    queries = ['username','email','telephone']

    userr = Users.query.filter_by(username=username).first()
    emmail = Users.query.filter_by(email=email).first()
    telee = Users.query.filter_by(telephone=telephone).first()
    print(userr, emmail, telee)

    if userr is None and emmail is None and telee is None:
      user = Users(username=username, first_name=first_name,last_name=last_name,email=email,telephone=telephone,password=password)
      db.session.add(user)
      db.session.commit()
      flash('Loggin Success')
      return redirect(url_for('dashboard'))

    else:

      flash('Username or email or telephone already exists!')
      return render_template('signup.html')
      
  return render_template('signup.html')







# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # Here we use a class of some kind to represent and validate our
#     # client-side form data. For example, WTForms is a library that will
#     # handle this for us, and we use a custom LoginForm to validate.
#     if request.method=="POST":
#         # Login and validate the user.
#         # user should be an instance of your `User` class
#         login_user(user)

#         flask.flash('Logged in successfully.')

#         next = flask.request.args.get('next')
#         # is_safe_url should check if the url is safe for redirects.
#         # See http://flask.pocoo.org/snippets/62/ for an example.
#         if not is_safe_url(next):
#             return abort(400)

#         return redirect(next or url_for('index'))
#     return render_template('login.html')



























if __name__=="__main__":app.run(debug=True)