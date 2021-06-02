from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from ..database import models
from ..helpers import converters as conv

requests = Blueprint('requests', __name__)

@requests.route('/request/all_tasks')
def all_tasks():
    print("--------------------------------------------------------------------------------------")
    print(render_template('tasks.html', tasks=models.Task.query.all()))
    print("--------------------------------------------------------------------------------------")
    return render_template('tasks.html', tasks=models.Task.query.all())
