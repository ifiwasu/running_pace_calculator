from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RunningForm(FlaskForm):
    pace = StringField('Pace (min/km)', validators=[DataRequired()])
    time = StringField('Duration (hh:mm:ss)', validators=[DataRequired()])
    submit = SubmitField('Calculate Distance')


