# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

# import Flask 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager




db = SQLAlchemy()

from .config import Config

# Inject Flask magic
app = Flask(__name__)

# load Configuration
app.config.from_object( Config ) 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
db.init_app(app)

from .models import User
from app import db
from app.models import VisitCounter

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()

# Import routing to render the pages
from app import views



def init_visit_counter():
    with app.app_context():
        db.create_all()  # Создает все таблицы, если они не существуют
        if not VisitCounter.query.first():
            counter = VisitCounter(count=0)
            db.session.add(counter)
            db.session.commit()

init_visit_counter()