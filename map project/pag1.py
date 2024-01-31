from tkinter import *
from tkintermapview import TkinterMapView
root=Tk()
root.geometry ('880x450')
root.title('MAP-OF-MIDDLE-EAST[MAP-of-JORDAN]')
root.iconbitmap('sumby.jpeg')
#root.configure(background="white")

def Irbid():
    map=TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(32.556863820511275, 35.8463807028747)
    map.set_zoom(15)
    Irbid=map.set_marker(32.556863820511275, 35.8463807028747)
    marker.set_text('Irbid')
def Jerash():
    map=TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(32.2740816691881, 35.8955117186694)
    map.set_zoom(15)
    Jerash=map.set_marker(32.2740816691881, 35.8955117186694)
    marker.set_text('Jerash')
def Ajloun():
    map=TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(32.33339404001871, 35.75173319924381)
    map.set_zoom(15)
    Ajloun=map.set_marker(32.33339404001871, 35.75173319924381)
    marker.set_text('Ajloun')
def Mafraq():
    map=TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(32.34302696197689, 36.20161358909079)
    map.set_zoom(15)
    Mafraq=map.set_marker(32.34302696197689, 36.20161358909079)
    marker.set_text('Mafraq')    
def alzarqa():
    map=TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(32.0639037146167, 36.093186577149865)
    map.set_zoom(15)
    alzarqa=map.set_marker(32.0639037146167, 36.093186577149865)
    marker.set_text('alzarqa') 
def Amman():
    map=TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(31.676527403732713, 36.668674768234865)
    map.set_zoom(15)
    Amman=map.set_marker(31.676527403732713, 36.668674768234865)
    marker.set_text('Amman') 
def Balqa():
    map=TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(32.03573261156529, 35.72601676142076)
    map.set_zoom(15)
    Balqa=map.set_marker(32.03573261156529, 35.72601676142076)
    marker.set_text('Balqa') 
def Madaba():
    map=TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(31.719693160122652, 35.792908216592714)
    map.set_zoom(15)
    Madaba=map.set_marker(31.719693160122652, 35.792908216592714)
    marker.set_text('Madaba')
def Karak():
    map=TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(31.185263861195068, 35.70385564169898)
    map.set_zoom(15)
    Karak=map.set_marker(31.185263861195068, 35.70385564169898)
    marker.set_text('Karak')    
def Tafila():
    map=TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(30.834880963543416, 35.614138677942364)
    map.set_zoom(15)
    Tafila=map.set_marker(30.834880963543416, 35.614138677942364)
    marker.set_text('Tafila')    
def Maan():
    map=TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(30.191579721832447, 35.72119052786714)
    map.set_zoom(15)
    Maan=map.set_marker(30.191579721832447, 35.72119052786714)
    marker.set_text('Maan')    
def Aqaba():
    map=TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(29.533535163879026, 35.006859010634884)
    map.set_zoom(15)
    Aqaba=map.set_marker(29.533535163879026, 35.006859010634884)
    marker.set_text('Aqaba')    
      
def cu():
    country=En.get()
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_address(country,marker=True) 
#========Title1========
Title1=Label(root,
             text='MAP-OF-MIDDLE-EAST',
             fg='white',
             bg='black',
             font=('Tajawal',18),)
Title1.pack(fill=X)
#========logo========
icon = PhotoImage(file='logo.jpeg')
root.iconphoto(True, icon)


#logo= PhotoImage (file='sumby.jpeg')
#lab_log=Label(root,image=logo,bd=0,bg='white')
#lab_log.place(x=30,y=40)

#========Label+Enyer+button========
l=Label(root,text='country:',font=('Tajawal 13'),fg='black',bg='white')
l.place(x=10,y=260)
En=Entry(root,font=('Tajawal ',14),width=10,bd=2,relief=GROOVE)
En.place(x=140,y=260)
b=Button(root,text='Git country',
          bg='black',fg='white',bd=1,
          relief=SOLID ,width=10,cursor='hand2',command=cu)
b.place(x=260,y=260)
#========pharmacy============

b1=Button(
    root,text='Irbid',
    cursor='hand2',bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal 12'),width=13,command=Irbid
)
b1.place(x=10,y=300)
b2=Button(
    root,text='Jerash',cursor='hand2',
    bg='white',fg='black',bd=1,
    relief=SOLID,font=('Tajawal 12'),width=13,command=Jerash

)
b2.place(x=130,y=300)
b3=Button(
    root,text='Ajloun',
    cursor='hand2',
    bg='white',fg='black',bd=1,relief=SOLID
    ,font=('Tajawal 12'),width=13,command=Ajloun

)
b3.place(x=250,y=300)
b4=Button(
    root,text='Mafraq',
    cursor='hand2',
    bg='white',fg='black',
    bd=1,
    relief=SOLID
    ,font=('Tajawal 12'),
    width=13,command=Mafraq
)
b4.place(x=10,y=340)
b5=Button(
    root,text='alzarqa',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID
    ,font=('Tajawal 12'),width=13,command=alzarqa
)
b5.place(x=130,y=340)
b6=Button(
    root,text='Amman Capital ',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,font=('Tajawal 12'),width=13,command=Amman
)
b6.place(x=250,y=340)
b7=Button(
    root,text='Balqa',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,font=('Tajawal 12'),width=13,command=Balqa
)
b7.place(x=10,y=380)
b8=Button(
    root,text='Madaba',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,font=('Tajawal 12'),width=13,command=Madaba
)
b8.place(x=130,y=380)
b9=Button(
    root,text='Tafila',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,font=('Tajawal 12'),width=13,command=Tafila
)
b9.place(x=250,y=380)

b10=Button(
    root,text='Karak',cursor='hand2',
    bg='white',fg='black',bd=1,
    relief=SOLID,font=('Tajawal 12'),width=13,command=Karak

)
b10.place(x=10,y=420)
b11=Button(
    root,text='Maan',
    cursor='hand2',
    bg='white',fg='black',bd=1,relief=SOLID
    ,font=('Tajawal 12'),width=13,command=Maan

)
b11.place(x=130,y=420)
b12=Button(
    root,text='Aqaba',
    cursor='hand2',
    bg='white',fg='black',
    bd=1,
    relief=SOLID
    ,font=('Tajawal 12'),
    width=13,command=Aqaba
)
b12.place(x=250,y=420)
#===========map==========
map=TkinterMapView(root,width=500,height=400,corner_radius=0)
map.place(x=370,y=45)
root.mainloop()

