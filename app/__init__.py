from flask import render_template, request, session, redirect, url_for, flash
from mixer.backend.flask import mixer
from app.models import User
from .models import app

@app.route('/')
def landing_page():
   return render_template('landing_page.html', tEvents=events, tPeople='', tDonations=donations)

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/event/<event_id>')
def show_donations(event_id):
   print(event_id)
   return render_template('landing_page.html')

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

with app.app_context():
   events = mixer.cycle(4).blend(Event,
                                    id=(n for n in (1,2,3,4)),
                                    name=(n for n in ('Back to School', 'Renovating', 'Race to end Poverty', 'Holiday Food Drive'))
                                 )
#    people = mixer.cycle(4).blend(Contact,
#                                     name=(n for n in ('Alice', 'Bob', 'Claudine', 'Dan')),
#                                     employeeId=(n for n in ('12345', '67891', '45678', '12356')),
#                                     email=(n for n in ('alice@email.com', 'bob@email.com', 'claudine@email.com', 'dan@email.com'))
#                                  )

   donations = mixer.cycle(2).blend(Donation,
                                       id=(n for n in (1,2,3,4)),
                                       personname=(n for n in ('Alice','Bob')),
                                       employeeId=(n for n in ('12345', '67891')),
                                       email=(n for n in ('alice@email.com', 'bob@email.com')),
                                       amount=(n for n in (30, 40)),
                                       event_id=(n for n in (3, 4))
                                    )