# Old app contents. kept temporarily during large transfer process
# 
# from flask import Flask#, register_blueprint
# from .database import models
# from .config import DB_CREDENTIALS
# from .testing import testing_database as tb
# from .templates import views as fviews
# from .database import requests
# from .database import posts

# print("-> database is running")

# def create_db(app):
#     models.db.init_app(app)
#     return models.db


# def create_app():
#     print("database is running")
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = \
#         'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' \
#         % DB_CREDENTIALS
#     print('postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s'
#         % DB_CREDENTIALS)

#     app.register_blueprint(fviews.frontend)
#     app.register_blueprint(tb.testing_db)
#     app.register_blueprint(requests.requests)
#     app.register_blueprint(posts.posts)
#     return app