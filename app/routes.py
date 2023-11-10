from flask import Flask,render_template,request, session,url_for, redirect,flash
from app import app,bcrypt
from app.models import Tenant, Landlord
from app.funcs import *


#welcome page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Go through all the tables and verify 
        user = Landlord.query.filter_by(landlordusername=username).first()
        if not user:
            user = Tenant.query.filter_by(username=username).first()

        if user and user.password:  # Use bcrypt to verify the password
            # User is authenticated
            session['user_id'] = username  # Store the username in the session
            flash('Login successful', 'success')
            return redirect(url_for('dashboard'))  # Redirect to the dashboard or another page
        else:
            flash('Login failed. Please check your username and password.', 'error')

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

@app.route('/twelcome')
def twelcome():

    return render_template("twelcome.html")

@app.route('/lwelcome')
def lwelcome():

    return render_template("lwelcome.html")
