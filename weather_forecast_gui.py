import tkinter as tk
from tkinter import messagebox
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
title_label = tk.Label(root, text="Weather Forecast Application \n by vishal", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
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
