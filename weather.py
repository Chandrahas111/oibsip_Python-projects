import requests
import tkinter as tk
from tkinter import ttk

API_KEY = 'b0857f923be03de237cf5dd7fd31e712'

# Function to get weather data for a city
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            "city": data["name"],
            "weather": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_data
    else:
        return None

# Function to display weather data
def display_weather():
    city_name = city_entry.get()
    weather_data = get_weather(city_name)

    if weather_data:
        weather_text.delete(1.0, tk.END)  # Clear previous text
        weather_text.insert(tk.END, f"Weather in {weather_data['city']}:\n\n")
        weather_text.insert(tk.END, f"Description: {weather_data['weather']}\n")
        weather_text.insert(tk.END, f"Temperature: {weather_data['temperature']}°C\n")
        weather_text.insert(tk.END, f"Humidity: {weather_data['humidity']}%\n")
        weather_text.insert(tk.END, f"Wind Speed: {weather_data['wind_speed']} m/s\n")
    else:
        weather_text.delete(1.0, tk.END)
        weather_text.insert(tk.END, "Error retrieving weather data.")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create input field and button
city_entry = ttk.Entry(root, width=30)
city_entry.pack(pady=10)

get_weather_button = ttk.Button(root, text="Get Weather", command=display_weather)
get_weather_button.pack(pady=10)

# Create text area to display weather data
weather_text = tk.Text(root, height=10, width=50)
weather_text.pack(pady=10)

# Run the main event loop
root.mainloop()