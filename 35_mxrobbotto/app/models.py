# Frivolous Ferrets - Nia Lam and Amanda Tan
# SoftDev
# K35 - mxrobbotto
# 2025-03-14
# time spent: 2.5

import sqlite3
import os
from flask import g

DATABASE = os.path.join(os.path.dirname(__file__), '../instance/site.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with get_db() as db:
        with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), 'r') as f:
            db.executescript(f.read())

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
