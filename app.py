from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import yaml
app = Flask(__name__)

db = yaml.full_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['SECRET_KEY']= 'RTMS'

mysql = MySQL(app)


@app.route('/' methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        username = 

    return render_template('index.html')

    
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #fetch data from form
        userDetails = request.form 
        username = userDetails['username']
        fname = userDetails['first_name']
        sname = userDetails['last_name']
        userEmail = userDetails['pemail']
        telephone = userDetails['telephone']
        password = userDetails['pwd']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO personal(Username, FirstName, Surname, Email, Telephone, Password) VALUES(%s,%s,%s,%s,%s,%s)", (username, fname, sname,userEmail,telephone, password))
        mysql.connection.commit()
        cur.close()
        return render_template('login.html', fname = fname)
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)

