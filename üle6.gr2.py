from tkinter import *
#Martin Pettai
#IT21
#ül06gr2



#akna seaded
aken = Tk()
aken.title('Joonistamine')


#lõuendi loomine
louend = Canvas(aken, width=1000, height=1000)
louend.pack()


#kujundite loomine
louend.create_rectangle(0, 0, 350, 100, fill='#1296F5', outline='#993333', width=0)

louend.create_rectangle(0, 100, 350, 110, fill='#ffffff', outline='#993333', width=0)

louend.create_rectangle(0, 110, 350, 150, fill='#000000', outline='#993333', width=0) 
louend.create_rectangle(0, 180, 350, 150, fill='#ffffff', outline='#993333', width=0)

louend.create_rectangle(0, 160, 350, 260, fill='#1296F5', outline='#993333', width=0)



aken.mainloop()
