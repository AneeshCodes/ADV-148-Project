# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 18:38:02 2022

@author: anees
"""

from tkinter import *
import random

root=Tk()
root.title("1D List")
root.geometry("400x400")

List1 = ["Bottle", "Banana", "Apple", "Carrot", "Gorilla Glue", "Custard Apple"]
label1= Label(root, text=str(List1))
item = Label(root)

def randomList():
    randomList = random.sample(range(0,5),1)   
    item["text"] = "The chosen item number is " + str(randomList)
    

btn = Button(root, text="Generate Item", command = randomList)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
label1.place(relx=0.5, rely=0.5, anchor=CENTER)
item.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()