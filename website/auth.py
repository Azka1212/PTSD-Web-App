from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

# Define routes to html pages
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/doctor')
def doctor():
    return render_template("doctor.html")

@auth.route('/admin_actions')
def admin_actions():
    return render_template("admin_actions.html")

@auth.route('/add_doctor')
def add_doctor():
    return render_template("add_doctor.html")

@auth.route('/add_admin')
def add_admin():
    return render_template("add_admin.html")

@auth.route('/add_receptionist')
def add_receptionist():
    return render_template("add_receptionist.html")

@auth.route('/receptionist_actions')
def receptionist_actions():
    return render_template("receptionist_actions.html")

@auth.route('/register_patient')
def register_patient():
    return render_template("register_patient.html")

@auth.route('/patient_list')
def patient_list():
    return render_template("patient_list.html")

@auth.route('/view_appointments')
def view_appointments():
    return render_template("view_appointments.html")

@auth.route('/doctor_actions')
def doctor_actions():
    return render_template("doctor_actions.html")

@auth.route('/fill_questionnare')
def fill_questionnare():
    return render_template("fill_questionnare.html")

@auth.route('/receptionist')
def receptionist():
    return render_template("receptionist.html")

@auth.route('/patient')
def patient():
    return render_template("patient.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash('Account created!', category='success')

            return redirect(url_for('views.home'))

    return render_template("sign_up.html")