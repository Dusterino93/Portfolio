# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:18:26 2020

@author: doand
"""


import tkinter as tk
##################################################
# How to make a window & a Label (title)

#window = tk.Tk()

#greeting = tk.Label(
   # text = "Hello, Tkinter", fg = "red", background = "#34A2FE",
   # width = 10,
  #  height = 10
#    )
#greeting.pack()

#window.mainloop()

#####################################################
# How to make buttons

#button = tk.Button(text = 'Click me!', width = 25,
                  # height = 5, bg = "blue", fg = "yellow")

#button.pack() #very important, make sure to have this or else it won't show up

#label = tk.Label(text = "Name")
#entry = tk.Entry()

#label.pack()
#entry.pack()

#entry.insert(0, "Python")
#entry.insert(0, "Real ")

#window.mainloop()

#################################################
# How to make text boxes

#window = tk.Tk()
#text_box = tk.Text()
#text_box.pack()

# to get text from a text box, you'll need to pass a start index and an end index.
# the syntax is "<line>.<char>" with line = line number and char with character number
# the rest of .get and .delete follows this concept
# for .insert, it follows the ("<line>.<char>", "String") format
# if you want to insert something on the 2nd, line, you must write ("2.0", "\nString")
# if you want to insert at end, it's better to do .insert(tk.END, "String")

#window.mainloop()

#################################################
# how to make a frame

window = tk.Tk()
frame = tk.Frame()
frame.pack()

window.mainloop()
