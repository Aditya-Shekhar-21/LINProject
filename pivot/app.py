from flask import *
# from flask_sqlalchemy import *
# from flask_wtf.file import URLField
from functools import wraps
from sqlalchemy import *
from views import home,user_profile
from database import db
import os 



app = Flask(__name__)



def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pivot.db'
    db.init_app(app)  
    app.register_blueprint(home.user_homes)
    app.register_blueprint(user_profile.user_profiles)
    return app 


def setup_database(app):
    
    with app.app_context():
        db.create_all()
 

    


if __name__ == '__main__':
    app = create_app()
    if not os.path.isfile('pivot.db'):
        setup_database(app)

    app.run()