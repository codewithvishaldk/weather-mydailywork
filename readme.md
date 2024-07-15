# Weather Forecast Application

This project is a Weather Forecast Application built in Python. It allows users to retrieve current weather information for a specified city using the Weatherbit API.

## Features

- Get current weather conditions, including temperature, humidity, wind speed, and a brief description.
- User-friendly command-line interface (CLI) or graphical user interface (GUI) options.

## Requirements

- Python 3.x
- `requests` library

You can install the required library using:

```bash
pip install requests
```

## Usage

### Non-GUI Version

1. **Run the Command-Line Interface:**

   To use the command-line version, create a file named `weather_forecast.py` and paste the following code:

   ```python
   import requests

   def get_weather(city):
       url = "https://api.weatherbit.io/v2.0/current"
       
       params = {
           "city": city,
           "key": "YOUR_API_KEY",  # Replace with your Weatherbit API key
           "units": "M"  # Metric units
       }

       response = requests.get(url, params=params)

       if response.status_code == 200:
           data = response.json()
           current_weather = data['data'][0]
           return {
               "location": current_weather['city_name'],
               "temperature": current_weather['temp'],
               "humidity": current_weather['rh'],
               "wind_speed": current_weather['wind_spd'],
               "description": current_weather['weather']['description']
           }
       else:
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
   ```

2. **Run the script:**

   ```bash
   python weather_forecast.py
   ```

### GUI Version

1. **Run the GUI Application:**

   To use the GUI version, create a file named `weather_forecast_gui.py` and paste the following code:

   ```python
   import tkinter as tk
   from tkinter import messagebox
   import requests

   def get_weather(city):
       url = "https://api.weatherbit.io/v2.0/current"
       
       params = {
           "city": city,
           "key": "YOUR_API_KEY",  # Replace with your Weatherbit API key
           "units": "M"  # Metric units
       }

       response = requests.get(url, params=params)

       if response.status_code == 200:
           data = response.json()
           current_weather = data['data'][0]
           return {
               "location": current_weather['city_name'],
               "temperature": current_weather['temp'],
               "humidity": current_weather['rh'],
               "wind_speed": current_weather['wind_spd'],
               "description": current_weather['weather']['description']
           }
       else:
           return None

   def show_weather():
       city = city_entry.get()
       weather_info = get_weather(city)

       if weather_info:
           output = (f"Location: {weather_info['location']}\n"
                     f"Temperature: {weather_info['temperature']} °C\n"
                     f"Humidity: {weather_info['humidity']}%\n"
                     f"Wind Speed: {weather_info['wind_speed']} m/s\n"
                     f"Weather: {weather_info['description']}\n")
           result_label.config(text=output)
       else:
           messagebox.showerror("Error", "City not found. Please check your input.")

   # Create the main window
   root = tk.Tk()
   root.title("Weather Forecast Application")
   root.geometry("400x300")
   root.configure(bg="#f0f0f0")

   # Create a title label
   title_label = tk.Label(root, text="Weather Forecast", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
   title_label.pack(pady=10)

   # Create input field
   city_label = tk.Label(root, text="Enter the name of a city:", bg="#f0f0f0")
   city_label.pack()

   city_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
   city_entry.pack(pady=5)

   # Create button to fetch weather
   fetch_button = tk.Button(root, text="Get Weather", command=show_weather, bg="#007BFF", fg="white", font=("Helvetica", 12))
   fetch_button.pack(pady=10)

   # Create label for displaying results
   result_label = tk.Label(root, text="", justify="left", bg="#f0f0f0", font=("Helvetica", 12))
   result_label.pack(pady=5)

   # Run the application
   root.mainloop()
   ```

2. **Run the script:**

   ```bash
   python weather_forecast_gui.py
   ```

## API Key

To run this application, you need to sign up for an API key from [Weatherbit](https://www.weatherbit.io/). Replace `YOUR_API_KEY` in the code with your actual API key.

## Example Usage

1. Enter a city name (e.g., "London", "New York") and press the button to get the current weather information.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

**Vishal**  
Email: [vishal.2302305051@gmail.com](mailto:vishal.2302305051@gmail.com)
```

### Notes

- Ensure to replace `YOUR_API_KEY` with your actual API key in both versions.
