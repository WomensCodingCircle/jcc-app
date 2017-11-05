from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from mixer.backend.flask import mixer


app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config.from_object('config')
Bootstrap(app)

@app.route('/')
def landing_page():
   return render_template('landing_page.html', tEvents=events, tPeople=people)

from app.models import Event, Contact

with app.app_context():
   events = mixer.cycle(4).blend(Event, name=(n for n in ('Back to School', 'Renovating', 'Race to end Poverty', 'Holiday Food Drive')))
   people = mixer.cycle(4).blend(Contact,
                                    name=(n for n in ('Alice', 'Bob', 'Claudine', 'Dan')),
                                    employeeId=(n for n in ('12345', '67891', '45678', '12356')),
                                    email=(n for n in ('alice@email.com', 'bob@email.com', 'claudine@email.com', 'dan@email.com'))
                                 )