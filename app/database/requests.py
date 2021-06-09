from flask import Blueprint, render_template
from ..database import models

requests = Blueprint('requests', __name__)

@requests.route('/request/all_tasks')
def all_tasks():
    # print("--------------------------------------------------------------------------------------")
    # print(render_template('tasks.html', tasks=models.Task.query.all()))
    # print("--------------------------------------------------------------------------------------")
    # tasks = models.Task.query.filterby(visible=True).all()
    db_tasks = (models.Task.query
        .filter_by(visible=True)
        .order_by(models.Task.priority.desc())
        )
    for task in db_tasks:
        task.update_prio()
    return render_template('tasks.html', tasks=db_tasks)
