from flask import render_template, request, session, redirect, url_for, flash
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


