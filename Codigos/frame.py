from tkinter import *

ventana = Tk()

ventana.title("Hola mundo")
ventana.resizable(True,True)
#Ancho -width, Largo -height
ventana.iconbitmap("favicon.ico")
ventana.geometry("850x400")
ventana.config(bg="Cyan")

'''
frame1 = Frame()
frame1.pack()
frame1.config(bg="Red")
frame1.config(width="650",height="350")
#Borde
frame1.config(bd=12)
frame1.config(relief="groove")
frame1.config(cursor="pirate")
'''

frame1 = Frame()
#frame1.pack(side = "bottom")

'''
frame1.pack(side="right",anchor="se")
frame1.config(bg="Red")
frame1.config(width="650",height="350")
'''

frame1.pack(fill = "both", expand = "True")
frame1.config(bg="Red")
frame1.config(width="650",height="350")


ventana.mainloop()
#raiz.title("")


