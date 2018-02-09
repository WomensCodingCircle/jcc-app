from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config.from_object('config')
Bootstrap(app)
db = SQLAlchemy(app)
admin=Admin(app)
migrate = Migrate(app,db)
login_manager = LoginManager()

from app.models import User, Event, Donation

@app.route('/')
def landing_page():
   events = Event.query.all()
   first = Event.query.first()
   donations = []
   event_id = None
   if (first):
      event_id = first.id
      donations = Donation.query.filter_by(event_id=event_id)
   return render_template('landing_page.html', tEvents=events, tPeople='', tDonations=donations, tEvent_id=event_id)

@app.route('/event/<event_id>')
def show_donations(event_id):
   print(event_id)
   events = Event.query.all()
   donations = Donation.query.filter_by(event_id=event_id)
   print(donations)
   return render_template('landing_page.html', tEvents=events, tDonations=donations, tEvent_id=int(event_id))

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/register/', methods=["GET", "POST"])
def register():
   if request.method=='POST':
      username=request.form['username']
      password=request.form['password']
      session['username']=username
      flash('Logged i as username ')
      flash('seccuessssss')
      return redirect(url_for('login'))
   return render_template('register.html')

@app.route('/login/', methods=["GET", "POST"])
def login():
   if request.method=="POST":
      username = request.form['username']
      password = request.form['password']
      user=User.query.filter_by(username=username).first()
      flash('Logged in ')
      try:
         if user.username==username:
            return redirect(url_for("admin.index"))
      except Exception:
         pass
   return render_template("login.html")

@app.route('/logout/')
def logout():
   session.pop('username', None)
   # flash("logged out")
   return render_template("logout.html")

@app.route('/mail/')
def generate_email_default():
   return render_template("email.html", tTitle = 'Sample email template')

@app.route('/mail/event/<event_id>/template/<template_id>')
def generate_email(event_id, template_id):
   # TODO: Query for the event with given event_id and for the template and generate email message and values for From, To, CC field
   event = Event.query.filter_by(id=event_id)
   if template_id == '1':
         title = "Email to Donators"
   else:
         title = "Email to Finance"
   return render_template("email.html", tTitle = title)