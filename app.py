from flask import Flask,render_template,session,request

import control
import model

 
app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

app.config['SECRET_KEY']= 'RTMS'

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    # session['name'] = 'ralph'
    name = request.form
    print(name)
    return render_template('index.html')

    
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    session['password'] = data['password']
    session['name'] = data['username']
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/signup',methods=['GET','POST'])
def signup():
    
    return render_template("signup.html")

@app.route('/login', methods= ['GET','POST'])
def submit():
    if request.method == "POST":
        details = request.form
        username = details['uname']
        firstname = details['fname']
        surname = details['surname']
        email = details['pemail']
        telephone = details['telephone']
        password = details['pwd']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO PERSONAL(Username,FirstName,Surname,Email,Telephone,Password) VALUES (%s, %s, %s, %s, %s, %s)", (username,firstname,surname,email,telephone,password))
        mysql.connection.commit()
        cur.close()
        return 'success'

    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)

