from flask import Blueprint, render_template, request, redirect, url_for
from ..database import models
from ..helpers import converters as conv
from datetime import datetime

frontend = Blueprint("frontend", __name__)

@frontend.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@frontend.route('/task', methods=["POST"])
def make_task():
    input = request.form
    print(input)
    due_date= None if input['due_date'] == ''\
        else datetime.strptime(input['due_date'],'%Y-%m-%dT%H:%M')
    start_date= datetime.now() if input['start_date'] == ''\
        else datetime.strptime(input['start_date'],'%Y-%m-%dT%H:%M')

    print(type(due_date))
    print(type(start_date))
    print(due_date)
    print(start_date)

    new_task = models.Task(
        input['name'] if input['name'] is not None else 'Untitled',
        input['status'],
        due_date= due_date,
        start_date= start_date
    )
    models.db.session.add(new_task)
    models.db.session.commit()
    print(conv.row2dict(new_task))
    return(redirect(url_for("frontend.index")))
