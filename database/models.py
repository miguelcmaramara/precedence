from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ..config import DB_CREDENTIALS
import datetime as dt

app = Flask(__name__)  # remove later
db = SQLAlchemy(app)  # remove later
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % DB_CREDENTIALS


class Task(db.Model):
    # TODO: Get this documentation done
    """ This class represents portion of life to be improved or a project

    This class represents portion of life to be improved or a project.
    Each scope can contain one or more sub-scopes. A scope can be classified as
    a project. Projects are more actionable scopes that tasks can be associated
    with.  However, since scopes can also contain tasks, the distinction is
    more conceptual than logical.

    - **Parameters**::
        :param name: String - Name of the task
        :param status: String - Status of the task
                       Default - "Not Started"
                       Accepted Vals - "Not Started", "Started", "Depreciated",
                            "Backburner", "Event", "Blocked"
        :param priority: int - priority of the function
                         Default - #TODO add here
        :param visible: boolean - visibility of the task on the creen
                        Default - True

        :param start_date: datetime - Optional start of the task
                           Default=datetime.now()
        :param creation_date: datetime - Optional creation date parameter
                              Default=datetime.now()
        :param due_date: datetime - Optional date a task should be completed by
                         Default=datetime.MAX_YEAR()
        :param completion_date: datetime - date that task should be
                                           completed
        :param start_priority: #TODO add here
        :param creation_priority:
        :param due_priority:
        :param completion_priority:

        :param recur_task: Task - Optional previous recurring task in recurre seq

        :param super_task: Task - Optional task which depends on this task

        :param time_slots: Task - Optional timeslot which is associated with task

        scope
    """
    def __init__(  # TODO: get constructor done
        self,
        name,
        status="Not Started",
        priority=None, #TODO add priority here
        visibility=True,
        start_date=dt.now(),
        creation_date=dt.now(),
        due_date=dt.MAXYEAR,
        completion_date=None,
        start_priority=None, # TODO add a priorty function
        creation_priority=None, # Here too
        due_priority=None, # Here too
        completion_priority=None, # Here too
        recur_task=None, # Input task objects here and below
        super_task=None,
        time_slots=None,
        scope=None,
    ):
        self.name = name
        self.status = status
        self.priority = priority
        self.visible = visible

        self.start_date = start_date
        self.creation_date = creation_date
        self.due_date = due_date
        self.completion_date = completion_date

        self.start_priority = start_priority
        self.creation_priority = creation_priority
        self.due_priority = due_priority
        self.completion_priority = completion_priority

        self.self.recur_task = recur_task.id
        self.self.super_task = super_task.id
        self.self.time_slots = time_slot.id
        self.scope = scope.id

        name
        status
        priority
        visible
        
        start_date
        creation_date
        due_date
        completion_date
        
        start_priority
        creation_priority
        due_priority
        completion_priority
        
        recur_task

        super_task

        time_slots

        scope














    # TODO: get getter/setter ready for prioirty stuff

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    status = db.Column(db.Integer, nullable=False)
    priority = db.Column(db.Float, nullable=False)
    visible = db.Column(db.Boolean, nullable=False)

    start_date = db.Column(db.dateTime)
    creation_date = db.Column(db.dateTime, nullable=False)
    due_date = db.Column(db.dateTime)
    completion_date = db.Column(db.dateTime)

    start_priority = db.Column(db.dateTime)
    creation_priority = db.Column(db.dateTime, nullable=False)
    due_priority = db.Column(db.dateTime)
    completion_priority = db.Column(db.dateTime)

    recur_task = db.Column(db.Integer, db.ForeignKey("task.id"))
    recur_tasks = db.relationship("Task", backref="framework_task", lazy=True)

    super_task = db.Column(db.Integer, db.ForeignKey("task.id"))
    sub_tasks = db.relationship("Task", backref="super_task", lazy=True)

    time_slots = db.relationship("TimeSlow", backref="task", lazy=True)

    scope = db.Column(db.Integer, db.ForeignKey("Scope.id"))
    # TODO: implement tags
    # tags


class Scope(db.Model):
    """ This class represents portion of life to be improved or a project

    This class represents portion of life to be improved or a project.
    Each scope can contain one or more sub-scopes. A scope can be classified as
    a project. Projects are more actionable scopes that tasks can be associated
    with.  However, since scopes can also contain tasks, the distinction is
    more conceptual than logical.

    - **Parameters**::
        :param name: String - Name of the scope
        :param visibility: boolean - If the item should show up on the scopes
                          Default=True
        :param start_date: datetime - Optional start of the project
                           Default=datetime.now()
        :param creation_date: datetime - Optional creation date parameter
                              Default=datetime.now()
        :param due_date: datetime - Optional date a project/scope should be
                                    completed by
                         Default=datetime.MAX_YEAR()
        :param completion_date: datetime - date that project / scope should be
                                           completed
                                Default=None;
        :param project: boolean - If the scope is a project
        :param color: String - lowercase name of the color or Hex code
                      Default="red"
        :param super_scope: Scope - scope of which contains this task
                            Default="None"
    """
    def __init__(
        self,
        name,
        visibility=True,
        start_date=dt.now(),
        creation_date=dt.now(),
        due_date=dt.MAXYEAR,
        completion_date=None,
        project=False,
        color="red",
        super_scope=None
    ):
        self.name = name
        self.visibility = visibility
        self.start_date = start_date
        self.creation_date = creation_date
        self.due_date = due_date
        self.completion_date = completion_date
        self.super_scope = super_scope
        self.project = project
        self.color = color

    __tablename__ = 'scopes'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    visibility = db.Column(db.boolean, nullable=False)

    start_date = db.Column(db.dateTime)
    creation_date = db.Column(db.dateTime, nullable=False)
    due_date = db.Column(db.dateTime)
    completion_date = db.Column(db.dateTime)

    project = db.Column(db.Boolean, nullable=False)
    color = db.Column(db.String, nullable=False)

    # TODO: Is vvv a sep table?
    super_scope = db.Column(db.Integer, db.ForeignKey("scope.id"))
    sub_scopes = db.relationship("Scope", backref="super_scope", lazy=True)

    #NOTE Should I change the backref name of this haha
    tasks = db.relationship("Scope", backref="scope", lazy=True)


class TimeSlot(db.Model):
    """ This class represents a calendar event that may be associated with a task

    This class represents a calendar event that may be associated with a task.
    Each TimeSlot instance can be associated with one task and can be synced
    with external calendar apps

    - **Parameters**::
        :param name: Name of the Timeslot
        :param start_date: The start date/time of the timeslot
        :param end_date: The ending date/time of the timeslot
        :param creation_date: The date/time the timeslot was created
        :param task: The task associated with the timeslot
        :param success: The extent at which a task was finished
                        0 = Not applicable
                        1 = Very ineffectively (No work done)
                        2 = Neither inneffectively / effectively
                        3 = Very effectively (All work finished)
    """
    def __init__(
        self,
        name,
        start_date,
        end_date,
        creation_date=dt.now(),
        task=None,
        success=0
    ):
        self.task = task.id
        self.name = name
        self.success = success
        self.start_date = start_date
        self.end_date = end_date
        self.creation_date = creation_date

    __tablename__ = "time_slots"

    id = db.Column(db.Integer, primary_Key=True, nullable=False)
    name = db.Column(db.String, nullable=False)

    start_date = db.Column(db.dateTime, nullable=False)
    end_date = db.Column(db.dateTime, nullable=False)
    creation_date = db.Column(db.dateTime, nullable=False)

    task = db.Column(db.Integer, db.ForeignKey("task.id"))
    success = db.Column(db.Integer)
