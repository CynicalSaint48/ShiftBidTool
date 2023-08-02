from datetime import datetime
from shiftbidtool import db
from shiftbidtool import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    empID = db.Column(db.String(6), unique=True, nullable=False)
    fName = db.Column(db.String(50), nullable=False)
    lName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phoneNumber = db.Column(db.String(12))
    bidType = db.Column(db.String(50), nullable=False)
    isAdmin = db.Column(db.Integer(), nullable=False, default='0')
    activated = db.Column(db.Integer(), nullable=False, default='0')
    rank = db.Column(db.Integer())

    def __repr__(self):
        return f"User('{self.empID}', '{self.fName}', '{self.lName}', '{self.email}', '{self.activated}')"

class Shift(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    shiftID = db.Column(db.String(50), unique=True, nullable=False)
    w1TS = db.Column(db.DateTime())
    w1TE = db.Column(db.DateTime())
    w1WS = db.Column(db.DateTime())
    w1WE = db.Column(db.DateTime())
    w1ThS = db.Column(db.DateTime())
    w1ThE = db.Column(db.DateTime())
    w1FS = db.Column(db.DateTime())
    w1FE = db.Column(db.DateTime())
    w1SaS = db.Column(db.DateTime())
    w1SaE = db.Column(db.DateTime())
    w1SuS = db.Column(db.DateTime())
    w1SuE = db.Column(db.DateTime())
    w1MS = db.Column(db.DateTime())
    w1ME = db.Column(db.DateTime())
    w2TS = db.Column(db.DateTime())
    w2TE = db.Column(db.DateTime())
    w2WS = db.Column(db.DateTime())
    w2WE = db.Column(db.DateTime())
    w2ThS = db.Column(db.DateTime())
    w2ThE = db.Column(db.DateTime())
    w2FS = db.Column(db.DateTime())
    w2FE = db.Column(db.DateTime())
    w2SaS = db.Column(db.DateTime())
    w2SaE = db.Column(db.DateTime())
    w2SuS = db.Column(db.DateTime())
    w2SuE = db.Column(db.DateTime())
    w2MS = db.Column(db.DateTime())
    w2ME = db.Column(db.DateTime())
    specIndicator = db.Column(db.String(50))
    shiftSup = db.Column(db.String(50))
    shiftAOSF = db.Column(db.String(50))
    truckType = db.Column(db.String(50))
    PrimaryCrew1 = db.Column(db.String(50))
    PrimaryCrew2 = db.Column(db.String(50))
    SecondaryCrew1 = db.Column(db.String(50))
    SecondaryCrew2 = db.Column(db.String(50))
                          