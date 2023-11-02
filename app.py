from flask import Flask,render_template,request, session,url_for, redirect,flash
from flask_mysqldb import MySQL
import yaml
import MySQLdb.cursors

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


db = yaml.full_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['SECRET_KEY']= 'rtms@2023'

mysql = MySQL(app)

#welcome page
from flask import render_template, request, flash, redirect, url_for, session
from app import app, db

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()

        # Check if the user is a tenant
        tenant = cur.execute("SELECT * FROM tenants WHERE username = %s", (username,))

        if tenant and tenant['password'] == password:
            # Set user data in session
            session['user_id'] = username  # Assuming 'username' can be used as an identifier
            flash('Login successful!', 'success')
            return redirect(url_for('welcome'))

        # If the user is not a tenant, check if they are a landlord
        landlord = cur.execute("SELECT * FROM landlorddetails WHERE landlordusername = %s", (username,))

        if landlord and landlord['password'] == password:
            # Set user data in session
            session['user_id'] = username  # Assuming 'landlordusername' can be used as an identifier
            flash('Login successful!', 'success')
            return redirect(url_for('welcome'))

        flash('Login unsuccessful. Please check your credentials.', 'danger')

    return render_template('index.html')

    
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/signup', methods=['GET', 'POST'])
def signupp():
    if request.method == 'POST':
        selected_option = request.form.get('client_type')
        if selected_option == "tenant":
            return tenant_signup()
        elif selected_option == "landlord":
            return landlord_signup()

    return render_template("signup.html")

    

#Functions

#function for landlord signup
def landlord_signup():
    if request.method == 'POST':
        #fetch data from form
        landlordDetails = request.form 
        username = landlordDetails['username']
        fname = landlordDetails['first_name']
        sname = landlordDetails['last_name']
        userEmail = landlordDetails['pemail']
        telephone = landlordDetails['telephone']
        password = landlordDetails['pwd']
            #hash password
                
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO landlorddetails(landlordusername, firstName, surname, email, telephone, password) VALUES(%s,%s,%s,%s,%s,%s)", (username, fname, sname,userEmail,telephone, password))
        mysql.connection.commit()
        cur.close()
        return render_template('lwelcome.html', username = username)
    

#function for tenant sign up
def tenant_signup():
    if request.method == 'POST':
        #fetch data from form
        tenantDetails = request.form 
        username = tenantDetails['username']
        fname = tenantDetails['first_name']
        sname = tenantDetails['last_name']
        userEmail = tenantDetails['pemail']
        telephone = tenantDetails['telephone']
        password = tenantDetails['pwd']
        #hash password
                
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tenants(username, firstName, surname, email, telephone, password) VALUES(%s,%s,%s,%s,%s,%s)", (username, fname, sname,userEmail,telephone, password))
        mysql.connection.commit()
        cur.close()

        return render_template('twelcome.html', username = username)
    







