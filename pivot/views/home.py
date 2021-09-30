from models.user import User
from flask import *
from database import db
from flask_login import login_required,current_user,LoginManager

user_homes = Blueprint('user_home', __name__,)

login_manager = LoginManager()

# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         # return f(*args, **kwargs)
        
#         # flash("You need to login first")
#         return redirect(url_for('login'))

#     return wrap



@user_homes.route('/home/',methods=['GET','POST'])
# @login_required
def home():
    # data = [{
    #     "status":"complete",

    # }]
    # data1 = User(username=request.form['username'],status=request.form['status'])
    # db.session.add_all([data1])
    # db.session.commit()
    data =  User.query.order_by(User.req_id.desc(), User.req_id.desc()).all()
#    print(data)
    return render_template('index.html',data=data)



# @user_homes.route('/register/',methods=['GET', 'POST'])
# def register():
#     return render_template('register.html')
    