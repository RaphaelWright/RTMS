from flask import Flask,render_template,request, session,url_for, redirect,flash
from app import app, db
from app.models import Tenant, Landlord



def landlord_signup():
    if request.method == 'POST':
        landlordDetails = request.form
        username = landlordDetails['username']
        fname = landlordDetails['first_name']
        sname = landlordDetails['last_name']
        userEmail = landlordDetails['pemail']
        telephone = landlordDetails['telephone']
        password = landlordDetails['pwd']

        new_landlord = Landlord(landlordusername=username, firstName=fname, surname=sname, email=userEmail, telephone=telephone, password=password)
        db.session.add(new_landlord)
        db.session.commit()

        return render_template('lwelcome.html', username=username)
    
def tenant_signup():
    if request.method == 'POST':
        tenantDetails = request.form
        username = tenantDetails['username']
        fname = tenantDetails['first_name']
        sname = tenantDetails['last_name']
        userEmail = tenantDetails['pemail']
        telephone = tenantDetails['telephone']
        password = tenantDetails['pwd']

        new_tenant = Tenant(username=username, firstName=fname, surname=sname, email=userEmail, telephone=telephone, password=password)
        db.session.add(new_tenant)
        db.session.commit()

        return render_template('twelcome.html', username=username)
    