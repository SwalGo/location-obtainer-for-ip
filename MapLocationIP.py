import geocoder
import tkinter as tk
import tkinter
from tkinter import *
import folium
import webbrowser
g=geocoder.ip('120.20.225.238')
def exeuc():
 myAddress=g.latlng
 print(myAddress)
 my_map1=folium.Map(location=myAddress,zoom_start=15)
 folium.CircleMarker(location=myAddress,radius=50).add_to(my_map1)
 folium.Marker(myAddress,popup=myAddress).add_to(my_map1)
 my_map1.save("myMap.html")
 def callback(url):
     webbrowser.open_new_tab(url)
 #newwin=tkinter.Tk()
 win.title('Information')
 win.geometry('300x300')
 btn.destroy()
 #Toplevel(newwin)
 Label(win,text='Information')
 var=StringVar()
 label=Label(win,textvariable=var,relief=FLAT)
 var.set("Latitude and Longitude:"+str(myAddress))
 link=Label(win,text="Location",fg="blue",cursor='hand2')
 link.pack()
 link.bind("<Button-1>",lambda e:
 callback("myMap.html"))
 label.pack()
 win.mainloop()
win=tkinter.Tk()
win.title('ALERT')
win.geometry('300x300')
photobutn=PhotoImage(file='button.png')
btn=Button(win,text='ALERT',bd='5',bg='red',image=photobutn,command=exeuc)
btn.pack(side='top')
win.mainloop()

