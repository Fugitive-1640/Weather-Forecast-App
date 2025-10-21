from tkinter import *
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#202731")
root.resizable(False, False)

def getWeather():
    city = textfeild.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    try:
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lat=location.latitude, lng=location.longitude)
        timezone.config(text=result)
        long_lat.config(text=f"{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)

        # OpenWeatherMap API
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(weather_url)
        weather_data = response.json()

        if weather_data.get("cod") != 200:
            messagebox.showerror("Error", weather_data.get("message", "Failed to retrieve data"))
            return

        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        pressure = weather_data["main"]["pressure"]
        wind = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"]

        # Update labels
        t.config(text=f"{temp} °C")
        h.config(text=f"{humidity} %")
        p.config(text=f"{pressure} hPa")
        w.config(text=f"{wind} m/s")
        d.config(text=description.capitalize())

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

        
#icon
image_icon = PhotoImage(file="D:\SHYLESH\Weather-Forecast-App\OpenWeather 5 day API\Images\logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="D:\SHYLESH\Weather-Forecast-App\OpenWeather 5 day API\Images\Rounded Rectangle 1.png")
Label(root, image=Round_box, bg="#202731").place(x=30, y=60)

#label
label1 = Label(root, text="Temperature", font=("Helvetica", 11), fg="#323661", bg="#aad1c8")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=("Helvetica", 11), fg="#323661", bg="#aad1c8")
label2.place(x=50, y=140)

label3 = Label(root, text="Wind Speed", font=("Helvetica", 11), fg="#323661", bg="#aad1c8")
label3.place(x=50, y=160)

label4 = Label(root, text="Pressure", font=("Helvetica", 11), fg="#323661", bg="#aad1c8")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=("Helvetica", 11), fg="#323661", bg="#aad1c8")
label5.place(x=50, y=200)

#Search box

Search_image=PhotoImage(file="D:\SHYLESH\Weather-Forecast-App\OpenWeather 5 day API\Images\Rounded Rectangle 3.png")
myimage=Label(root,image=Search_image,bg="#202731")
myimage.place(x=270,y=122)

weather_image=PhotoImage(file="D:\SHYLESH\Weather-Forecast-App\OpenWeather 5 day API\Images\Layer 7.png")
weatherimage=Label(root,image=weather_image,bg="#333c4c")
weatherimage.place(x=290,y=127)

textfeild=Entry(root,justify="center",width=15,font=("poppins", 25,"bold"),bg="#333c4c",border=0, fg="white")
textfeild.place(x=370,y=130)

Search_icon=PhotoImage(file="D:\SHYLESH\Weather-Forecast-App\OpenWeather 5 day API\Images\Layer 6.png")
myimage=Button(root,image=Search_icon,borderwidth=0,cursor="hand2",bg="#333c4c",command=getWeather)
myimage.place(x=640,y=135)

#Bottom Box

frame=Frame(root,width=900,height=180,bg="#7094d4")
frame.pack(side=BOTTOM)

#Boxes
firstbox_img = PhotoImage(file="D:\SHYLESH\Weather-Forecast-App\OpenWeather 5 day API\Images\Rounded Rectangle 2.png")
secondbox_img = PhotoImage(file="D:\SHYLESH\Weather-Forecast-App\OpenWeather 5 day API\Images\Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox_img, bg="#7094d4").place(x=30, y=20)
Label(frame, image=secondbox_img, bg="#7094d4").place(x=300, y=30)
Label(frame, image=secondbox_img, bg="#7094d4").place(x=400, y=30)
Label(frame, image=secondbox_img, bg="#7094d4").place(x=500, y=30)
Label(frame, image=secondbox_img, bg="#7094d4").place(x=600, y=30)

#clock

clock=Label(root,text= "Clock", font=("Helvetica", 20),bg="#202731",fg="white")
clock.place(x=30,y=20)

#timezone

timezone=Label(root,font=("Helvetica", 20),bg="#202731",fg="white")
timezone.place(x=500,y=20)

long_lat=Label(root,font=("Helvetica", 10),bg="#202731",fg="white")
long_lat.place(x=500,y=50)

#thpwd

t=Label(frame,font=("Helvetica", 10),bg="#333c4c",fg="white")
t.place(x=150,y=120)

h=Label(frame,font=("Helvetica", 10),bg="#333c4c",fg="white")
h.place(x=150,y=140)

p=Label(frame,font=("Helvetica", 10),bg="#333c4c",fg="white")
p.place(x=150,y=160)

w=Label(frame,font=("Helvetica", 10),bg="#333c4c",fg="white")
w.place(x=150,y=180)

d=Label(frame,font=("Helvetica", 10),bg="#333c4c",fg="white")
d.place(x=150,y=200)

#first cell

firstframe=Frame(root,width=230,height=132,bg="red")
firstframe.place(x=35,y=315)

firstimage=Label(firstframe,bg="#323661")
firstimage.place(x=1,y=15)

day1=Label(firstframe,font=("Helvetica", 10),bg="#323661",fg="white")
day1.place(x=100,y=5)

day1temp=Label(firstframe,font=("Helvetica", 10),bg="#323661",fg="white")
day1temp.place(x=100,y=50)

#second cell

secondframe=Frame(root,width=70,height=115,bg="red")
secondframe.place(x=305,y=325)

secondimage=Label(secondframe,bg="#eeefea")
secondimage.place(x=7,y=25)

day2=Label(secondframe,font=("Helvetica", 10),bg="#eeefea",fg="white")
day2.place(x=10,y=5)

day2temp=Label(secondframe,font=("Helvetica", 10),bg="#eeefea",fg="white")
day2temp.place(x=2,y=70)

#third cell

thirdframe=Frame(root,width=70,height=115,bg="red")
thirdframe.place(x=405,y=325)           

thirdimage=Label(thirdframe,bg="#eeefea")
thirdimage.place(x=7,y=25)

day3=Label(thirdframe,font=("Helvetica", 10),bg="#eeefea",fg="white")
day3.place(x=10,y=5)

day3temp=Label(thirdframe,font=("Helvetica", 10),bg="#eeefea",fg="white")
day3temp.place(x=2,y=70)

# Fourth cell

fourthframe=Frame(root,width=70,height=115,bg="red")
fourthframe.place(x=505,y=325)           

fourthimage=Label(fourthframe,bg="#eeefea")
fourthimage.place(x=7,y=25)

day4=Label(fourthframe,font=("Helvetica", 10),bg="#eeefea",fg="white")
day4.place(x=10,y=5)

day4temp=Label(fourthframe,font=("Helvetica", 10),bg="#eeefea",fg="white")
day4temp.place(x=2,y=70)

# Fifth cell

fifthframe=Frame(root,width=70,height=115,bg="red")
fifthframe.place(x=605,y=325)           

fifthimage=Label(fifthframe,bg="#eeefea")
fifthimage.place(x=7,y=25)

day5=Label(fifthframe,font=("Helvetica", 10),bg="#eeefea",fg="white")
day5.place(x=10,y=5)

day5temp=Label(fifthframe,font=("Helvetica", 10),bg="#eeefea",fg="white")
day5temp.place(x=2,y=70)



root.mainloop()