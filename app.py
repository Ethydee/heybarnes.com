import datetime as dt
import os
import random as rd
from datetime import datetime
from functools import wraps

import pandas as pd
import qrcode
from flask import Flask
from flask import abort
from flask import redirect
from flask import render_template
from flask import request

from forms import PostForm
from forms import TicketForm

app = Flask(__name__)
app.config["TRAP_BAD_REQUEST_KEY_ERRORS"] = True
app.config['SECRET_KEY'] = "#########"


def BlockedAddress(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if request.remote_addr != "173.16.171.238":
            return f(*args, **kwargs)
        else:
            return abort(403)
    return wrapped


def convertdate(date):
    year, monthnum, day = date.split("-")
    if monthnum[0] == "0":
        monthnum = monthnum[1]
    monthnum = int(monthnum)
    month = dt.date(1900, monthnum, 1).strftime('%B')
    return f"{month} {day}, {year}"


def grad(num):
    if num >= 98 < 100:
        let = "A+"
    elif num >= 90 < 98:
        let = "A"
    elif num >= 80 < 90:
        let = "B"
    elif num >= 70 < 80:
        let = "C"
    else:
        let = "F"
    return let



def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return rd.randint(range_start, range_end)


def get_posts():
    f = pd.read_csv("posts.csv")
    names = list(f.name)
    text = list(f.post)
    image = list(f.image)
    times = list(f.time)
    posts = []
    for i in range(len(names)):
        posts += [{
            'author': {'username': names[i]},
            'body': text[i],
            'image': image[i],
            'time': times[i]
        }]
    posts.reverse()
    return posts


def savepost(formdata):
    f = open("posts.csv", "a")
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    if len(formdata['image']) == 0:
        p = f"\n\"{formdata['username']}\",\"{formdata['postbox']}\",\"\\x00\",{dt_string}"
    else:
        p = f"\n\"{formdata['username']}\",\"{formdata['postbox']}\",\"{formdata['image']}\",{dt_string}"
    f.write(p)
    f.close()


@app.errorhandler(500)
def backend_error(e):
    return render_template('500.html'), 500


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
@app.route('/index')
@BlockedAddress
def index():
    if "ron" in request.args:
        if request.args["ron"] == "6969":
            return render_template('index.html', ron=True)
    names = ["Ron", "Shane", "Mr. Walter", "Barnes", "Mr. Hudson", "Mr. Owen"]
    rdict = {}
    grades = {}
    user = {'username': rd.choice(names)}
    for i in names:
        rdints = [rd.randint(60, 100), rd.randint(60, 100)]
        rdint = sorted(rdints)[-1]
        letter = grad(rdint)
        rdict[i] = (rdint, letter)
    for name in rdict:
        grade = rdict.get(name)
        grades[name] = grade
    return render_template('index.html', title='Ronin', grades=grades, user=user)


@app.route("/post", methods=['GET', 'POST'])
@BlockedAddress
def post():
    form = PostForm()
    if form.is_submitted():
        result = request.form
        for post in result:
            print(result[post])
            if len(result[post]) > 200:
                return redirect('forum')
        savepost(result)
        print(result)
        return redirect('forum')
    return render_template("post.html", form=form)


@app.route("/forum")
@BlockedAddress
def forum():
    f = open('posts.csv', 'r')
    amount = len(f.readlines()) - 1
    return render_template("forum.html", posts=get_posts(), amount=amount)


@app.route("/ticketmaker", methods=['GET', 'POST'])
@BlockedAddress
def ticketmaker():
    form = TicketForm()
    if form.is_submitted():
        ticket = {}
        result = request.form
        print(result)
        alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ticket["FID"] = rd.choice(alph) + rd.choice(alph) + rd.choice(alph) + str(random_with_N_digits(4))
        ticket["lastname"] = result["name"].split(" ")[1].upper()
        ticket["firstname"] = result["name"].split(" ")[0].upper()
        ticket["namecode"] = str(random_with_N_digits(5)) + "-" + ticket["lastname"]
        img = qrcode.make(ticket["namecode"])
        img.save(f"{os.getcwd()}/static/images/pict0.png", "PNG")
        if result["radio"] == "bills":
            ticket["bills"] = "X"
        else:
            ticket["coins"] = "X"
        ticket["money"] = format(float(result["money"]), '.2f')
        ticket["date"] = convertdate(result["date"]).upper()
        return render_template("tooth_ticket.html", result=result, ticket=ticket)
    return render_template("make_ticket.html", form=form)


@app.route("/hudson")
@BlockedAddress
def hudson():
    return render_template("hudson.html")


@app.route("/simon")
@BlockedAddress
def simon():
    return render_template("simon.html")

@app.route("/CSPproject")
@BlockedAddress
def csp():
    return render_template("CSPproject.html")

@app.route("/page2")
@BlockedAddress
def page2():
    return render_template("page2.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
