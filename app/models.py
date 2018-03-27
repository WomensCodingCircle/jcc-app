from flask_admin.contrib.sqla import ModelView
from wtforms import TextAreaField
from wtforms.widgets import TextArea
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
   name = db.Column(db.String(150), unique = False, nullable=False)
   sender = db.Column(db.String(200), unique=False, nullable=False)
   recipient = db.Column(db.String(200), unique=False, nullable=False)
   cc = db.Column(db.String(200), unique=False, nullable=True)
   subject = db.Column(db.String(200), unique=False, nullable=True)
   message = db.Column(db.String(10000), unique=False, nullable=True)
   def __repr__(self):
      return self.name

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(120), nullable=False)
   password = db.Column(db.String(255), nullable=False)
   def __repr__(self):
      return self.username

class Eventview(ModelView):
   form_columns = ["date", "name"]

class CKTextAreaWidget(TextArea):
   def __call__(self, field, **kwargs):
      if kwargs.get('class'):
         kwargs['class'] += ' ckeditor'
      else:
         kwargs.setdefault('class', 'ckeditor')
      return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(TextAreaField):
   widget = CKTextAreaWidget()

class TemplateView(ModelView):
   extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']
   form_columns = ["name", "sender", "recipient", "cc", "subject", "message"]
   form_overrides = {
      'message': CKTextAreaField
   }

admin.add_view(ModelView(User, db.session))
admin.add_view(Eventview(Event, db.session))
admin.add_view(ModelView(Donation, db.session))
admin.add_view(ModelView(Initiative, db.session))
admin.add_view(TemplateView(EmailTemplate, db.session))