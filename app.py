from flask import Flask, render_template, requests, redirect, url_for, flash
from werkzeug.exceptions import HTTPException
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db.init_app(app)

@app.before_first_request
def create_tables():
        db.create_all()

if___name___ == '__main__':
    app.run(debug=True)