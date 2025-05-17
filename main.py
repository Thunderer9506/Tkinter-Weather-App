import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from dotenv import load_dotenv
import os

load_dotenv()

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")

        upper_frame = ttk.Frame(self)
        upper_frame.pack(side='top', anchor='nw', padx=10, pady=10, fill='x')

        label = ttk.Label(upper_frame, text="Enter City: ")
        label.pack(side='left', padx=5, pady=5)

        self.entry = ttk.Entry(upper_frame)
        self.entry.pack(side='left', padx=5, pady=5)

        button = ttk.Button(upper_frame, text="Submit", command=self.display)
        button.pack(side='left', padx=5, pady=5)

        topspacer = ttk.Label(self, text="")
        topspacer.pack(side='top', pady=5)

        self.temp = ttk.Label(self, text='Temperature: ')
        self.temp.pack(side='top', anchor='w', padx=15, pady=5)

        self.condition = ttk.Label(self, text='Condition: ')
        self.condition.pack(side='top', anchor='w', padx=15, pady=5)

        self.humidity = ttk.Label(self, text='Humidity: ')
        self.humidity.pack(side='top', anchor='w', padx=15, pady=5)

        self.windSpeed = ttk.Label(self, text='Wind Speed: ')
        self.windSpeed.pack(side='top', anchor='w', padx=15, pady=5)

        bottomSpacer = ttk.Label(self, text="")
        bottomSpacer.pack(side='bottom', pady=5)

        self.mainloop()

    def display(self):
        weather = Weather(self.entry.get().title())
        data = weather.fetch_weatherData()
        if "error" in data:
            messagebox.showerror("Error","No Such City/Area Exist")
        else:
            self.temp['text'] = f'Temperature: {data["main"]["temp"]}C'
            self.condition['text'] = f'Condition: {data["weather"][0]["description"]}'
            self.humidity['text'] = f'Humidity: {data["main"]["humidity"]}%'
            self.windSpeed['text'] = f'Wind Speed: {data["wind"]["speed"]} km/h'

class Weather:
    def __init__(self,cityName):
        self.cityName = cityName
        self.appid = os.getenv("APPID")
        self.GEOURL = os.getenv("GEO_URL")
        self.WeatherURL = os.getenv("DATA_URL")
        self.GeoCode = self.get_geocoords()

    def get_geocoords(self):
        params = {
            'q':self.cityName,
            'appid':self.appid,
        }

        get_geocode = requests.get(self.GEOURL,params)
        try:
            data = get_geocode.json()[0]
            return (data['lat'],data['lon'])
        except Exception as e:
            return {'error':e}
    
    def fetch_weatherData(self):
        try:
            params = {
                'lat':self.GeoCode[0],
                'lon':self.GeoCode[1],
                'appid':self.appid,
                'units':"metric",
            }

            get_weatherData = requests.get(self.WeatherURL,params)
            data = get_weatherData.json()
            return data
        except Exception as e:
            return {'error': str(e)}
        

GUI()