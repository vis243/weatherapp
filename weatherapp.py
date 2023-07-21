import tkinter as tk
import requests
#import tkFont
from tkinter import font
def test_function(entry):
    print("this is the entry",entry)


#118a268f17ba697c03aa2c1b0ec5bca8
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}


def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str




def get_weather(city):
    weather_key="118a268f17ba697c03aa2c1b0ec5bca8"
    url="https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)

    '''print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])'''

root=tk.Tk()    

canvas=tk.Canvas(root,height=500,width=700)
background_image=tk.PhotoImage(file="vb.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)
frame=tk.Frame(root,bg="yellow",bd=5)
button=tk.Button(frame, text="Get Weather",bg="grey",fg="white",command=lambda: get_weather(entry.get()))

entry=tk.Entry(frame,font=("algerian",24))
lower_frame=tk.Frame(root,bg="yellow",bd=5)
label=tk.Label(lower_frame,bd=10,font=("courier",24))

frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')
button.place(relx=0.7,relwidth=0.3,relheight=1)
entry.place(relwidth=0.65,relheight=1)
lower_frame.place(relx=0.5,rely=0.35,relwidth=0.75,relheight=0.55,anchor='n')
canvas.pack()
label.place(relwidth=1,relheight=1)
root.mainloop()
