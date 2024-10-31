def convert_time_to_minutes(time):
    hours, minutes, seconds = map(int, time.split(':'))
    return hours * 60 + minutes + seconds / 60

def convert_pace_to_minutes(pace):
    minutes, seconds = map(int, pace.split(':'))
    return minutes + seconds / 60

def calculate_distance(pace, time):
    time_in_minutes = convert_time_to_minutes(time)
    pace_in_minutes = convert_pace_to_minutes(pace)
    
    distance = time_in_minutes / pace_in_minutes
    return round(distance, 2)

def calculate_time(pace, distance):
    pace_in_minutes = convert_pace_to_minutes(pace)
    time_in_minutes = pace_in_minutes * float(distance)
    
    hours = int(time_in_minutes // 60)
    minutes = int(time_in_minutes % 60)
    seconds = int((time_in_minutes * 60) % 60)
    
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def calculate_pace(time, distance):
    time_in_minutes = convert_time_to_minutes(time)
    pace_in_minutes = time_in_minutes / float(distance)
    
    minutes = int(pace_in_minutes)
    seconds = int((pace_in_minutes * 60) % 60)
    
    return f"{minutes}:{seconds:02}"
