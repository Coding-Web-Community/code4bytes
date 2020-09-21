from datetime import datetime


delta_array = []
delta_sum = 0
max_delta = (0, '')
min_delta = (float('inf'), '')

with open('time.log') as f:
    for row in f:
        dates, code = row.split(' | ')
        dates = dates.split(' - ')
        code = code.strip()

        delta = (datetime.fromisoformat(dates[1]) - datetime.fromisoformat(dates[0])).total_seconds()
        if delta > max_delta[0]:
            max_delta = (delta, code)

        if delta < min_delta[0]:
            min_delta = (delta, code)

        delta_sum += delta
        delta_array.append((delta, code))

    average = delta_sum / len(delta_array)
    closest_delta = min(delta_array, key=lambda x: abs(x[0]-average))
    print(f"Shortest time delta: {min_delta[1]}")
    print(f"Longest time delta: {max_delta[1]}")
    print(f"Closest time delta: {closest_delta[1]}")
