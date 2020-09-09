
import datetime
from functools import wraps
from flask import Flask, flash, redirect, render_template, request, session, url_for, request
from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy
# from flask.ext.navigation import Navigation
from flask_nav.elements import Navbar, View


app = Flask(__name__)
# app.config.from_object('_config')
db = SQLAlchemy(app)



@app.route("/Home")
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/portfolio")
@app.route("/Portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/about")
@app.route("/About")
def about():
    return render_template('about.html')

@app.route("/resume")
@app.route("/resumé")
@app.route("/Resumé")
def resume():
    return render_template('resume.html')

