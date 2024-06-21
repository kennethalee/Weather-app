import tkinter as tk
from tkinter import messagebox
import requests
import datetime

# Function to fetch weather data
def fetch_weather(city):
    api_key = '343b1511061902a30faf2791d7eb4df9'
    base_weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    weather_url = f"{base_weather_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(weather_url)
    return response.json()

# Function to fetch forecast data
def fetch_forecast(city):
    api_key = '343b1511061902a30faf2791d7eb4df9'
    base_forecast_url = "http://api.openweathermap.org/data/2.5/forecast?"
    forecast_url = f"{base_forecast_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(forecast_url)
    return response.json()

# Function to display weather data
def show_weather():
    city = city_entry.get()  # Get city name from entry widget
    if city:
        weather_data = fetch_weather(city)  # Fetching weather data 
        if weather_data["cod"] != "404":
            # Extract data from json
            main = weather_data["main"]
            wind = weather_data["wind"]
            weather_desc = weather_data["weather"][0]["description"]

            # Update labels with fetched data
            temp_label.config(text=f"Temperature: {main['temp']}°C")
            feels_like_label.config(text=f"Feels Like: {main['feels_like']}°C")
            humidity_label.config(text=f"Humidity: {main['humidity']}%")
            wind_speed_label.config(text=f"Wind Speed: {wind['speed']} m/s")
            description_label.config(text=f"Weather: {weather_desc.capitalize()}")
            city_label.config(text=f"Showing data for {city.upper()}")
        else:
            messagebox.showerror("Error", "City not found")  # Error if city not found
    else: 
        messagebox.showwarning("Warning", "Please enter a city name")  # Error if city name is empty 

# Function to display weather forecast 
def show_forecast():
    city = city_entry.get()
    if city:
        forecast_data = fetch_forecast(city)
        if forecast_data["cod"] != "404":
            forecast_title = "Weather Forecast:\n"
            forecast_text = ""
            for item in forecast_data["list"][:5]:  # Displaying next 5 forecasts
                dt = datetime.datetime.fromtimestamp(item["dt"])
                main = item["main"]
                weather_desc = item["weather"][0]["description"]
                forecast_text += f"{dt.strftime('%Y-%m-%d %H:%M')} - {weather_desc.capitalize()}, Temp: {main['temp']}°C\n"

            forecast_label.config(text=forecast_text)
            forecast_title_label.config(text=forecast_title)
            city_label.config(text=f"Showing data for {city}")
        else: 
            messagebox.showerror("Error", "City not found")
    else: 
        messagebox.showwarning("Warning", "Please enter a city name")

# Function to bind enter key to fetch and show weather data
def on_enter(event):
    show_weather()

# Function to create reset button
def reset():
    city_entry.delete(0, tk.END)
    temp_label.config(text="")
    feels_like_label.config(text="")
    humidity_label.config(text="")
    wind_speed_label.config(text="")
    description_label.config(text="")
    forecast_title_label.config(text="")
    forecast_label.config(text="")

# Tkinter window settings

# Main window
app = tk.Tk()
app.title("Weather App")

# Window geometry (width x height)
app.geometry('400x600')

# Configure labels and entry fields (Weather information)
city_label = tk.Label(app, text="City", font=("Helvetica", 14))
city_label.pack(pady=10)

note_label = tk.Label(app, text="City, Country (ex: AU, USA)", font=("Helvetica", 10, "italic"))
note_label.pack(pady=(0, 10))

city_entry = tk.Entry(app, width=25, font=("Helvetica", 14))
city_entry.pack(pady=5)

# Send button
search_button = tk.Button(app, text="Send", command=show_weather, font=("Helvetica", 14))
search_button.pack(pady=10)

# Forecast button
forecast_button = tk.Button(app, text="Forecast", command=show_forecast, font=("Helvetica", 14))
forecast_button.pack(pady=10)

# Reset button
reset_button = tk.Button(app, text="Reset", command=reset, font=("Helvetica", 14))
reset_button.pack(pady=10)

city_label = tk.Label(app, text="", font=("Helvetica", 14))
city_label.pack()

temp_label = tk.Label(app, text="", font=("Helvetica", 12))
temp_label.pack()

feels_like_label = tk.Label(app, text="", font=("Helvetica", 12))
feels_like_label.pack()

humidity_label = tk.Label(app, text="", font=("Helvetica", 12))
humidity_label.pack()

wind_speed_label = tk.Label(app, text="", font=("Helvetica", 12))
wind_speed_label.pack()

description_label = tk.Label(app, text="", font=("Helvetica", 12))
description_label.pack()

# Configure labels and entry fields (Forecast function)
forecast_title_label = tk.Label(app, text="", font=("Helvetica", 12, "bold"), justify=tk.CENTER)
forecast_title_label.pack(padx=(0, 0), pady=(10,0))

forecast_label = tk.Label(app, text="", font=("Helvetica", 12), justify=tk.LEFT)
forecast_label.pack()

# Bind enter key for on_enter function
app.bind('<Return>', on_enter)

# Run the app
app.mainloop()

