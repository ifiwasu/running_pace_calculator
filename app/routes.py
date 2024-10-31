from flask import Blueprint, render_template
from app.forms import RunningForm
from app.helper import calculate_distance, calculate_pace, calculate_time

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    form = RunningForm()
    
    if form.validate_on_submit():
        pace = form.pace.data
        time = form.time.data
        distance = form.distance.data
        
        if not distance:
            result = calculate_distance(pace, time)
            form.distance.data = result
        elif not time:
            result = calculate_time(pace, distance)
            form.time.data = result
        elif not pace:
            result = calculate_pace(time, distance)
            form.pace.data = result
    
    return render_template('home.html', form=form)