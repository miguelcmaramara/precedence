from flask import Blueprint, render_template, request, redirect, url_for
from ..database import models
from ..helpers import converters as conv
from datetime import datetime

frontend = Blueprint("frontend", __name__)

@frontend.route('/', methods=["POST","GET"])
def index():
    # if request.method=="POST":
    #     user=request.form
    return render_template('index.html')

@frontend.route('/task', methods=["POST"])
def make_task():
    input = request.form
    print(input)

    new_task = models.Task(
        input['name'] if input['name'] is not None else 'Untitled',
        1,
        due_date= datetime.strptime(input['due_date'],'%Y-%m-%dT%H:%M'),
        start_date= datetime.strptime(input['start_date'],'%Y-%m-%dT%H:%M'),
    )
    models.db.session.add(new_task)
    models.db.session.commit()
    print(conv.row2dict(new_task))
    return(redirect(url_for("frontend.index")))
