from ..database import models
import datetime as dt
from flask import Blueprint

print("-> testing_database loaded")
testing_db = Blueprint("testing", __name__)

@testing_db.route("/test")
def test():
    return{"message": f"testing successful"}

@testing_db.route("/test/add_task")
def add_task():
    new_task = models.Task(
        "test_task",
        1,
        due_date=dt.datetime.now() + dt.timedelta(days=2),
    )

    models.db.session.add(new_task)
    models.db.session.commit()
    return{"message": f"scope {new_task.name} has been created successfully"}


@testing_db.route("/test/add_scope")
def add_scope():
    new_scope = models.Scope(
        "test_scope"
    )

    models.db.session.add(new_scope)
    models.db.session.commit()
    return{"message": f"scope {new_scope.name} has been created successfully"}


@testing_db.route("/test/add_time_slot")
def add_time_slot():
    new_time_slot = models.TimeSlot(
        "test_time_slot",
        start_date=dt.datetime.now(),
        end_date=dt.datetime.now() + dt.timedelta(hours=5)
    )

    models.db.session.add(new_time_slot)
    models.db.session.commit()
    return{"message": f"time slot {new_time_slot.name} \
        has been created successfully"}


@testing_db.route("/test/<obj_type>/<obj_id>")
def get_obj(obj_type, obj_id):
    obj = None
    if(obj_type == "task"):
        obj = models.Task.query.get_or_404(obj_id)
    if(obj_type == "scope"):
        obj = models.Scope.query.get_or_402(obj_id)
    if(obj_type == "time_slot"):
        obj = models.TimeSlot.query.get_or_402(obj_id)
    else:
        return{"message": "type mismatch"}

    return{
        "message": "success",
        "obj": f"type: {obj.name} of {obj.__name__} type"
    }


@testing_db.route("/test/<obj_type>/<obj_id>/type")
def drop_obj(obj_type, obj_id):
    obj = None
    if(obj_type == "task"):
        obj = models.Task.query.get_or_404(obj_id)
    if(obj_type == "scope"):
        obj = models.Scope.query.get_or_402(obj_id)
    if(obj_type == "time_slot"):
        obj = models.TimeSlot.query.get_or_402(obj_id)
    else:
        return{"message": "type mismatch"}

    models.db.session.delete(obj)
    models.db.session.commit()

    return{
        "message": "success",
        "obj": f"type: {obj.name} of {obj.__name__} type has been deleted"
    }