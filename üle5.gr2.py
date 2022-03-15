#martin pettai
#it21
#ül5
from tkinter import *
#akna seaded
aken = Tk()
aken.title('Nupud')
aken.geometry("300x200")




#funktsioonid



def arvuta():
    nimi = sisestus.get()
    #print("Tere " +nimi)
    valjund.config(text="Tere "+nimi)




#sildid
silt = Label(aken, text="Hind käibemaksuta:")
silt.grid(row=0,column=0)

valjund = Label(aken, text="Siia tuleb tervitus")
valjund.grid(row=2,columnspan=3)



#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)



#nupud
nupp1 = Button(aken, text="Tervita", width=10, command=arvuta)
nupp1.grid(row=1, column=1)

aken.mainloop()


#valikukast
var = IntVar()
valikukast = Radiobutton(aken,text="Valik 1", variable=var, value=1, command=naita_valikut)
valikukast.grid(row=1)
valikukast = Radiobutton(aken,text="Valik 2", variable=var, value=2, command=naita_valikut)
valikukast.grid(row=2)



aken.mainloop()