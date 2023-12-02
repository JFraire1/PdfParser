from parsing import text
from tkinter import * #main way to import.

root = Tk()  #first thing you create -- root widget -- before anything else
root.geometry("500x450")

myLabel = Label(root, text="PDF Parser", font=("Arial", 20)) #label
myLabel2 = Label(root, text=text, font=("Arial", 15), wraplength=300, justify=LEFT, padx=3, pady=2) #label
'''
myButton = Button(root, text="Open PDF", padx = 30)
myButton2 = Button(root, text="Autofill", padx = 30)
myButton3 = Button(root, text="Save", padx = 30)
myButton4 = Button(root, text="Save As", padx = 30)
myButton5 = Button(root, text="Quit", padx = 30)
'''

#^^ overall 2 step process -- define widget, create widget ^^

#myLabel.pack() #packing it into root "storage widget" in order to output

myLabel.grid(row=0, column=1)
myLabel2.grid(row=1, column=1)
'''
myButton.grid(row=2, column =1)
myButton2.grid(row=2, column =2)
myButton3.grid(row=2, column =3)
myButton4.grid(row=2, column =4)
myButton5.grid(row=2, column =5)
'''



root.mainloop() #displays