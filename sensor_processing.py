def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

data = [72, 55, 101, 90]
result = calculate_average(data)
print("Average PM2.5 reading:", result)

stations = [
    ["A1", 62],
    ["B2", 110],
    ["C3", 88],
    ["D4", 45]
]

for station in stations:
    print(f"{station[0]} → {station[1]}")

def report_status(stations, threshold):
    for station in stations:
        name = station[0]
        pm25 = station[1]
        if pm25 > threshold:
            print(f"{name} is above the threshold with PM2.5 = {pm25}")
        else:
            print(f"{name} is within safe limits with PM2.5 = {pm25}")

report_status(stations, 100)

Add Assignment 2 sensor data processing code
