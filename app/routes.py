from flask import Blueprint, render_template
from app.forms import RunningForm
from app.helper import calculate_distance

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    form = RunningForm()
    distance = None
    
    if form.validate_on_submit():
        pace = form.pace.data
        time = form.time.data
        
        distance = calculate_distance(pace, time)
    
    return render_template('home.html', form=form, distance=distance)

