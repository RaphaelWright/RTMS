from flask_mysqldb import MySQL
from flask import *
import MySQLdb.cursors
from app import app

def signup():

    mysql = MySQL(model)

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
        cur.execute("INSERT INTO landlorddetails(username, firstName, surname, email, telephone, password) VALUES(%s,%s,%s,%s,%s,%s)", (username, fname, sname,userEmail,telephone, password))
        mysql.connection.commit()
        cur.close()
         return render_template('welcome.html', username = username)
    return render_template('signup.html')
    