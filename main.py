import customtkinter as ctk
from chimptest import resetLevelChimp, ChimpMenu
from perfectpitch import pitchMenu
# region tkinter settings
mainMenu = []
gameplayMenus = []
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("640x360")
root.minsize(640, 360)
root.maxsize(640, 360)
root.title("Mind Games")
root.iconbitmap("allData/assets/PNG/icon.ico")
# endregion

def menu():
    resetLevelChimp()
    for i in range(len(mainMenu)):
        if mainMenu[i] is not None:
            mainMenu[i].destroy()
    canvasMenu = ctk.CTkCanvas(root, width=640, height=360)
    canvasMenu.pack()
    mainMenu.append(canvasMenu)
    # cap = cv2.VideoCapture('bg.mp4')
    label1 = ctk.CTkLabel(canvasMenu, text='Chimpanzee test',
                                  fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    label1.place(x=100, y=120)
    ChimpTest = ctk.CTkButton(canvasMenu, text="Test",
                              width=100, height=40, command=ChimpMenu)
    ChimpTest.place(x=120, y=150)
    ChimpTest.lift()
    label2 = ctk.CTkLabel(canvasMenu, text='Perfect Pitch Quiz',
                                  fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    label2.place(x=360, y=120)
    perfectPitch = ctk.CTkButton(canvasMenu, text="Quiz",
                              width=100, height=40, command=pitchMenu)
    perfectPitch.place(x=380, y=150)
    perfectPitch.lift()

resetLevelChimp()
menu()
root.mainloop()
