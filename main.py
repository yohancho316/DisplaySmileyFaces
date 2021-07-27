################################# Python Imported Libraries ######################################
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.constants import DISABLED, NORMAL
from PIL import Image, ImageTk

################################# TKinter Code #############################################
class Cube(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("John's GUI Cube Application")
    self.geometry("300x180")
    self.resizable(True,True)

    container = ttk.Frame(self)
    container.grid(padx=10,pady=10,sticky='EW')

    cube_frame = CubeFrame(container).grid(row=0,column=0,sticky='NSEW')

class CubeFrame(ttk.Frame):
  def __init__(self,container):
    super().__init__(container)
    self.red_smiley = ImageTk.PhotoImage(Image.open('./images/red_smile.png'))
    self.white_smiley = ImageTk.PhotoImage(Image.open('./images/white_smile.png'))
    self.yellow_smiley = ImageTk.PhotoImage(Image.open('./images/yellow_smile.png'))

    # Red Smiley Image Labels
    self.red_smiley_1 = ttk.Label(self,image=self.red_smiley)
    self.red_smiley_1.grid(row=0,column=0)
    self.red_smiley_2 = ttk.Label(self,image=self.red_smiley)
    self.red_smiley_2.grid(row=0,column=1)
    self.red_smiley_3 = ttk.Label(self,image=self.red_smiley)
    self.red_smiley_3.grid(row=0,column=2)

    # White Smiley Image Labels
    self.white_smiley_1 = ttk.Label(self,image=self.white_smiley)
    self.white_smiley_1.grid(row=1,column=0)
    self.white_smiley_2 = ttk.Label(self,image=self.white_smiley)
    self.white_smiley_2.grid(row=1,column=1)
    self.white_smiley_3 = ttk.Label(self,image=self.white_smiley)
    self.white_smiley_3.grid(row=1,column=2)

    # Yellow Smiley Image Labels
    self.yellow_smiley_1 = ttk.Label(self,image=self.yellow_smiley)
    self.yellow_smiley_1.grid(row=2,column=0)
    self.yellow_smiley_2 = ttk.Label(self,image=self.yellow_smiley)
    self.yellow_smiley_2.grid(row=2,column=1)
    self.yellow_smiley_3 = ttk.Label(self,image=self.yellow_smiley)
    self.yellow_smiley_3.grid(row=2,column=2)

    # Image Label Buttons
    self.row_one_button = ttk.Button(self,text='Change Row 1',command=self.change_row_one).grid(row=0,column=3,sticky='WE')
    self.row_two_button = ttk.Button(self,text='Change Row 2',command=self.change_row_two).grid(row=1,column=3,sticky='WE')
    self.row_three_button = ttk.Button(self,text='Change Row 3',command=self.change_row_three).grid(row=2,column=3,sticky='WE')

    # Set padx & pady Spacing for Each Child TK Object
    for child in self.winfo_children():
      child.grid_configure(padx=5, pady=5)

  # Change Row One Image Labels
  def change_row_one(self):
    self.red_smiley_1.configure(image=self.white_smiley)
    self.red_smiley_2.configure(image=self.white_smiley)
    self.red_smiley_3.configure(image=self.white_smiley)

  # Change Row Two Image Labels
  def change_row_two(self):
    self.white_smiley_1.configure(image=self.yellow_smiley)
    self.white_smiley_2.configure(image=self.yellow_smiley)
    self.white_smiley_3.configure(image=self.yellow_smiley)

  # Change Row Three Image Labels
  def change_row_three(self):
    self.yellow_smiley_1.configure(image=self.red_smiley)
    self.yellow_smiley_2.configure(image=self.red_smiley)
    self.yellow_smiley_3.configure(image=self.red_smiley)

################################# Python Code ##############################################
cube = Cube()
cube.mainloop()