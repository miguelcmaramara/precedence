from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from ..database import models
from ..helpers import converters as conv

requests = Blueprint("requests", __name__)

@requests.route('/request/all_tasks')
def all_tasks():
    task_list = {}
    # tasks = models.Task.query.filter_by(visible=True).all()
    tasks = models.Task.query.all()
    for task,i in zip(tasks, range(len(tasks))):
        task_list[i] = conv.row2dict(task)
    print(task_list)
        
    return task_list
    # return jsonify({tasks:[tasks]})
    # return jsonify({tasks:[models.Task.query.filter_by(visible=True).all()]})
