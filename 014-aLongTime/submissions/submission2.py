from datetime import datetime, timedelta
import re


date_times = {}
pattern = r"((?:\d*-?){3}\s(?:\d*:?){3})\s-\s((?:\d*-?){3}\s(?:\d*:?){3})\s\|\s([a-zA-Z]*)\n"
with open('time.log', 'r') as f:
    max_val = (timedelta.min, '')
    min_val = (timedelta.max, '')
    delta_sum = timedelta()

    matches = re.findall(pattern, f.read())
    for match in matches:
        start, end, code = match
        delta = datetime.strptime(end, '%Y-%m-%d %H:%M:%S') - datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        if delta < min_val[0]:
            min_val = (delta, code)

        if delta > max_val[0]:
            max_val = (delta, code)

        date_times[code] = delta
        delta_sum += delta

    average_delta = delta_sum / len(matches)
    closest_val = (delta, code)
    for code, delta in date_times.items():
        if abs(delta - average_delta) < abs(closest_val[0] - average_delta):
            closest_val = (delta, code)

    print(f"Shortest time delta: {min_val[1]}")
    print(f"Longest time delta: {max_val[1]}")
    print(f"Closest time delta: {closest_val[1]}")
