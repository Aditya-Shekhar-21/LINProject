from database import db
from datetime import datetime 



class User(db.Model):
    req_id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False, default = datetime.now() )
    username = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

