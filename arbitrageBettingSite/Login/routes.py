from flask import render_template, url_for, flash, redirect, request, Blueprint
from arbitrageBettingSite import app, conn, bcrypt
from arbitrageBettingSite.forms import CustomerLoginForm, EmployeeLoginForm
from flask_login import login_user, current_user, logout_user, login_required

from arbitrageBettingSite import accessType,mysession

Login = Blueprint('Login', __name__)

posts = [{}]

@Login.route("/")
@Login.route("/home")
def home():
    mysession["state"]="home or /"
    print(mysession)
    accessType = mysession["accessType"]
    print("role:" + accessType)
    return render_template('homePage.html',posts=posts,accessType=accessType)

@Login.route("/login", methods=['GET', 'POST'])
def login():

    #202212
    mysession["state"]="login"
    print(mysession)
    role=None    
    
    
@Login.route("/logout")
def logout():
    #202212
    mysession["state"]="logout"
    print(mysession)

    logout_user()
    return redirect(url_for('Login.login'))