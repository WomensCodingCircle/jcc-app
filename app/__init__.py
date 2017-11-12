from flask import render_template, request, session, redirect, url_for, flash
from mixer.backend.flask import mixer
from app.models import User
from .models import app

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

from app.models import Event, Donation