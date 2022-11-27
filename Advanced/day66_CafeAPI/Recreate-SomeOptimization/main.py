from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import random


# Create the app
app = Flask(__name__)

# Connected with the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)


# Create table
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(500), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        dictionary = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return dictionary


# Create initial database
# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


# ---------------- HTTP GET - Read Record ----------------- #
@app.route('/get', methods=['GET'])
def get_cafe():
    mode = request.args.get('mode')
    all_cafes = db.session.query(Cafe).all()
    print(type(all_cafes))
    random_cafe = random.choice(all_cafes)
    print(type(random_cafe))
    if mode == 'random':
        return jsonify(cafe={
                "name": random_cafe.name,
                "map_url": random_cafe.map_url,
                "img_url": random_cafe.img_url,
                "location": random_cafe.location,

                # Put some properties in a sub-category
                "amenities": {
                    "seats": random_cafe.seats,
                    "has_toilet": random_cafe.has_toilet,
                    "has_wifi": random_cafe.has_wifi,
                    "has_sockets": random_cafe.has_sockets,
                    "can_take_calls": random_cafe.can_take_calls,
                    "coffee_price": random_cafe.coffee_price,
                },
            })
    elif mode == 'all':
        return jsonify(cafes=[{
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,

            # Put some properties in a sub-category
            "amenities": {
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price,
            }
        } for cafe in all_cafes])
    else:
        return jsonify(
            error={'Bad Request': 'Mode is wrong'}
        ), 400


@app.route('/search', methods=['GET'])
def search():
    try:
        loc = request.args.get('loc').title()
        print(loc)
    except AttributeError:
        return jsonify(
            error={'Bad Request': 'Parameter missing'}
        ), 400
    target_cafe = Cafe.query.filter_by(location=loc).first()
    if target_cafe:
        return jsonify(
            cafe=target_cafe.to_dict(),
        )
    else:
        return jsonify(
            error={'Not Found': 'Sorry, no cafe at this location'}
        ), 404


# ---------------- HTTP POST - Create Record ----------------- #
@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        has_sockets=bool(request.form.get('has_sockets')),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        seats=request.form.get('seats'),
        coffee_price=request.form.get('coffee_price'),
    )
    try:
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(
            response={'Success': 'New cafe has been added'}
        ), 200
    except Exception:
        return jsonify(
            error={'Bad Request': 'Some data missing '}
        ), 400


# ---------------- HTTP PUT/PATCH - Create Record ----------------- #
@app.route('/update', methods=['PATCH'])
def update_cafe():
    cafe_id = request.args.get('id')
    new_price = request.args.get('price')

    try:
        cafe_to_update = Cafe.query.get(cafe_id)
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(
            response={'Success': 'Cafe has been updated'}
        ), 200
    except AttributeError:
        return jsonify(
            error={'Not Found': 'Sorry cafe with that id not exist'}
        ), 404


if __name__ == '__main__':
    app.run(debug=True)

