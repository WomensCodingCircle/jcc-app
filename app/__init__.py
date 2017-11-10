from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from mixer.backend.flask import mixer


app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config.from_object('config')
Bootstrap(app)

@app.route('/')
def landing_page():
   return render_template('landing_page.html', tEvents=events, tPeople=people, tDonations=donations)

@app.route('/about')
def about():
   text = 'This application has been build by the womens coding circle at Janelia'
   return render_template('about.html')

@app.route('/event/<event_id>')
def show_donations(event_id):
   print(event_id)
   return render_template('landing_page.html')

from app.models import Event, Contact, Donation

with app.app_context():
   events = mixer.cycle(4).blend(Event,
                                    id=(n for n in (1,2,3,4)),
                                    name=(n for n in ('Back to School', 'Renovating', 'Race to end Poverty', 'Holiday Food Drive'))
                                 )
   people = mixer.cycle(4).blend(Contact,
                                    name=(n for n in ('Alice', 'Bob', 'Claudine', 'Dan')),
                                    employeeId=(n for n in ('12345', '67891', '45678', '12356')),
                                    email=(n for n in ('alice@email.com', 'bob@email.com', 'claudine@email.com', 'dan@email.com'))
                                 )

   donations = mixer.cycle(2).blend(Donation,
                                    id=(n for n in (1,2,3,4)),
                                    personname=(n for n in ('Alice','Bob')),
                                    employeeId=(n for n in ('12345', '67891')),
                                    email=(n for n in ('alice@email.com', 'bob@email.com')),
                                    amount=(n for n in (30, 40)),
                                    event_id=(n for n in (3, 4))
                                 )