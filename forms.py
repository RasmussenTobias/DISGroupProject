from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class AddUserForm(FlaskForm):
    uid = IntegerField('uid',validators=[DataRequired()])
    username = StringField('uname', validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('add')

    