
from flask import Flask, render_template
from .database import models
# import config
from flask_migrate import Migrate
# from testing import testing_database
from .config import DB_CREDENTIALS

print("database is running")
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' \
#     % config.DB_CREDENTIALS
# print('postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s'
#       % config.DB_CREDENTIALS)

# db.init_app(app)
# migrate = Migrate(app, db)
migrate = Migrate()

def create_db(app):
    models.db.init_app(app)
    migrate.init_app(app,models.db)
    return models.db


def create_app():
    print("database is running")
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = \
    #     'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' \
    #     % config.DB_CREDENTIALS
    # print('postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s'
    #     % config.DB_CREDENTIALS)
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' \
        % DB_CREDENTIALS
    print('postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s'
        % DB_CREDENTIALS)
    return app
    
if __name__ == '__main__':
    from testing import testing_database as tdb
    render_template(tdb.testing_db)


    app.run(debug=True)
