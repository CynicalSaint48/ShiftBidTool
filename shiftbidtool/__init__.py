from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd45f9983da1d12a9f2111f24e2fe9a35'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_message_category ='info'

reservations = ['blahblah', 'Not Reserved']
supervisors = ['Andrew Smith', 'Brian Smith', 'Chris Simmons', 'Dan Baltimore', 'Don Shue', 'Gabe McGaha', 'John Crunk', 'John Stroup', 'Jose Gonzalez', 'Joshua Baun', 'Kenny Phillips', 'Siobhan Klass']
assistants = ['', 'AOSF1', 'AOSF2']


from shiftbidtool import routes