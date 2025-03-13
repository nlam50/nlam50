from flask import Flask
import os
from .models import init_db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    with app.app_context():
        init_db()

    from . import routes

    return app
