import requests

def get_weather(city):
    url = "https://api.weatherbit.io/v2.0/current"

    params = {
        "city": city,
        "key": "579fb9be53164f1ea6e2be9504e24b85",  # Replace with your Weatherbit API key
        "units": "M"  # Metric units
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        current_weather = data['data'][0]

        temperature = current_weather['temp']
        humidity = current_weather['rh']
        wind_speed = current_weather['wind_spd']
        description = current_weather['weather']['description']
        city_name = current_weather['city_name']

        return {
            "location": city_name,
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "description": description
        }
    else:
        print("Error:", response.json().get("error", "Unknown error"))
        return None

def display_weather(weather_info):
    if weather_info:
        print(f"\nLocation: {weather_info['location']}")
        print(f"Temperature: {weather_info['temperature']} °C")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind Speed: {weather_info['wind_speed']} m/s")
        print(f"Weather: {weather_info['description']}\n")
    else:
        print("City not found. Please check your input.")

def main():
    print("Weather Forecast Application")
    city = input("Enter the name of a city: ")
    weather_info = get_weather(city)
    display_weather(weather_info)

if __name__ == "__main__":
    main()
