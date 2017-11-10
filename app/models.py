from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config.from_object('config')
Bootstrap(app)

db = SQLAlchemy(app)

class Event(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   date = db.Column(db.Date)
   name = db.Column(db.String(150), unique = True, nullable=False)
   Donations=db.relationship('Donation', backref='event', lazy='dynamic')

   def __repr__(self):
     return self.name

class Donation(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   personname=db.Column(db.String(150), nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   employeeID=db.Column(db.Integer)
   amount=db.Column(db.Float)
   event_id=db.Column(db.Integer, db.ForeignKey('event.id'))


   def __repr__(self):
     return self.personname

class Eventview(ModelView):
   form_columns = ["id", "date", "name"]

admin=Admin(app)
admin.add_view(Eventview(Event, db.session))
admin.add_view(ModelView(Donation, db.session))


class User(db.Model):
      id=db.Column(db.Integer, primary_key=True)
      username=db.Column(db.String(120), nullable=False)
      password=db.Column(db.String(255), nullable=False)

admin.add_view(ModelView(User, db.session))
