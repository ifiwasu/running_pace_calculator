from flask import Blueprint, render_template, request
from app.forms import RunningForm, RiegelForm
from app.helper import calculate_distance, calculate_pace, calculate_time, riegel_time_predictor

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    form = RunningForm()
    form_riegel = RiegelForm()
    riegel_result = None

    if request.method == 'POST':
        if 'submit_running' in request.form and form.validate_on_submit():
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

        elif 'submit_riegel' in request.form and form_riegel.validate_on_submit():
            base_time = form_riegel.base_time.data
            base_distance = form_riegel.base_distance.data
            target_distance = form_riegel.target_distance.data
            riegel_result = riegel_time_predictor(base_time, base_distance, target_distance)

    return render_template('home.html', form=form, form_riegel=form_riegel, riegel_result=riegel_result)

