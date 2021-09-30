from flask import *

user_profiles = Blueprint('user_profile', __name__,)






@user_profiles.route('/login/')
def login():
    return render_template('login.html')


@user_profiles.route('/settlment_pkg/')
def settlment_pkg():
    return render_template('settlment_pkg.html')


@user_profiles.route('/output/')
def output():
    
    return "<h>Your Record successfully stored!</h>"