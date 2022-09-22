import tkinter
import tkintermapview
import phonenumbers
import opencage
from api_key import api_key
from phonenumbers import geocoder
from phonenumbers import carrier

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from opencage.geocoder import OpenCageGeocode

root = tkinter.Tk()
root.geometry("500x500")

phone_tracker_label = Label(text="Phone Number Location Trackerr")
phone_tracker_label.pack()

def get_tracked_location():
    num = phone_number.get("1.0",END)
    try:
        target_num = phonenumbers.parse(num)
    except:
        messagebox.showerror("Error","Phone number input is empty")
    target_location = geocoder.description_for_number(target_num,"en")
    phone_isp = carrier.name_for_number(target_num,"en")

    open_cager = OpenCageGeocode(api_key)
    query = str(target_location)
    results = open_cager.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    map_label = LabelFrame(root)
    map_label.pack(pady=20)
    map_widget = tkintermapview.TkinterMapView(map_label,width=450,height=450,corner_radius=0)

    map_widget.set_position(lat,lng)
    map_widget.set_marker(lat,lng,text="Phone Location")
    map_widget.set_zoom(10)
    map_widget.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
    map_widget.pack()

    addr = tkintermapview.convert_coordinates_to_address(lat,lng)

    result.insert(END,"The country of this number is: "+target_location)
    result.insert(END,"\n The  Sim Card of this number is: "+phone_isp)
    result.insert(END,"\n Latitude : "+str(lat))
    result.insert(END,"\n Longitude : "+str(lng))
    result.insert(END,"\n Street Adress  is: "+addr.street)
    result.insert(END,"\n City Adress is: "+addr.city)
    result.insert(END,"\n Postal code is :"+addr.postal)


phone_number = Text(height=1)
phone_number.pack()
style = Style()
style.configure("TButton",font=('sans-serif',20,'bold'),borderwidth='4' )
style.map('TButton',foreground=[('active','!disabled','green')],
                     background=[('active','black')])
button = Button(text="Track", command=get_tracked_location)
button.pack(pady=10,padx=100)
result = Text(height=7)
result.pack()
root.mainloop()
