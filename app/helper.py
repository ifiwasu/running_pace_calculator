def min_per_km_to_kmh(pace_string):
    min_sec = pace_string.split(':')
    minutes = int(min_sec[0])
    seconds = int(min_sec[1])
    total_min = minutes + (seconds / 60)
    speed_in_kmh = 60 / total_min
    rounded_kmh = round(speed_in_kmh, 2)
    return rounded_kmh

def kmh_to_min_per_km(kmh):
    total_min_per_km = 60 / kmh
    minutes = int(total_min_per_km)
    seconds = (total_min_per_km - minutes) * 60
    rounded_seconds = round(seconds)
    return f"{minutes}:{rounded_seconds:02d}"

def calculate_time(speed, distance):
    time_in_hours = distance / speed
    hours = int(time_in_hours)

    remaining_minutes = (time_in_hours - hours) * 60
    minutes = int(remaining_minutes)

    seconds = (remaining_minutes - minutes) * 60
    rounded_seconds = round(seconds) 
    return f"{hours}:{minutes:02d}:{rounded_seconds:02d}"

def calculate_speed(distance, hours, minutes, seconds):
    total_time_in_hours = hours + (minutes / 60) + (seconds / 3600) 
    speed = distance / total_time_in_hours
    return round(speed, 2)

def calculate_distance(speed, hours, minutes, seconds):
    total_time_in_hours = hours + (minutes / 60) + (seconds / 3600) 
    distance = speed * total_time_in_hours
    return round(distance, 2)

