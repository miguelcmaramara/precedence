from app import create_app, create_db
from flask_migrate import Migrate


app = create_app()
db = create_db(app)

migrate = Migrate(app,db, compare_type=True)


if __name__ == "__main__":
    app.run(debug=True)