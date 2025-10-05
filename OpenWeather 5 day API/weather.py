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
myimage=Button(root,image=Search_icon,borderwidth=0,cursor="hand2",bg="#333c4c")
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




root.mainloop()