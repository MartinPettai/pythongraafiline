from tkinter import *

#akna seaded
aken = Tk()
aken.title("Martin")
aken.configure(background='black')
aken.geometry("300x100+100+100")
aken.minsize(200,100)
aken.maxsize(800, 400)
aken.resizable(0,0)

#tekst
tekst=Label(aken, text="Nimi: Martin Pettai", foreground="red", background="black", font="Tahoma 16 bold italic").pack()

tekst=Label(aken, text="rühm: IT21", foreground="red", background="black", font="Tahoma 16 bold italic").pack()


tekst=Label(aken, text="2022", foreground="red", background="black", font="Tahoma 16 bold italic").pack()



aken.mainloop()