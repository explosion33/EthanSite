from flask import session, render_template, flash, redirect, request, url_for, send_file
from werkzeug import secure_filename
from app import app
import os
import stat
import logging #change logging status of wekzeug
from random import randint

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("main.html", head="Start of Website")


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
