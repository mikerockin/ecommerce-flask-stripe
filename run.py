# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_minify import Minify
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from app import app
from datetime import datetime



DEBUG  = app.config['DEBUG']
STRIPE = app.config['STRIPE_IS_ACTIVE'] 

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)
    
if DEBUG:
    app.logger.info('DEBUG            = ' + str(DEBUG) )
    app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE' )
    app.logger.info('STRIPE           = ' + str( STRIPE ) )

if __name__ == "__main__":
    app.run()

