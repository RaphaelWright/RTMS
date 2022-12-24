from flask import Flask,render_template,request, session
from flask_mysqldb import MySQL
import yaml
import hashlib
import MySQLdb.cursors
app = Flask(__name__)

db = yaml.full_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['SECRET_KEY']= 'RTMS'


mysql = MySQL(app)

#welcome page
@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM personal WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        personal = cursor.fetchone()

        # If account exists in accounts table in out database
        if personal:
            # Create session data, we can access this data in other routes
            # session['loggedin'] = True
            # session['username'] = personal['username']
            # # Redirect to home page
            return render_template('welcome.html', username = username)
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
            return render_template('index.html', msg = msg)

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
        #hash password
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO personal(username, firstName, surname, email, telephone, password) VALUES(%s,%s,%s,%s,%s,%s)", (username, fname, sname,userEmail,telephone, password))
        mysql.connection.commit()
        cur.close()
        return render_template('welcome.html', username = username)
    return render_template('signup.html')


#welcome page
# @app.route("/timeleft")
# def timeleft():
#     pass

# @app.route("/announcements")
# def announcements():
#     pass


# @app.route("aboutlandlord")
# def aboutlandlord():
#     pass


if __name__ == "__main__":
    app.run(debug=True)

