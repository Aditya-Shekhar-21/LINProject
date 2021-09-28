from flask import *
from flask_sqlalchemy import *
# from flask_wtf.file import URLField
from datetime import datetime 
from functools import wraps
from sqlalchemy import *




app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqldb.db'
db = SQLAlchemy(app)




class User(db.Model):
    req_id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False, default = datetime.now() )
    username = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# data1 = User(req_id=14,username="SCHIKOTI",status="complete")
# data2 = User(req_id=13,username="SBOBBA",status="complete")
# data3 = User(req_id=12,username="PNIBRAD",status="in progress")



# db.session.add_all([data3])

# db.session.commit()



def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # return f(*args, **kwargs)
        
        # flash("You need to login first")
        return redirect(url_for('login'))

    return wrap


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/home/',methods=['GET','POST'])
# @login_required
def home():
   print(request.form['username'])
   data1 = User(req_id=request.form['req_id'],username=request.form['username'],status=request.form['status'])
   db.session.add_all([data1])
   db.session.commit()
   data =  User.query.order_by(User.req_id.desc(), User.req_id.desc()).all()
   return render_template('index.html',data=data)



@app.route('/register/',methods=['GET', 'POST'])
def register():
    return render_template('register.html')




@app.route('/output/')
def output():
    
    return "<h>Your Record successfully stored!</h>"

if __name__ == '__main__':
    app.run()