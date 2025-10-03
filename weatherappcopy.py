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
root.configure(bg="#57adff")
root.resizable(False, False)

# Icon
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)

# Rounded box
Round_box = PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=110)

# Labels
Label(root, text="Temperature", font=('Helvetica', 11), fg="white", bg="#203243").place(x=50, y=120)
Label(root, text="Humidity", font=('Helvetica', 11), fg="white", bg="#203243").place(x=50, y=140)
Label(root, text="Pressure", font=('Helvetica', 11), fg="white", bg="#203243").place(x=50, y=160)
Label(root, text="Wind Speed", font=('Helvetica', 11), fg="white", bg="#203243").place(x=50, y=180)
Label(root, text="Description", font=('Helvetica', 11), fg="white", bg="#203243").place(x=50, y=200)

# Search box
Search_image = PhotoImage(file="Images/Rounded Rectangle 3.png")
Label(root, image=Search_image, bg="#57adff").place(x=270, y=120)

weat_image = PhotoImage(file="Images/Layer 7.png")
Label(root, image=weat_image, bg="#203243").place(x=290, y=127)

textfield = Entry(root, justify='center', width=15, font=('poppins', 13, 'bold'), bg="#203243", fg="white")
textfield.place(x=370, y=130)
textfield.focus()

Search_icon = PhotoImage(file="Images/Layer 6.png")
Button(root, image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243").place(x=645, y=125)

# Bottom box
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

# Bottom boxes
firstbox = PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=20)

#clock(here we will place the time)
clock=Label(root,text="2:30 pm",font=('Helvetica', 11), fg="white", bg="#203243")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=('Helvetica', 11), fg="white", bg="#203243")
timezone.place(x=700,y=20)

long_lat=Label(root,font=('Helvetica', 11), fg="white", bg="#203243")
long_lat.place(x=700,y=50)

root.mainloop()