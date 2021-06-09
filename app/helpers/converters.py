# Credit:
# https://stackoverflow.com/questions/1958219/
# convert-sqlalchemy-row-object-to-python-dict?page=1&tab=votes#tab-top
# TODO: make my own suitable
# meant for temporary debugging
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d