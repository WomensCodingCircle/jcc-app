from flask import Flask, render_template, request, session, redirect, url_for, flash
from mixer.backend.flask import mixer
from app.models import User
from .models import app


@app.route('/')
def landing_page():
   return render_template('landing_page.html', tEvents=events)

from app.models import Event

with app.app_context():
   events = mixer.cycle(4).blend(Event, name=(n for n in ('Back to School', 'Renovating', 'Race to end Poverty')))



@app.route('/register/', methods=["GET", "POST"])
def register():
   if request.method=='POST':
      username=request.form['username']
      password=request.form['password']
      session['username']=username
      flash('Logged in ')
      return redirect(url_for('landing_page'))
   return render_template('register.html')

@app.route('/login/', methods=["GET", "POST"])
def login():
   if request.method=="POST":
      username = request.form['username']
      password = request.form['password']
      user=User.query.filter_by(username=username).first()
      if user.username==username:
         return user.password
   return render_template("login.html")





