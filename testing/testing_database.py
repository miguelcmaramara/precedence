from ..database import models
import datetime as dt
from flask import Blueprint
from .. helpers import converters as conv

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
    return{
        "message": f"scope {new_task.name} has been created successfully",
        "obj": conv.row2dict(new_task)
    }

@testing_db.route("/test/add_scope")
def add_scope():
    new_scope = models.Scope(
        "test_scope"
    )

    models.db.session.add(new_scope)
    models.db.session.commit()
    return{"message": f"scope {new_scope.name} has been created successfully",
        "obj": conv.row2dict(new_scope)
    }



@testing_db.route("/test/add_time_slot")
def add_time_slot():
    new_time_slot = models.TimeSlot(
        "test_time_slot",
        start_date=dt.datetime.now(),
        end_date=dt.datetime.now() + dt.timedelta(hours=5)
    )

    models.db.session.add(new_time_slot)
    models.db.session.commit()
    return{"message": f"time slot {new_time_slot.name} has been created successfully",
        "obj": conv.row2dict(new_time_slot)
    }



@testing_db.route("/test/<obj_type>/<obj_id>")
def get_obj(obj_type, obj_id):
    obj = None
    print(obj_type)
    if(obj_type == "task"):
        obj = models.Task.query.get_or_404(obj_id)
    elif(obj_type == "scope"):
        obj = models.Scope.query.get_or_404(obj_id)
    elif(obj_type == "time_slot"):
        obj = models.TimeSlot.query.get_or_404(obj_id)
    else:
        return{"message": "type mismatch"}

    return{
        "message": f"success: {obj.name} of {type(obj).__name__} type",
        "obj": conv.row2dict(obj)
    }


@testing_db.route("/test/<obj_type>/<obj_id>/drop")
def drop_obj(obj_type, obj_id):
    obj = None
    if(obj_type == "task"):
        obj = models.Task.query.get_or_404(obj_id)
    elif(obj_type == "scope"):
        obj = models.Scope.query.get_or_404(obj_id)
    elif(obj_type == "time_slot"):
        obj = models.TimeSlot.query.get_or_404(obj_id)
    else:
        return{"message": "type mismatch"}

    models.db.session.delete(obj)
    models.db.session.commit()

    return{
        "message": f"success: deleted {obj.name} of {type(obj).__name__} type",
        "obj": conv.row2dict(obj)
    }