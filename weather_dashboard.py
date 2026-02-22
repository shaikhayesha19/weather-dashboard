import requests
import pandas as pd
import matplotlib.pyplot as plt

# City coordinates
cities = {
    "Pune": (18.52, 73.85),
    "Mumbai": (19.07, 72.87),
    "Delhi": (28.61, 77.23),
    "Bangalore": (12.97, 77.59),
    "Chennai": (13.08, 80.27)
}

data_list = []

for city, (lat, lon) in cities.items():
    url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(url, params=params)
    data = response.json()

    weather = data.get("current_weather", {})

    data_list.append({
        "City": city,
        "Temperature": weather.get("temperature"),
        "Wind Speed": weather.get("windspeed")
    })

df = pd.DataFrame(data_list)

print(df)

# ---------------- VISUALIZATION ---------------- #

# Temperature
plt.figure()
plt.bar(df["City"], df["Temperature"])
plt.title("Temperature by City")
plt.ylabel("°C")
plt.show()

# Wind Speed
plt.figure()
plt.plot(df["City"], df["Wind Speed"], marker='o')
plt.title("Wind Speed")
plt.show()