from flask import session, render_template, flash, redirect, request, url_for, send_file , abort
from werkzeug import secure_filename
from app import app
import os
import stat
import ast
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
            "link": "/skills",
            "name": "Skills",
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
            if item["link"] in request.path:
                item["active"] = "active"
    
    return navbar

def getPageData(page, root = ""):
    f = open("pageData.txt", "r")
    t = f.read()
    f.close()
    datas = ast.literal_eval(t)

    data = None
    for d in datas:
        if root in d["root"] and d["title"] == page:
            data = d
            break

    if data:
        for section in data["sections"]:
            for group in section["groups"]:
                try:
                    group["size"]
                except:
                    group["size"] = "50%"
                
                try:
                    group["type"]
                except:
                    group["type"] = "text"

                try:
                    group["link"]
                except:
                    group["link"] = ""

                try:
                    group["imLink"]
                except:
                    group["imLink"] = ""
            
    print(data)
    return data

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("main.html", navbar=getNavbar())

@app.route('/academics', methods=['GET', 'POST'])
def academics():
    data = getPageData("Academic Highlights")

    if data:
        return render_template("page.html", navbar=getNavbar(request.path), data=data)
    else:
        abort(404)    


@app.route('/skills', methods=['GET', 'POST'])
def programming():
    data = getPageData("Skills")

    if data:
        return render_template("page.html", navbar=getNavbar(request.path), data=data)
    else:
        abort(404)    

    return render_template("list.html", navbar=getNavbar(request.path), data=data)

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    data = {
        'title': "Projects",
        'elements': [
            {
                'image': "holder.png",
                'title': "test",
                "link": "academics/test"
            },
            {
                'image': "holder.png",
                'title': "test2",
                "link": "academics/test2"
            },
            {
                'image': "holder.png",
                'title': "test3",
                "link": "academics/test3"
            },
            {
                'image': "holder.png",
                'title': "test4",
                "link": "academics/test4"
            },
            {
                'image': "holder.png",
                'title': "test5",
                "link": "academics/test5"
            },
            {
                'image': "holder.png",
                'title': "test6",
                "link": "academics/test6"
            },
        ],
    }
    return render_template("list.html", navbar=getNavbar(request.path), data=data)

@app.route('/volunteering', methods=['GET', 'POST'])
def volunteering():
    return render_template("list.html", navbar=getNavbar(request.path))

@app.route('/rocketry', methods=['GET', 'POST'])
def rocketry():
    data = getPageData("Rocketry")

    if data:
        return render_template("page.html", navbar=getNavbar(request.path), data=data)
    else:
        abort(404)    

    return render_template("list.html", navbar=getNavbar(request.path), data=data)

@app.route('/sports', methods=['GET', 'POST'])
def sports():
    return render_template("list.html", navbar=getNavbar(request.path))

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
