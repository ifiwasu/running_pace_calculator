def convert_time_to_minutes(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_minutes = (hours * 60) + minutes + (seconds / 60)
    return total_minutes

def convert_pace_to_minutes(pace_str):
    minutes, seconds = map(int, pace_str.split(':'))
    return minutes + (seconds / 60)

def calculate_distance(pace, time):
    time_in_minutes = convert_time_to_minutes(time)
    pace_in_minutes = convert_pace_to_minutes(pace)
    
    distance = time_in_minutes / pace_in_minutes
    return round(distance, 2)

# print(calculate_distance('6:00', '1:00:00'))