from flask import render_template, request, session, redirect, url_for, flash
from mixer.backend.flask import mixer
from app import app
from app.models import *

@app.route('/generate')
def generate():
  events = mixer.cycle(4).blend(Event, name=(n for n in ('Back to School', 'Renovating', 'Race to end Poverty')))
  # TODO: add some code to generate dummy development data and save it to the database
  return "Generated!"

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
  events = Event.query.all()
  donations = Donation.query.filter_by(event_id=event_id)
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
  event = Event.query.filter_by(id=event_id)
  myTemplate = EmailTemplate.query.filter_by(id=template_id).first()
  # TODO: Query for the event with given event_id and for the template and generate email message and values for From, To, CC field
  return render_template("email.html", tTemplate=myTemplate)