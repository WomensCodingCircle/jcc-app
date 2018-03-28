from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config.from_object('config')
Bootstrap(app)
db = SQLAlchemy(app)
admin=Admin(app)
migrate = Migrate(app,db)
login_manager = LoginManager()
ckeditor = CKEditor(app)

from app import views, models