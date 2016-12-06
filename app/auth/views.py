from flask import render_template,url_for,request,flash,redirect
from flask_login import login_user,logout_user
from . import auth
from ..models import  User
from .forms import LoginForm,RegistrationForm

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username and password')
    return render_template('auth/login.html',form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('you have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/register.html',form=form)