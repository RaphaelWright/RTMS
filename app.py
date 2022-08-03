from multiprocessing.pool import ApplyResult
from turtle import title
from flask import Flask, render_template


app = Flask(__name__)

#routings
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template('about.html', title = title)


@app.route('/contact')
def contact():
    return render_template("contact.html", title = title)


