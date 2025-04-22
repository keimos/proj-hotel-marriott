from flask import Flask, jsonify, requests
from models import db, Reservation
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db.init_app(app)
CORS(app) # Allo React frontend to talk to Flask

@app.before_first_request
def create_tables():
        db.create_all()

@app.route('/')
def home():
    return jsonify

@app.route('/reserve', methods=['GET','POST'])
def reserve():
    data = requests.get_json()
    try:
        new_reservation = Reservation(
            guest_name=data['guest_name'],
            room_type=data['room_type'],
            check_in_date=data['check_in_date'],
            check_out_date=data['check_out_date']
        )
        db.session.add(new_reservation)
        db.session.commit()
        return jsonify({"message": "Reservation created successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Error creating reservation: {str(e)}")
        return jsonify({"error": "Failed to create reservation"}), 500


@app.errorhandler(404)
def not_found_error(e):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500

if ___name___ == '__main__':
    app.run(debug=True)