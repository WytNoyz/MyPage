#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""HTTP route definitions"""

from flask import g
from app import app
import sqlite3

DATABASE = "online_store.db"


def get_db():
    deb = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)


def return_users():
    cursor = get_db().execute("select * from user", ())
    results - cursor.fetchall()
    cursor.close()
    return results


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route('/')
@app.route('/nate')
def index():
    return "Hello, World!"


@app.get('/users')
def get_users():
    cursor = get_db().execute("select * from user", ())
    results = cursor.fetchall()
    cursor.close()
    return results


@app.route('/aboutme')
def about_me():
    me = {"first_name": "Nate",
          "last_name": "Newport",
          "hobby": "Cool stuff"}
    return me
