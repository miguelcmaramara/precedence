from flask import Blueprint, request, redirect, url_for
from ..database import models

posts = Blueprint('posts', __name__)

@posts.route('/post/task_complete', methods=["POST"])
def task_complete():
    input = int(request.get_data())
    # print("...................")
    # print(request)
    # print("...................")
    # print(input)
    # print("...................")

    task = models.Task.query.get(input)
    task.completed_now()
    models.db.session.commit()

    return(redirect(url_for("frontend.index")))
