from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField

class RunningForm(FlaskForm):
    pace = StringField('Pace (min/km)')
    time = StringField('Duration (hh:mm:ss)')
    distance = StringField('Distance (k)')
    result = HiddenField()
    submit = SubmitField('Calculate Distance')

    def validate_on_submit(self):
        # Call the original validate to trigger field validators if needed
        initial_validation = super(RunningForm, self).validate_on_submit()
        
        if not initial_validation:
            return False
        
        filled_fields = sum(bool(field.data) for field in [self.pace, self.time, self.distance])
        if filled_fields != 2:
            self.pace.errors.append("Vul twee van de drie velden in om de derde waarde te berekenen.")
            return False
        
        return True