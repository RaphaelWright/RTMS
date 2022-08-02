from multiprocessing.pool import ApplyResult
from turtle import title
from flask import Flask, render_template


app = Flask(__name__)

#routings
@app.route('/')
def index():
    title = "RTMS - Manage Tenants"
    return render_template("index.html", title = title)


@app.route('/about')
def about():
    title = "About RTMS"
    return render_template('about.html', title = title)


@app.route('/contact')
def contact():
    title = " RTMS - Contact"
    return render_template("contact.html", title = title)


