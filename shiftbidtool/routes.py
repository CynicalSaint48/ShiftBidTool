from flask import render_template, url_for, flash, redirect, session
from shiftbidtool import app, db, bcrypt
from shiftbidtool.forms import AddEmployeeForm, GetEmployeeForm, ActivateEmployeeForm, LoginForm, EditEmployeeForm, GetShiftForm, AddShiftForm, EditShiftForm, updateShifts
from shiftbidtool.models import User, Shift
from flask_login import login_user, current_user, logout_user

updateShifts

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/live/admin")
def liveAdmin():
    return render_template('live_admin.html', title='Live Admin')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            session["empID"] = user.empID
            if user.phoneNumber == None:
                flash(f"You don't have a contact phone number yet!  Please update to continue.", 'danger')
                return redirect(url_for('activate'))
            else:
                print(user.phoneNumber)
                flash(f'You have been logged in!', 'success') 
                return redirect(url_for('home'))
        else:
            flash(f'Your email or key code are incorrect.  Please try again.', 'danger') 
            return render_template('login.html', title='Log In', form=form)
    return render_template('login.html', title='Log In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/activation", methods=['GET', 'POST'])
def activate():
    empID = session.get("empID")
    user = User.query.filter_by(empID=empID).first()

    form = ActivateEmployeeForm(empID=empID, email=user.email, fName=user.fName, lName=user.lName)

    if form.validate_on_submit():
        user = User.query.filter_by(empID=empID).first()
        user.phoneNumber = form.phoneNumber.data
        user.activated = '1'
        db.session.commit()
        flash(f'Thank you, you are logged in!', 'success')
        return redirect(url_for('home'))

    return render_template('activation.html', title='Activate Account', form=form)

@app.route("/employee_list")
def employees():
    users = User.query.all()
    return render_template('employees.html', title='Employee List', users=users)

@app.route("/get_employee", methods=['GET', 'POST'])
def getEmployee():
    form = GetEmployeeForm()
    if form.validate_on_submit():
        user = User.query.filter_by(empID=form.empID.data).first()
        if user:
            session["empID"] = user.empID
            session["fName"] = user.fName
            session["lName"] = user.lName
            session["email"] = user.email
            session["password"] = user.password
            session["bidType"] = user.bidType
            session["isAdmin"] = user.isAdmin
            flash(f'Employee {form.empID.data} Found', 'success')
            return redirect(url_for('editEmployee'))
        else:
            session["empID"] = form.empID.data
            flash(f'Employee not {form.empID.data} Found.  Please add them here.', 'danger')
            return redirect(url_for('addEmployee'))
    return render_template('getemployee.html', title='Get Employee', form=form)

@app.route("/add_employee", methods=['GET', 'POST'])
def addEmployee():
    empID = session.get("empID")

    form = AddEmployeeForm(empID=empID)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(empID=form.empID.data, email=form.email.data, password=hashed_password, fName=form.fName.data, lName=form.lName.data, bidType=form.bidType.data, isAdmin=form.isAdmin.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Employee {form.empID.data} Added to Database', 'success')
        return redirect(url_for('home'))

    return render_template('addemployee.html', title='Add Employee', form=form, empID=empID)

@app.route("/edit_employee", methods=['GET', 'POST'])
def editEmployee():
    empID = session.get("empID")
    fName = session.get("fName")
    lName = session.get("lName")
    email = session.get("email")
    bidType = session.get("bidType")
    isAdmin = session.get("isAdmin")

    form = EditEmployeeForm(empID=empID, fName=fName, lName=lName, email=email, bidType=bidType, isAdmin=isAdmin)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User.query.filter_by(empID=form.empID.data).first()
        user.empID = form.empID.data
        user.fName = form.fName.data
        user.lName = form.lName.data
        user.email = form.email.data
        user.bidType = form.bidType.data
        user.isAdmin = form.isAdmin.data
        user.password = hashed_password
        db.session.commit()
        print(user)
        flash(f'Employee {form.empID.data} Edited', 'success')
        return redirect(url_for('home'))
    return render_template('editemployee.html', title='Edit Employee', form=form)

@app.route("/get_shift", methods=['GET', 'POST'])
def getShift():
    shiftList = updateShifts()
    form = GetShiftForm()
    form.shiftID.choices = shiftList
    if form.validate_on_submit():
        shift = Shift.query.filter_by(shiftID=form.shiftID.data).first()
        if shift:
            session["shiftID"] = shift.shiftID
            flash(f'Shift {form.shiftID.data} Found', 'success')
            return redirect(url_for('editShift'))
        else:
            flash(f'Shift {form.shiftID.data} not Found.  Please add it here.', 'danger')
            return redirect(url_for('addShift'))
    return render_template('getshift.html', title='Get Shift', form=form)

@app.route("/add_shift", methods=['GET', 'POST'])
def addShift():
    form = AddShiftForm()
    if form.validate_on_submit():
        shift = Shift(shiftID=form.shiftID.data, specIndicator=form.specIndicator.data, shiftSup=form.shiftSup.data, shiftAOSF=form.shiftAOSF.data, truckType=form.truckType.data, PrimaryCrew1=form.PrimaryCrew1.data, PrimaryCrew2=form.PrimaryCrew2.data, SecondaryCrew1=form.SecondaryCrew1.data, SecondaryCrew2=form.SecondaryCrew2.data)
        db.session.add(shift)
        db.session.commit()
        print("HERE WE ARE")
        shiftList = updateShifts()
        print(shiftList)
        flash(f'Shift {form.shiftID.data} Added to Database', 'success')
        return redirect(url_for('home'))

    return render_template('addshift.html', title='Add Shift', form=form)

@app.route("/edit_shift", methods=['GET', 'POST'])
def editShift():
    shiftID = session.get("shiftID")
    shift = Shift.query.filter_by(shiftID=shiftID).first()
    specIndicator = shift.specIndicator
    shiftSup = shift.shiftSup
    shiftAOSF = shift.shiftAOSF
    truckType = shift.truckType
    PrimaryCrew1 = shift.PrimaryCrew1
    PrimaryCrew2 = shift.PrimaryCrew2
    SecondaryCrew1 = shift.SecondaryCrew1
    SecondaryCrew2 = shift.SecondaryCrew2
    form = EditShiftForm(shiftID=shiftID, specIndicator=specIndicator, shiftSup=shiftSup, shiftAOSF=shiftAOSF, truckType=truckType, PrimaryCrew1=PrimaryCrew1, PrimaryCrew2=PrimaryCrew2, SecondaryCrew1=SecondaryCrew1, SecondaryCrew2=SecondaryCrew2)  
    
    if form.validate_on_submit():
        shift = Shift.query.filter_by(shiftID=form.shiftID.data).first()
        shift.specIndicator = form.specIndicator.data
        shift.shiftSup = form.shiftSup.data
        shift.shiftAOSF = form.shiftAOSF.data
        shift.truckType = form.truckType.data
        shift.PrimaryCrew1 = form.PrimaryCrew1.data
        shift.PrimaryCrew2 = form.PrimaryCrew2.data
        shift.SecondaryCrew1 = form.SecondaryCrew1.data
        shift.SecondaryCrew2 = form.SecondaryCrew2.data
        db.session.commit()
        flash(f'Shift {form.shiftID.data} Updated', 'success')
        return redirect(url_for('home'))

    return render_template('editshift.html', title='Add Shift', form=form)

@app.route("/temp/singleview")
def singleView():
    shiftID = "B13"
    w1TS = ""
    w1TE = ""
    w1WS = "08:30"
    w1WE = "22:00"
    w1ThS = "08:30"
    w1ThE = "21:30"
    w1FS = ""
    w1FE = ""
    w1SaS = ""
    w1SaE = ""
    w1SuS = ""
    w1SuE = ""
    w1MS = "08:30"
    w1ME = "22:00"
    w2TS = "08:30"
    w2TE = "18:30"
    w2WS = ""
    w2WE = ""
    w2ThS = ""
    w2ThE = ""
    w2FS = "08:30"
    w2FE = "18:30"
    w2SaS = "08:30"
    w2SaE = "18:30"
    w2SuS = "08:30"
    w2SuE = "18:30"
    w2MS = ""
    w2ME = ""
    shiftSup = "Kenny Phillips"
    shiftAOSF = "Ashley Romero de Palma"
    truckType = "BLS-911"
    PrimaryCrew1 = ""
    SecondaryCrew1 = "Ricky Rescue"
    thisShift = Shift(shiftID=shiftID, w1TS=w1TS, w1TE=w1TE, w1WS=w1WS, w1WE=w1WE, w1ThS=w1ThS, w1ThE=w1ThE,
                      w1FS=w1FS, w1FE=w1FE, w1SaS=w1SaS, w1SaE=w1SaE, w1SuS=w1SuS, w1SuE=w1SuE, w1MS=w1MS, w1ME=w1ME,
                      w2TS=w2TS, w2TE=w2TE, w2WS=w2WS, w2WE=w2WE, w2ThS=w2ThS, w2ThE=w2ThE, w2FS=w2FS, w2FE=w2FE, 
                      w2SaS=w2SaS, w2SaE=w2SaE, w2SuS=w2SuS, w2SuE=w2SuE, w2MS=w2MS, w2ME=w2ME,
                      shiftSup=shiftSup, shiftAOSF=shiftAOSF, PrimaryCrew1=PrimaryCrew1, SecondaryCrew1=SecondaryCrew1, truckType=truckType)
    return render_template('singleshift.html', title='Single Shift', thisShift=thisShift)