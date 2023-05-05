weather = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

city_temp = {key: ('WARM' if value >= 40 else "COLD") for (key, value) in weather.items()}

print(city_temp)
