from multiprocessing.pool import ApplyResult
from flask import Flask, render_template


app = Flask(__name__)

#routings
@app.route('/')
def index():
    return render_template("index.html")


