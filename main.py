import tkinter as tk
from tkinter import ttk
import requests

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
        temp = ttk.Label(self, text='Temperature: ')
        temp.pack(side='top', anchor='w', padx=15, pady=5)

        condition = ttk.Label(self, text='Condition: ')
        condition.pack(side='top', anchor='w', padx=15, pady=5)

        humidity = ttk.Label(self, text='Humidity: ')
        humidity.pack(side='top', anchor='w', padx=15, pady=5)

        windSpeed = ttk.Label(self, text='Wind Speed: ')
        windSpeed.pack(side='top', anchor='w', padx=15, pady=5)

        topspacer = ttk.Label(self, text="")
        topspacer.pack(side='bottom', pady=5)

        self.mainloop()

    def display(self):
        print(self.entry.get())

class Weather:
    def __init__(self):
        pass

get_geocode = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=Ghaziabad&appid=ec99aec66d6d231466250cf9fb84d219")

# GET request to GeeksforGeeks
# get_response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=ec99aec66d6d231466250cf9fb84d219")

# Printing only the status code
print(get_geocode.json()[0]['lat'],get_geocode.json()[0]['lon'])

# GUI()