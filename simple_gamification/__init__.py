from functools import wraps

from flask import Flask, render_template, current_app, redirect, url_for, flash
from flask_login import LoginManager, current_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
login_manager = LoginManager()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)
Migrate(app, db, compare_type=True)

## Login configs ##
login_manager.init_app(app)
login_manager.login_view = "auth.login"
login_manager.login_message = "You must be logged in to view this page."

def login_required(role=["ANY"]):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
               return current_app.login_manager.unauthorized()
            urole = current_user.urole
            if ( (urole not in role) and (role != ["ANY"])):
                flash("You do not have permission to access this page", "warning")
                return redirect(url_for('principal.index'))
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

## Blueprints
from simple_gamification.auth.views import auth

app.register_blueprint(auth)