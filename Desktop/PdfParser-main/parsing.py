import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
from tkPDFViewer import tkPDFViewer as pdf
import PyPDF2

def import_file(root):
    file_pdf = filedialog.askopenfilename()
    v1 = pdf.ShowPdf()  # creating object of ShowPDF from tkPDFVIEWER
    v2 = v1.pdf_view(root,
                     pdf_location=file_pdf,
                     width=100, height=150)
    v2.pack()
    root.mainloop()
    print("Your file: ", file_pdf)
def command_button(root):
    open_file = Button(root, text = "Open File", command=lambda:import_file(root))
    open_file.place(x= 20, y=50)
    exit_program = Button(root, text = "Exit Program", command = lambda: exit())
    exit_program.place(x = 20, y=100)
    #edit_file = Button(root, text = "Edit File", command = lambda:)
    # i wanted to create an edit file button that appeared after opening a file
    # which would allow me to change the text on said file.
    return root


def text_box(root):
    my_text = Text(root, width=60, height=25)
    my_text.pack(pady=20)


def main():
    root = tk.Tk()  # initialize once, multiple times will not work. best to do it in main
    root.geometry("1000x900")
    command_button(root)
    root.mainloop()

if __name__=="__main__":
    main()








