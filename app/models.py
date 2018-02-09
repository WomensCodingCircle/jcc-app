from flask_admin.contrib.sqla import ModelView
from app import db, admin

class Initiative(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(150), unique = False, nullable = False)
   events = db.relationship('Event', backref='initiative', lazy = True)
   def __repr__(self):
      return self.name

class Event(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   date = db.Column(db.Date)
   name = db.Column(db.String(150), unique = True, nullable=False)
   donations = db.relationship('Donation', backref='event', lazy=True)
   initiative_id = db.Column(db.Integer, db.ForeignKey('initiative.id'),
                              nullable=True)
   def __repr__(self):
      return self.name

class Donation(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   personname=db.Column(db.String(150), nullable=False)
   email = db.Column(db.String(120), unique=False, nullable=False)
   employeeID=db.Column(db.Integer)
   amount=db.Column(db.Float)
   event_id = db.Column(db.Integer, db.ForeignKey('event.id'),
                         nullable=False)
   def __repr__(self):
      return self.personname

class EmailTemplate(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   sender = db.Column(db.String(200), unique=False, nullable=False)
   recipient = db.Column(db.String(200), unique=False, nullable=False)
   cc = db.Column(db.String(200), unique=False, nullable=False)
   subject = db.Column(db.String(200), unique=False, nullable=False)
   message = db.Column(db.String(10000), unique=False, nullable=False)

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(120), nullable=False)
   password = db.Column(db.String(255), nullable=False)
   def __repr__(self):
      return self.username

class Eventview(ModelView):
   form_columns = ["date", "name"]

admin.add_view(ModelView(User, db.session))
admin.add_view(Eventview(Event, db.session))
admin.add_view(ModelView(Donation, db.session))
admin.add_view(ModelView(Initiative, db.session))
admin.add_view(ModelView(EmailTemplate, db.session))