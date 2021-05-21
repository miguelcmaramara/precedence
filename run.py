from .app import create_app, create_db
from flask import render_template
from flask_migrate import Migrate
# from testing import testing_database


app = create_app()
db = create_db(app)

# render_template(testing_database.testing_db)
migrate = Migrate(app,db)


if __name__ == "__main__":
    app.run(debug=True)