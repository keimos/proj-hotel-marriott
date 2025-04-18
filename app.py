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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserve', methods=['GET','POST'])
def reserve():
    form = ReservationForm()
    if form.validate_on_submit():
        try:
             new_reservation = Reservation(
                guest_name=form.guest_name.data,
                room_type=form.room_type.data,
                check_in_date=form.check_in_date.data,
                check_out_date=form.check_out_date.data
             )
             db.session.add(new_reservation)
             db.session.commit()
             flash('Reservation successful!', 'success')
             return redirect(url_for('success'))
        except Exception as e:
            db.session.rollback()
            flash('Reservation failed. Please try again: {}'.format(str(e)), 'danger')
    return render_template('reserve.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.errorhandler(HTTPException)
def handle_exception(e):
    return render_template("error.html", error=e), e.code

@app.errorhandler(Exception)
def handle_general_error(e):
    app.logger.error(f"Unhandled Exception: {str(e)}")
    return render_template("error.html", error="An unexpected error occurred."), 500

if ___name___ == '__main__':
    app.run(debug=True)