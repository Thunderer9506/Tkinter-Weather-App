import tkinter as tk
from tkinter import ttk
import requests
from dotenv import load_dotenv
import os

load_dotenv()

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        # self.geometry("500x500")

        # Create a frame for the upper part of the UI
        upper_frame = ttk.Frame(self)
        upper_frame.pack(side='top', anchor='nw', padx=10, pady=10, fill='x')

        # Place the widgets in the frame
        label = ttk.Label(upper_frame, text="Enter City: ")
        label.pack(side='left', padx=5, pady=5)

        self.entry = ttk.Entry(upper_frame)
        self.entry.pack(side='left', padx=5, pady=5)

        button = ttk.Button(upper_frame, text="Submit", command=self.display)
        button.pack(side='left', padx=5, pady=5)

        # Add a spacer to separate the button from the labels
        topspacer = ttk.Label(self, text="")
        topspacer.pack(side='top', pady=5)

        # Place the labels below each other
        self.temp = ttk.Label(self, text='Temperature: ')
        self.temp.pack(side='top', anchor='w', padx=15, pady=5)

        self.condition = ttk.Label(self, text='Condition: ')
        self.condition.pack(side='top', anchor='w', padx=15, pady=5)

        self.humidity = ttk.Label(self, text='Humidity: ')
        self.humidity.pack(side='top', anchor='w', padx=15, pady=5)

        self.windSpeed = ttk.Label(self, text='Wind Speed: ')
        self.windSpeed.pack(side='top', anchor='w', padx=15, pady=5)

        topspacer = ttk.Label(self, text="")
        topspacer.pack(side='bottom', pady=5)

        self.mainloop()

    def display(self):
        weather = Weather(self.entry.get().title())
        data = weather.fetch_weatherData()
        self.temp['text'] = 'Temperature:'+data["main"]["temp"]
        self.condition['text'] = 'Condition:'+data["weather"]["description"]
        self.humidity['text'] = 'Humidity:'+data["main"]["humidity"]
        self.windSpeed['text'] = 'Wind Speed:'+data["wind"]["2.44"]+"km"


class Weather:
    def __init__(self,cityName):
        self.cityName = cityName
        self.appid = os.getenv("APPID")
        self.GEOURL = os.getenv("GEO_URL")
        self.WeatherURL = os.getenv("DATA_URL")
        self.GeoCode = self.get_geocoords()

    def get_geocoords(self):
        params = f"q={self.cityName}&appid={self.appid}"
        get_geocode = requests.get(self.GEOURL+params)
        data = get_geocode.json()[0]
        return (data['lat'],data['lon'])
    
    def fetch_weatherData(self):
        params = {
            'lat':self.GeoCode[0],
            'lon':self.GeoCode[1],
            'appid':self.appid,
            'units':"metric",
        }
        # params = f"lat={self.GeoCode[0]}&lon={self.GeoCode[1]}&appid={self.appid}&units=metric"
        get_geocode = requests.get(self.WeatherURL,params)
        data = get_geocode.json()
        return data

# get_geocode = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=Ghaziabad&appid=ec99aec66d6d231466250cf9fb84d219")

# GET request to GeeksforGeeks
# get_response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=ec99aec66d6d231466250cf9fb84d219")

# Printing only the status code
# print(get_geocode.json()[0]['lat'],get_geocode.json()[0]['lon'])

geocode = Weather("Ghaziabad")
print(geocode)


# GUI()