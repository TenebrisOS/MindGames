import tkinter
import customtkinter as ctk
import webbrowser
import json
import random
from PIL import ImageTk, Image
import cv2

with open('C:/Users/Samy Lamlih/Documents/code/py/MindGames/data.json') as f:
   data = json.load(f)

level = data['LEVEL']
clickedList = []
clickedList.clear()
#region Buttons Edit

def AddToList(buttonNumb):
    buttons[buttonNumb - 3].destroy()
    clickedList.append(buttonNumb)
    print(clickedList)
    if clickedList == [1] :
        return
    else :
        i = check_order(lst= clickedList)
        if i == False :
            clickedList.clear()
            root.destroy()
        elif i == True :
            return

def check_order(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            print("The list is not in order!")
            return False
        print("The list is in order.")
        return True

def generate_random_position(button):
    button.lift()
    button_width = button.winfo_reqwidth()
    button_height = button.winfo_reqheight()
    x_min = 0
    x_max = root.winfo_width() - button_width
    y_min = 0
    y_max = root.winfo_height() - button_height
    while True:
        x_coord = random.randint(x_min, x_max)
        y_coord = random.randint(y_min, y_max)
        button_bbox = (x_coord, y_coord, x_coord + button_width, y_coord + button_height)
        overlapping = False
        for other_button_bbox in button_positions:
            if intersect(button_bbox, other_button_bbox):
                overlapping = True
                break
        if not overlapping:
            return x_coord, y_coord

def intersect(bbox1, bbox2):
    x1, y1, x2, y2 = bbox1
    x3, y3, x4, y4 = bbox2
    return not (x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1)

def create_buttons():
    cap.release()
    PlayButton.destroy()
    for numb in range(level + 3) :
        button = numb + 1
        buttons[button] = ctk.CTkButton(canvas, text=numb+1, width=50, height=50, command=lambda:AddToList(buttonNumb=button))
        x_coord, y_coord = generate_random_position(buttons[button])
        buttons[button].place(x=x_coord, y=y_coord)
        button_positions.append((x_coord, y_coord, x_coord + buttons[button].winfo_reqwidth(), y_coord + buttons[button].winfo_reqheight()))

def EnterGameplayScene() :
    create_buttons()

#endregion

#region BG
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("640x360")
root.minsize(640, 360)
root.maxsize(640, 360)
root.title("MindGames")
root.iconbitmap("icon.ico")
canvas = ctk.CTkCanvas(root, width=640, height=360)
canvas.pack()
cap = cv2.VideoCapture('bg.mp4')
PlayButton = ctk.CTkButton(canvas, text="Play", width=120, height=32, command=EnterGameplayScene)
PlayButton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
PlayButton.lift()
buttons = {}
button_positions = []
while cap.isOpened():
    # read next frame
    ret, frame = cap.read()
    if not ret:
        break
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = image.resize((640, 360), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=photo, anchor="nw")
    root.update()
#endregion

root.mainloop()