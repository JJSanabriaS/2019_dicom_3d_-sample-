# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:06:51 2019
@author: JOHNJAIRO
"""
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog 

root = Tk(  )

def OpenFile():
    root.directory = filedialog.askdirectory()
    print (root.directory)

def demo():
    #root = tk.Tk()
    schedGraphics = tkinter
    root = schedGraphics.Tk()
    root.title("Testing GUI")
    universal_height = 606
    
    
    menu = Menu(root)
    root.config(menu=menu)
    file = Menu(menu)
    file.add_command(label = 'Escolha pasta do paciente', command = OpenFile)
    file.add_command(label = 'Exit', command = lambda:exit())
    menu.add_cascade(label = 'Pasta paciente', menu = file)

    
    nb = tkinter.ttk.Notebook(root)
    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    page1 = tkinter.ttk.Frame(nb, width= universal_height,height = (universal_height)/2)
    page2 = tkinter.ttk.Frame(nb,width = universal_height,height = (universal_height)/2)
    page3 = tkinter.ttk.Frame(nb,width = universal_height,height = (universal_height)/2)
    page4 = tkinter.ttk.Frame(nb,width = universal_height,height = (universal_height)/2)
    

    nb.add(page1, text='Tomografia-Dicom')
    nb.add(page2, text='Dentes')
    nb.add(page3, text='Face')
    nb.add(page4, text='Superposição: Tomografia/Dentes ')
#    https://www.programcreek.com/python/example/104109/tkinter.ttk.Notebook
 #   https://stackoverflow.com/questions/16514617/python-tkinter-notebook-widget
 #   https://stackoverflow.com/questions/44745297/adding-notebook-tabs-in-tkinter-how-do-i-do-it-with-a-class-based-structure

    nb.grid(row=2)

    day_label = schedGraphics.Label(page1, text="imagems Dicom:")
    day_label.pack()
    day_label.place(x=0, y=30)
    
    day_label = schedGraphics.Label(page2, text="Dentes:     ..........")
    day_label.pack()
    day_label.place(x=0, y=30)
    
    day_label = schedGraphics.Label(page3, text="Face:     ..........")
    day_label.pack()
    day_label.place(x=0, y=30)
    
    day_label = schedGraphics.Label(page4, text="Superposição   ..........")
    day_label.pack()
    day_label.place(x=0, y=30)
    
    
    
    canvas = schedGraphics.Canvas(page1,width = 900, height = universal_height)
    canvas.create_rectangle(50,500,300,600,fill = "red")
    canvas.grid()
    
    canvas = schedGraphics.Canvas(page2,width = 900, height = universal_height)
    canvas.create_rectangle(50,500,300,600,fill = "blue")
    canvas.grid()
    
    canvas = schedGraphics.Canvas(page3,width = 900, height = universal_height)
    canvas.create_rectangle(50,500,300,600,fill = "green")
    canvas.grid()
    
    canvas = schedGraphics.Canvas(page4,width = 900, height = universal_height)
    canvas.create_rectangle(50,500,300,600,fill = "black")
    canvas.grid()

    
    
    
    root.mainloop()

if __name__ == "__main__":
    demo()