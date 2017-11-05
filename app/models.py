from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class Event(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   date = db.Column(db.Date)
   name = db.Column(db.String(150), unique = True, nullable=False)

   def __repr__(self):
      return self.name

class Donation(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   personname=db.Column(db.String(150), nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   employeeID=db.Column(db.Integer)
   amount=db.Column(db.Float)

   def __repr__(self):
      return self.personname

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True, nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)

   def __repr__(self):
      return self.username

class Contact(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name =  db.Column(db.String(150), unique = True, nullable=False)
   address =  db.Column(db.String(564), default='Street ')
   birthday = db.Column(db.Date)
   personal_phone = db.Column(db.String(20))
   personal_cellphone = db.Column(db.String(20))

   def __repr__(self):
      return self.name