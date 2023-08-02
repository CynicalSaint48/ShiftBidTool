from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange
from shiftbidtool.models import User, Shift
from shiftbidtool import reservations, supervisors, assistants

def updateShifts():
    shifts = Shift.query.all()
    shiftList = []
    for shift in shifts:
        shiftList.append(shift.shiftID)
    return shiftList

# shifts = Shift.query.all()
# shiftList = []
# for shift in shifts:
#     shiftList.append(shift.shiftID)

systemGroups = ['NET-PCC', 'NET-TL', 'ALS-PCC', 'NCC']


class AddEmployeeForm(FlaskForm):
    
    empID = StringField('Employee ID',
                            validators=[DataRequired(message="Required Field"), Length(min=6, max=6, message="ID should be 6 digits. Include leading zeros")])
    fName = StringField('First Name',
                            validators=[DataRequired(message="Required Field")])
    lName = StringField('Last Name',
                            validators=[DataRequired(message="Required Field")])
    email = StringField('Email',
                         validators=[DataRequired(message="Required Field"), Email(message="Invalid Email")])
    password = StringField('Key Code',
                             validators=[Length(min=18, max=18, message="Field must be exactly 18 characters long.  Please Copy/Paste")])    
    bidType = SelectField('Crew Bid Type', choices=systemGroups,
                          validators=[DataRequired(message="Required Field")])
    isAdmin = BooleanField('Admin Access')
    submit = SubmitField('Save Employee')

    def validate_empID(self, empID):
        user = User.query.filter_by(empID=empID.data).first()
        if user:
            raise ValidationError('Employee ID Already Exists in Database')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(' Email already exists in Database under a different Employee ID.  Check Employee List')

class EditEmployeeForm(FlaskForm):
    
    empID = StringField('Employee ID',
                            validators=[DataRequired(message="Required Field"), Length(min=6, max=6, message="ID should be 6 digits. Include leading zeros")])
    fName = StringField('First Name',
                            validators=[DataRequired(message="Required Field")])
    lName = StringField('Last Name',
                            validators=[DataRequired(message="Required Field")])
    email = StringField('Email',
                         validators=[DataRequired(message="Required Field"), Email(message="Invalid Email")])
    password = StringField('Key Code',
                             validators=[Length(min=18, max=18, message="Field must be exactly 18 characters long.  Please Copy/Paste")])
    bidType = SelectField('Crew Bid Type', choices=systemGroups,
                          validators=[DataRequired(message="Required Field")])
    isAdmin = BooleanField('Admin Access')
    submit = SubmitField('Save Employee')
    delete = SubmitField('Delete Employee Data')

class GetEmployeeForm(FlaskForm):
    
    empID = StringField('Employee ID',
                            validators=[DataRequired(message="Required Field"), Length(min=6, max=6, message="6 digits. Include leading zeros")])   
    submit = SubmitField('Get Employee')

class ActivateEmployeeForm(FlaskForm):
    empID = StringField('Employee ID',
                            validators=[DataRequired(message="Required Field"), Length(min=6, max=6, message="ID should be 6 digits. Include leading zeros")])
    email = StringField('Email',
                         validators=[DataRequired(), Email()])
    fName = StringField('First Name',
                            validators=[DataRequired(message="Required Field")])
    lName = StringField('Last Name',
                            validators=[DataRequired(message="Required Field")])
    phoneNumber = StringField('Contact Number',
                              validators=[DataRequired(), Length(min=10, max=10)])
    confirm_phoneNumber = StringField('Confirm Contact Number',
                                      validators=[DataRequired(), EqualTo('phoneNumber')])
    submit = SubmitField('Save and Log In')

class LoginForm(FlaskForm):
    email = StringField('Email',
                         validators=[DataRequired(), Email()])
    password = StringField('Key Code',
                             validators=[DataRequired(), Length(min=18, max=18)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Save and Log In')

class GetShiftForm(FlaskForm):
    shiftID = SelectField('Shift ID', choices=updateShifts,
                            validators=[DataRequired(message="Required Field")])
    shiftID = SelectField('Shift ID',
                            validators=[DataRequired(message="Required Field")])
    submit = SubmitField('Get Shift')

class AddShiftForm(FlaskForm):
    
    shiftID = StringField('Shift ID',
                            validators=[DataRequired(message="Required Field")])
    specIndicator = SelectField('Reserved for:', choices = reservations, default='Not Reserved')
    
    assistants = ['Assistant 1', 'Assistant 2']
    shiftSup = SelectField('Ops Supervisor', choices=supervisors, 
                            validators=[DataRequired(message="Required Field")])
    shiftAOSF = SelectField('Assistant Supervisor', choices=assistants)
    systemGroups = ['NET', 'BLS 911', 'ALS 911']
    truckType = SelectField('System Group', choices=systemGroups, 
                         validators=[DataRequired(message="Required Field")])
    PrimaryCrew1 = StringField('Primary Crew 1 Employee ID',
                             validators=[Length(max=6, message="Employee ID must be exactly 6 characters long.  Please include leading zeros.")])
    PrimaryCrew2 = StringField('Primary Crew 2 Employee ID',
                             validators=[Length(max=6, message="Employee ID must be exactly 6 characters long.  Please include leading zeros.")])
    SecondaryCrew1 = StringField('Secondary Crew 1 Employee ID',
                             validators=[Length(max=6, message="Employee ID must be exactly 6 characters long.  Please include leading zeros.")])
    SecondaryCrew2 = StringField('Secondary Crew 2 Employee ID',
                             validators=[Length(max=6, message="Employee ID must be exactly 6 characters long.  Please include leading zeros.")])
    submit = SubmitField('Save Shift')

    def validate_empID(self, shiftID):
        shift = Shift.query.filter_by(shiftID=shiftID.data).first()
        if shift:
            raise ValidationError('Shift ID Already Exists in Database')

class EditShiftForm(FlaskForm):
    
    shiftID = StringField('Shift ID',
                            validators=[DataRequired(message="Required Field")])
    reservations = ['AOSF', 'Something Else', 'Not Reserved']
    specIndicator = SelectField('Reserved for:', choices = reservations, default='Not Reserved')
    shiftSup = SelectField('Ops Supervisor', choices=supervisors, 
                            validators=[DataRequired(message="Required Field")])
    shiftAOSF = SelectField('Assistant Supervisor', choices=assistants)
    systemGroups = ['NET', 'BLS 911', 'ALS 911']
    truckType = SelectField('System Group', choices=systemGroups, 
                         validators=[DataRequired(message="Required Field")])
    PrimaryCrew1 = StringField('Primary Crew 1 Employee ID',
                             validators=[Length(max=6, message="Employee ID must be exactly 6 characters long.  Please include leading zeros.")])
    PrimaryCrew2 = StringField('Primary Crew 2 Employee ID',
                             validators=[Length(max=6, message="Employee ID must be exactly 6 characters long.  Please include leading zeros.")])
    SecondaryCrew1 = StringField('Secondary Crew 1 Employee ID',
                             validators=[Length(max=6, message="Employee ID must be exactly 6 characters long.  Please include leading zeros.")])
    SecondaryCrew2 = StringField('Secondary Crew 2 Employee ID',
                             validators=[Length(max=6, message="Employee ID must be exactly 6 characters long.  Please include leading zeros.")])
    submit = SubmitField('Update Shift')