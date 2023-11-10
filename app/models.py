
from sqlalchemy import Column, Integer, String
from app import db


class Landlord(db.Model):
    __tablename__ = 'landlorddetails'
    landlordusername = db.Column(String(50), primary_key=True)
    firstName = db.Column(String(50), nullable=False)
    surname = db.Column(String(50), nullable=False)
    email = db.Column(String(30), nullable=False)
    telephone = db.Column(String(20), nullable=False)
    password = db.Column(String(20), nullable=False)



class Personal(db.Model):
    __tablename__ = 'personal'
    username = db.Column(String(20), primary_key=True)
    firstName = db.Column(String(50), nullable=False)
    surname = db.Column(String(50), nullable=False)
    email = db.Column(String(50), nullable=False)
    telephone = db.Column(String(20), nullable=False)
    password = db.Column(String(20), nullable=False)

class Tenant(db.Model):
    __tablename__ = 'tenants'
    username = db.Column(String(20), primary_key=True)
    firstName = db.Column(String(25), nullable=False)
    surname = db.Column(String(25), nullable=False)
    email = db.Column(String(30), nullable=False)
    telephone = db.Column(String(20), nullable=False)
    password = db.Column(String(30), nullable=False)
