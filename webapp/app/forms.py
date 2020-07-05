from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class CountryForm(FlaskForm):
    country = StringField('Country')
    submit = SubmitField('Search')
