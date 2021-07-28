################################# Python Imported Libraries ######################################
import tkinter as tk
import random
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
    self.geometry("380x180")
    self.resizable(False,False)
    container = ttk.Frame(self)
    container.grid(padx=10,pady=10,sticky='EW')
    cube_frame = CubeFrame(container).grid(row=0,column=0,sticky='NSEW')

class CubeFrame(ttk.Frame):
  def __init__(self,container):
    super().__init__(container)
    self.red_smiley = ImageTk.PhotoImage(Image.open('./images/red_smile.png'))
    self.white_smiley = ImageTk.PhotoImage(Image.open('./images/white_smile.png'))
    self.yellow_smiley = ImageTk.PhotoImage(Image.open('./images/yellow_smile.png'))
    self.colors_list = [self.red_smiley,self.white_smiley,self.yellow_smiley]

    # Red Smiley Image Labels
    self.red_smiley_1 = ttk.Button(self,image=self.red_smiley,command=lambda:self.red_smiley_1.configure(image=self.colors_list[int(random.randint(0,2))]))
    self.red_smiley_1.grid(row=0,column=0)
    self.red_smiley_2 = ttk.Button(self,image=self.red_smiley,command=lambda:self.red_smiley_2.configure(image=self.colors_list[int(random.randint(0,2))]))
    self.red_smiley_2.grid(row=0,column=1)
    self.red_smiley_3 = ttk.Button(self,image=self.red_smiley,command=lambda:self.red_smiley_3.configure(image=self.colors_list[int(random.randint(0,2))]))
    self.red_smiley_3.grid(row=0,column=2)

    # White Smiley Image Labels
    self.white_smiley_1 = ttk.Button(self,image=self.white_smiley,command=lambda:self.white_smiley_1.configure(image=self.colors_list[int(random.randint(0,2))]))
    self.white_smiley_1.grid(row=1,column=0)
    self.white_smiley_2 = ttk.Button(self,image=self.white_smiley,command=lambda:self.white_smiley_2.configure(image=self.colors_list[int(random.randint(0,2))]))
    self.white_smiley_2.grid(row=1,column=1)
    self.white_smiley_3 = ttk.Button(self,image=self.white_smiley,command=lambda:self.white_smiley_3.configure(image=self.colors_list[int(random.randint(0,2))]))
    self.white_smiley_3.grid(row=1,column=2)

    # Yellow Smiley Image Labels
    self.yellow_smiley_1 = ttk.Button(self,image=self.yellow_smiley,command=lambda:self.yellow_smiley_1.configure(image=self.colors_list[int(random.randint(0,2))]))
    self.yellow_smiley_1.grid(row=2,column=0)
    self.yellow_smiley_2 = ttk.Button(self,image=self.yellow_smiley,command=lambda:self.yellow_smiley_2.configure(image=self.colors_list[int(random.randint(0,2))]))
    self.yellow_smiley_2.grid(row=2,column=1)
    self.yellow_smiley_3 = ttk.Button(self,image=self.yellow_smiley,command=lambda:self.yellow_smiley_3.configure(image=self.colors_list[int(random.randint(0,2))]))
    self.yellow_smiley_3.grid(row=2,column=2)

    # Image Label Buttons
    self.row_one_button = ttk.Button(self,text='Change Row 1',command=self.change_row_one).grid(row=0,column=3,sticky='WE')
    self.row_two_button = ttk.Button(self,text='Change Row 2',command=self.change_row_two).grid(row=1,column=3,sticky='WE')
    self.row_three_button = ttk.Button(self,text='Change Row 3',command=self.change_row_three).grid(row=2,column=3,sticky='WE')

    # Set padx & pady Spacing for Each Child TK Object
    for child in self.winfo_children():
      child.grid_configure(padx=5, pady=5)

  # Change Entire Row One Image Buttons
  def change_row_one(self):
    random_color = random.randint(0,2)
    self.red_smiley_1.configure(image=self.colors_list[random_color])
    self.red_smiley_2.configure(image=self.colors_list[random_color])
    self.red_smiley_3.configure(image=self.colors_list[random_color])

  # Change Entire Row Two Image Buttons
  def change_row_two(self):
    random_color = random.randint(0,2)
    self.white_smiley_1.configure(image=self.colors_list[random_color])
    self.white_smiley_2.configure(image=self.colors_list[random_color])
    self.white_smiley_3.configure(image=self.colors_list[random_color])

  # Change Entire Row Three Image Buttons
  def change_row_three(self):
    random_color = random.randint(0,2)
    self.yellow_smiley_1.configure(image=self.colors_list[random_color])
    self.yellow_smiley_2.configure(image=self.colors_list[random_color])
    self.yellow_smiley_3.configure(image=self.colors_list[random_color])

################################# Python Code ##############################################
cube = Cube()
cube.mainloop()