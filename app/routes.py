from flask import session, render_template, flash, redirect, request, url_for, send_file
from werkzeug import secure_filename
from app import app
import os
import stat
import logging #change logging status of wekzeug
from random import randint

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def getNavbar(route=None):
    navbar=[
        {
            "link": "/academics",
            "name": "Academics",
            "active": "",
        },
        {
            "link": "/programming",
            "name": "Programming",
            "active": "",
        },
        {
            "link": "/projects",
            "name": "Projects",
            "active": "",
        },
        {
            "link": "/volunteering",
            "name": "Volunteering",
            "active": "",
        },
        {
            "link": "/rocketry",
            "name": "Rocketry",
            "active": "",
        },
        {
            "link": "/sports",
            "name": "Sports",
            "active": "",
        }, 
    ]
    if route:
        for item in navbar:
            if item["link"] == request.path:
                item["active"] = "active"
    
    return navbar



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("main.html", navbar=getNavbar())

@app.route('/academics', methods=['GET', 'POST'])
def academics():
    return render_template("page.html", navbar=getNavbar(request.path))

@app.route('/programming', methods=['GET', 'POST'])
def programming():
    return render_template("page.html", navbar=getNavbar(request.path))

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template("page.html", navbar=getNavbar(request.path))

@app.route('/volunteering', methods=['GET', 'POST'])
def volunteering():
    return render_template("page.html", navbar=getNavbar(request.path))

@app.route('/rocketry', methods=['GET', 'POST'])
def rocketry():
    return render_template("page.html", navbar=getNavbar(request.path))

@app.route('/sports', methods=['GET', 'POST'])
def sports():
    return render_template("page.html", navbar=getNavbar(request.path))

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
