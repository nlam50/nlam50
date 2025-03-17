# Frivolous Ferrets - Nia Lam and Amanda Tan
# SoftDev
# K35 - mxrobbotto
# 2025-03-14
# time spent: 2.5

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    with app.app_context():
        from . import routes

    return app