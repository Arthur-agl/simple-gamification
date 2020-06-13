from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from simple_gamification import db, login_manager

class User(db.Model, UserMixin):
    id                  = db.Column(db.Integer(),   primary_key=True)
    email               = db.Column(db.String(100), nullable=False, unique=True,)
    password            = db.Column(db.Text(),      nullable=False)
    urole               = db.Column(db.String(50),  nullable=False)

    name                = db.Column(db.String(60),  nullable=False)
    gender              = db.Column(db.String(60),  nullable=False)
    birthday            = db.Column(db.Date(),      nullable=False)