import requests

API_KEY = "1a400c37eeef09c4dfeaf85f761d1a77"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print("\nWeather Report")
    print("----------------------")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

else:
    print("City not found!")