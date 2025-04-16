from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length, ValidationError
from datetime import date

class ReservationForm(FlaskForm):
    guest_name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    room_type = SelectField('Room Type', choices=[('single', 'Single'), ('double', 'Double'), ('suite', 'Suite')], validators=[DataRequired()])
    check_in_date = DateField('Check-In Date', format='%Y-%m-%d', validators=[DataRequired()])
    check_out_date = DateField('Check-Out Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Reserve Room')

    def validate_check_out(form, field):
        if field.data <= form.check_in_date.data:
            raise ValidationError('Check-out date must be after check-in date.')
        if field.data < date.today():
            raise ValidationError('Check-out date must be today or in the future.')