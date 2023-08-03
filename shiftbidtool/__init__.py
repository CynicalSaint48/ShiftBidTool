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

reservations = ['AOSF', 'Paramedic Student', 'Not Reserved']
supervisors = ['Andrew Smith', 'Brian Smith', 'Chris Simmons', 'Dan Baltimore', 'Don Shue', 'Gabe McGaha', 'John Crunk', 'John Stroup', 'Jose Gonzalez', 'Joshua Baun', 'Kenny Phillips', 'Siobhan Klass', 'Anthony Carriker', 'Matthew Lewis', 'Brandis Ridenhour', 'Luis Barrera',
               'Anna Elliott', 'Andy Williams', 'Nic Pirone', 'Allison Kerley', 'RJ Goodman', 'Jackson Langevoort', 'Ashley Romero-Depalma', 'Shane Anaya', 'James Camarena', 'Bobby Harford', 'Kelly McCarthy', 'Jeremy Murphy', 'Chris Jerrell', 'Mike Stratton', 'Lizz Kurc', 'Joshua Baun', 'Daniel Geis']
assistants = ['Anna Elliott', 'Andy Williams', 'Nic Pirone', 'Allison Kerley', 'RJ Goodman', 'Jackson Langevoort', 'Ashley Romero-Depalma', 'Shane Anaya', 'James Camarena', 'Bobby Harford', 'Kelly McCarthy', 'Jeremy Murphy', 'Chris Jerrell', 'Mike Stratton', 'Lizz Kurc', 'Joshua Baun', 'Daniel Geis']
systemGroups = ['ALS 911', 'BLS 911', 'NET']
bidTypes = ['NET-PCC', 'NET-TL', 'ALS-PCC', 'NCC']

from shiftbidtool import routes