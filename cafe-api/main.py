from crypt import methods
import random
from urllib import response
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
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


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price
    })


@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    cafe_list = []
    for cafe in cafes:
        cafe_dict = {"id": cafe.id,
                     "name": cafe.name,
                     "map_url": cafe.map_url,
                     "img_url": cafe.img_url,
                     "location": cafe.location,
                     "seats": cafe.seats,
                     "has_toilet": cafe.has_toilet,
                     "has_wifi": cafe.has_wifi,
                     "has_sockets": cafe.has_sockets,
                     "can_take_calls": cafe.can_take_calls,
                     "coffee_price": cafe.coffee_price}
        cafe_list.append(cafe_dict)
    all_cafes = {"cafes": cafe_list}
    print(all_cafes)
    all_cafes_json = jsonify(cafes=all_cafes["cafes"])
    return all_cafes_json


@app.route("/search", methods=["GET"])
def get_cafe_at_location():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe={"id": cafe.id,
                             "name": cafe.name, 
                             "map_url": cafe.map_url,
                             "img_url": cafe.img_url, 
                             "location": cafe.location, 
                             "seats": cafe.seats,
                             "has_toilet": cafe.has_toilet,
                             "has_wifi": cafe.has_wifi,
                             "has_sockets": cafe.has_sockets,
                             "can_take_calls": cafe.can_take_calls,
                             "coffee_price": cafe.coffee_price})
    else:
        return jsonify(error={"message": "No cafe found at that location"})


# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["GET","PATCH"])
def update_price_at_cafe_id(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
  
    if cafe:
        new_price = request.args.get("new_price")
        cafe.coffee_price = f"£{float(new_price)}"
        db.session.commit()
        return jsonify(response={"message": "Cafe price updated"}), 200
    else:
        return jsonify(error={"message": "No cafe found with that ID"}), 404
        
    
# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_close_at_cafe_id(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success":"Successfully delete the cafe from teh database"}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a Cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, That's not allowed. make sure you have the correct Api Key"}), 403
    

if __name__ == '__main__':
    app.run(debug=True)
