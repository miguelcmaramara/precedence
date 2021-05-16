# Requirements:
# flask
# flask_sqlalchemy
# flask_migrate
# postgresql


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import POSTGRES


app = Flask(__name__)
# app.config['SQLALCHEMY_DATEBASE_URI'] = "postgresql://postgres:m1i2g3g4y5@localhost:5432/cars_api"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
print('postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"


@app.route('/hello')
def hello_world():
    print(1)
    # return {"hello": "world"}
    new_car = CarsModel(name='Subaru', model="Sedan", doors=4)
    print(1)
    db.session.add(new_car)
    print(2)
    db.session.commit()
    print(3)
    return {"message": f"car {new_car.name} has been created successfully."}


if __name__ == '__main__':
    app.run(debug=True)

# Imports and CarsModel truncated

@app.route('/cars')
def handle_cars():
    new_car = CarsModel(name='Subaru', model="Sedan", doors=4)
    print(1)
    db.session.add(new_car)
    print(2)
    db.session.commit()
    print(3)
    return {"message": f"car {new_car.name} has been created successfully."}