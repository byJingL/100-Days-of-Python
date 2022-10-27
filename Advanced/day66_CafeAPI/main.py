from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

API_KEY = 'TopSecretAPIKey'

# --------------- Create APP ----------------- #
app = Flask(__name__)

# ------------- Connect to Database --------------- #
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# ------------- Cafe TABLE Configuration --------------- #
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        #Method 1. Loop through each column in the data record
        dictionary = {}
        for column in self.__table__.columns:
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)

        # Method 2.Use Dictionary Comprehension to do the same thing.
        dictionary = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")
    

# --------------- HTTP GET - Read Record --------------#
@app.route('/random', methods=['GET'])
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all', methods=['GET'])
def get_all_cafe():
    cafes = db.session.query(Cafe).all()
    # cafe_list = []
    # for cafe in cafes:
    #     cafe_list.append(cafe.to_dict())

    # Use List Comprehension to do the same thing
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route('/search', methods=['GET'])
def search_cafe():
    # request->params use request.args.get()
    query_location = request.args.get('loc').capitalize()
    target_cafe = Cafe.query.filter_by(location=query_location).first()
    # Method 1. Use If
    # Method 2. (in def update_price) Use Exceptions
    if target_cafe:
        return jsonify(cafe=target_cafe.to_dict())
    else:
        return jsonify(
            error={"Not Found": "Sorry, we don't have a cafe at that location."}
        ), 404


# --------------- HTTP POST - Create Record --------------#
@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        # request->body->form use request.form.get()
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        # Change the datatype to boolean
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price'),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(
        response={"success": "Successfully added the new cafe."}
    ), 200


# --------------- HTTP PUT/PATCH - Update Record --------------#
@app.route('/update-price/<cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    price = request.args.get('new_price')
    cafe_to_update = Cafe.query.filter_by(id=cafe_id).first()
    # Method 1. (in def search_cafe) Use If
    # Method 2. Use Exceptions
    try:
        cafe_to_update.coffee_price = price
        db.session.commit()
        return jsonify(
            response={"success": "Successfully updated the price."}
        ), 200
    except AttributeError:
        return jsonify(
            error={"Not Found": "Sorry a cafe with that id was not found in the database."}
        ), 404


# --------------- HTTP DELETE - Delete Record --------------#
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    api = request.args.get('api_key')
    if api != API_KEY:
        return jsonify(
          error={"Bad Request": "Sorry, that's not allowed. Make sure you have the correct api_key."}
        ), 400
    else:
        cafe_to_delete = Cafe.query.filter_by(id=cafe_id).first()
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(
                response={"success": "Successfully deleted the closed cafe."}
            ), 200
        else:
            return jsonify(
                error={"Not Found": "Sorry a cafe with that id was not found in the database."}
            ), 404


if __name__ == '__main__':
    app.run(debug=True)
