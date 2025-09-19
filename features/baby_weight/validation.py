from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange

class BabyWeightForm(FlaskForm):
    gestation = FloatField('Gestation (days)', validators=[DataRequired(), NumberRange(min=200, max=300)])
    parity = SelectField('Parity', choices=[('0','0'), ('1','1'), ('2','2')], validators=[DataRequired()])
    age = FloatField('Age (years)', validators=[DataRequired(), NumberRange(min=18, max=60)])
    height = FloatField('Height (feet)', validators=[DataRequired(), NumberRange(min=1.0, max=8.0)])
    weight = FloatField('Weight (kg)', validators=[DataRequired(), NumberRange(min=20.0, max=200.0)])
    smoke = SelectField('Smoke', choices=[('0','No'), ('1','Yes')], validators=[DataRequired()])