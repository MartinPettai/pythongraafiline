#martin pettai
#it21
#ül5
from tkinter import *
#akna seaded
aken = Tk()
aken.title('Nupud')
aken.geometry("300x170")

#funktsioonid
def arvutused():
    hind = sisestus.get()
    km=var.get()/100
    hindkm=float(km)*float(hind)+float(hind)
    valjund.config(text=hindkm)
    kaibemaks=float(km)*float(hind)
    valjund2.config(text=kaibemaks)


#sildid
silt = Label(aken, text="Hind käibemaksuta:")
silt.grid(row=0,column=0)
silt = Label(aken, text="Käibemaksu määr:")
silt.grid(row=1,column=0)
silt = Label(aken, text="--------------------------------------------------------- ")
silt.grid(row=3,columnspan=2)
silt = Label(aken, text="Käibemaks:")
silt.grid(row=4,column=0)
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)
valjund2 = Label(aken, text="0.00€")
valjund2.grid(row=4,column=1)
#mingi nupp
var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=9, command=arvutused)
valikukast.grid(row=1,column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=20, command=arvutused)
valikukast.grid(row=2,column=1)

#sisestusväljad
silt = Label(aken, text="Hind käibemaksuga:")
silt.grid(row=5,column=0)
valjund = Label(aken, text="0.00€")
valjund.grid(row=5,column=1)
#nupud
nupp1 = Button(aken, text="ok", width=10, command=arvutused)
nupp1.grid(row=7, column=1)

aken.mainloop()



aken.mainloop()