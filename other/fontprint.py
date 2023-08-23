#This code wasn't made by TenebrisOS
from tkinter import font
import customtkinter as ctk
#Create an instance of tkinter frame
win = ctk.CTk()
win.geometry("750x350")
win.title('Font List')
#Create a list of font using the font-family constructor
fonts=list(font.families())
fonts.sort()
def fill_frame(frame):
   for f in fonts:
      #Create a label to display the font
      label = ctk.CTkLabel(frame,text=(f, 23),font=(f, 14)).pack()
def onFrameConfigure(canvas):
   canvas.configure(scrollregion=canvas.bbox("all"))
#Create a canvas
canvas = ctk.CTkCanvas(win,bd=1, background="white")
#Create a frame inside the canvas
frame = ctk.CTkFrame(canvas)
#Add a scrollbar
scroll_y = ctk.CTkScrollbar(win, command=canvas.yview)
canvas.configure(yscrollcommand=scroll_y.set)
scroll_y.pack(side="right", fill="y")
canvas.pack(side="left", expand=1, fill="both")
canvas.create_window((5,4), window=frame, anchor="n")
frame.bind("<Configure>", lambda e, canvas=canvas: onFrameConfigure(canvas))
fill_frame(frame)
win.mainloop()