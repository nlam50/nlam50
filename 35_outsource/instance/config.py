import os

SECRET_KEY = os.urandom(32)
DATABASE = os.path.join(os.path.dirname(__file__), 'site.db')
