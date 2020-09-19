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
    """
    getNavbar(route): returns a navbar dictionary useful for passing to html\n
    route : the routing of the page, used to highlight the active page
    """
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

def getPageData(ID, root = ""):
    """
    getPageData(ID, root) : reads teh data from a txt file, adds missing fields and returns for use in dynamic pages\n
    ID   : the page ID, used to search for page
    root : the root field of the page, use if you have pages with the same name
    """
    f = open("pageData.txt", "r")
    t = f.read()
    f.close()
    datas = ast.literal_eval(t)

    data = None
    for d in datas:
        if root in d["root"] and d["ID"] == ID:
            data = d
            break

    if data:
        try:
            data["sections"]
            page = True
        except:
            page = False
        
        if page:
            for section in data["sections"]:
                for group in section["groups"]:
                    try: #size
                        group["size"]
                    except:
                        group["size"] = "50%"
                    
                    try: #type
                        group["type"]
                    except:
                        group["type"] = "textImage"

                    try: #link
                        group["link"]
                    except:
                        group["link"] = ""

                    try: #imLink
                        group["imLink"]
                    except:
                        group["imLink"] = ""

                    try: #images
                        group["images"]
                    except:
                        group["images"] = "[]"

                    try: #autoSlide
                        group["autoSlide"]
                    except:
                        group["autoSlide"] = "false"
                    

            
    print(data)
    return data

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("main.html", navbar=getNavbar())

@app.route('/academics', methods=['GET', 'POST'])
def academics():
    data = getPageData("academic")

    if data:
        return render_template("page.html", navbar=getNavbar(request.path), data=data)
    else:
        abort(404)    

@app.route('/skills', methods=['GET', 'POST'])
def programming():
    data = getPageData("skills")

    if data:
        return render_template("page.html", navbar=getNavbar(request.path), data=data)
    else:
        abort(404)    

    return render_template("list.html", navbar=getNavbar(request.path), data=data)

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    data = getPageData("projects")
    data["origin"] = "projects/"

    if data:
        return render_template("list.html", navbar=getNavbar(request.path), data=data)
    else:
        abort(404)    

@app.route('/projects/<page>', methods=['GET', 'POST'])
def projectsData(page):
    data = getPageData(page, "projects")

    if data:
        return render_template("page.html", navbar=getNavbar(request.path), data=data)
    else:
        abort(404) 
    

@app.route('/volunteering', methods=['GET', 'POST'])
def volunteering():
    data = getPageData("volunteering")

    if data:
        return render_template("page.html", navbar=getNavbar(request.path), data=data)
    else:
        abort(404)    


@app.route('/rocketry', methods=['GET', 'POST'])
def rocketry():
    data = getPageData("rocketry")

    if data:
        return render_template("page.html", navbar=getNavbar(request.path), data=data)
    else:
        abort(404)    

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
