# TODO: Write documentation
import datetime as dt


def priorityTest():
    return -1


def priorityFromTask(task, dateNow=dt.datetime.now(), dateDue=None):
    if dateDue is not None:
        dateDue = task.due_date

    return priority(
            ["proj1", "proj2"],
            ["tag1", "tag2"],
            dateDue,
            dateNow
        )


def priority(scopes, tags, dateDue, dateNow=dt.datetime.now(), precision="Hours"):
    # model:
    # 4 ^ (dateBetween(now(), end(prop("Due Date")), "hours") / 100 +
    # 1.5 ^ prop("Difficulty") - .75

    prio = 0
    # Projects

    try:
        for scope in scopes:
            prio += sampleScopes[scope]  # Assumes scope pre defined
    except TypeError:
        prio += sampleScopes[scopes]

    # Tags
    for tag in tags:
        prio += sampleTags[tag]  # Assumes tag in list before it is called

    # Date
    dateBetween = dateNow - dateDue
    prio += 4**(-dateBetween.seconds/3600) / 100 + 1.5**1
    # TODO: Fix prio
    print(f"prio: {prio}")
    print(-dateBetween.seconds)
    print(-dateBetween.seconds/3600)
    print(4**(-dateBetween.seconds/3600))
    print(4**(-dateBetween.seconds/3600)/100)
    print(4**(-dateBetween.seconds/3600)/100 + 1.5 **1)

    return prio


precision = {  # TODO: implement precision
    "hours": 1
}

sampleTags = {  # Placeholder tags
    "tag1": 1,
    "tag2": 10,
    "tag3": 100
}

sampleScopes = {  # Placeholder scopes
    None: 0,
    "scope1": .1,
    "scope2": .01,
    "scope3": .001,
}
