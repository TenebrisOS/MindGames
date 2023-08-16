import tkinter
import customtkinter as ctk
import webbrowser
import json
import random
from PIL import ImageTk, Image
import cv2
import time

#region Chimp
with open('data.json') as f:
    data = json.load(f)


buttn_list = []

level = data['CHIMP_TEST_LEVEL']
clickedList = []

data["CHIMP_TEST_LEVEL"] = 1
with open("data.json", "w") as jsonFile:
    json.dump(data, jsonFile)


def AddToList(buttonNumb):
    buttn_list[buttonNumb-1].destroy()
    clickedList.append(buttonNumb)
    if len(clickedList) == 1:
        return
    else:
        if check_order(lst=clickedList):
            level = data['CHIMP_TEST_LEVEL']
            if len(clickedList) == level + 3:
                data["CHIMP_TEST_LEVEL"] = level + 1
                with open("data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                create_buttons()
            else:
                return
        else:
            root.destroy()


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
        button_bbox = (x_coord, y_coord, x_coord +
                       button_width, y_coord + button_height)
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
    level = data['CHIMP_TEST_LEVEL']
    # cap.release()
    canvasMenu.destroy()
    chimpCanvas = ctk.CTkCanvas(root, width=640, height=360)
    chimpCanvas.pack()

    for numb in range(level + 3):
        numb1 = numb + 1
        print(numb1)
        buttn_list.append(None)
        buttn_list[numb] = ctk.CTkButton(chimpCanvas, text=str(
            numb1), width=50, height=50, command=lambda num=numb1: AddToList(buttonNumb=num))
        x_coord, y_coord = generate_random_position(buttn_list[numb])
        buttn_list[numb].place(x=x_coord, y=y_coord)
        button_positions.append(
            (x_coord, y_coord, x_coord + buttn_list[numb].winfo_reqwidth(), y_coord + buttn_list[numb].winfo_reqheight()))


def EnterChimpTest():
    create_buttons()

    for i in buttn_list:
        print('Test: ' + i.__repr__())
#endregion
def EnterAimTrainer():
    create_buttons()

    for i in buttn_list:
        print('Test: ' + i.__repr__())


def EnterReactionTest():

    canvasMenu.destroy()
    reactionCanvas = ctk.CTkCanvas(root, width=640, height=360)
    reactionCanvas.pack()

    def calculateReactionTime(start_time):
            reactionCanvas.destroy()
            reactionCanvas = ctk.CTkCanvas(root, width=640, height=360)
            reactionCanvas.pack()
            end_time = time.time()
            elapsed_time = end_time - start_time
            label = ctk.CTkLabel(reactionCanvas, text=("Reaction Time : " + str(elapsed_time)),
                                     text_color="black", font=('arial', 20))
            label.pack()
            return elapsed_time

    def f():
        start_time = time.time()
        mainbutton = ctk.CTkButton(reactionCanvas, text="CLICK !!", width=640, height=360, command=lambda : calculateReactionTime(start_time=start_time))
        mainbutton.pack()


    label = ctk.CTkLabel(reactionCanvas, text=("Wait for the button to appear"),
                                 text_color="black", font=('arial', 40))
    label.pack()
    random_integer = random.randint(5, 10)
    root.after(2000, f)
    

    
        


# region BG
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("640x360")
root.minsize(640, 360)
root.maxsize(640, 360)
root.title("MindGames")
root.iconbitmap("icon.ico")
canvasMenu = ctk.CTkCanvas(root, width=640, height=360)
canvasMenu.pack()
# cap = cv2.VideoCapture('bg.mp4')
ChimpTest = ctk.CTkButton(canvasMenu, text="ChimpTest",
                          width=80, height=80, command=EnterChimpTest)
ChimpTest.place(x=100, y=100)
ChimpTest.lift()
ReactionTime = ctk.CTkButton(
    canvasMenu, text="ReactionTime", width=80, height=80, command=EnterReactionTest)
ReactionTime.place(x=300, y=100)
ReactionTime.lift()
AimTrainer = ctk.CTkButton(
    canvasMenu, text="AimTrainer", width=80, height=80, command=EnterReactionTest)
AimTrainer.place(x=500, y=100)
AimTrainer.lift()
# buttons = {}
button_positions = []
# while cap.isOpened():
#    # read next frame
#    ret, frame = cap.read()
#    if not ret:
#        break
#    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#    image = Image.fromarray(image)
#    image = image.resize((640, 360), Image.LANCZOS)
#    photo = ImageTk.PhotoImage(image)
#    canvas.create_image(0, 0, image=photo, anchor="nw")
#    root.update()
# endregion

root.mainloop()
