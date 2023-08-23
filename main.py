import customtkinter as ctk
from chimptest import ChimpMenu, resetLevelChimp


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
# endregion


def main():
    menu()
    root.mainloop()

def menu():
    for i in range(len(mainMenu)):
        if mainMenu[i] is not None:
            mainMenu[i].destroy()
    canvasMenu = ctk.CTkCanvas(root, width=640, height=360)
    canvasMenu.pack()
    mainMenu.append(canvasMenu)

    def buttonAction(is_chimp_test):
        canvasMenu.destroy()
        if is_chimp_test:
            ChimpMenu(root, mainMenu, gameplayMenus, menu)
            print('chimp')
        # if bool is False:
        #     pitchMenu()

    # cap = cv2.VideoCapture('bg.mp4')
    label1 = ctk.CTkLabel(canvasMenu, text='Chimpanzee test',
                          fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    label1.place(x=100, y=120)
    ChimpTest = ctk.CTkButton(canvasMenu, text="Test",
                              width=100, height=40)
    ChimpTest.place(x=120, y=150)
    ChimpTest.lift()
    ChimpTest.bind("<Button-1>", lambda event: buttonAction(True))

    label2 = ctk.CTkLabel(canvasMenu, text='Perfect Pitch Quiz',
                          fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    label2.place(x=360, y=120)
    perfectPitch = ctk.CTkButton(canvasMenu, text="Quiz",
                                 width=100, height=40)
    perfectPitch.place(x=380, y=150)
    perfectPitch.lift()
    perfectPitch.bind("<Button-1>", lambda event: buttonAction(False))



if __name__ == "__main__":
    main()
    resetLevelChimp()
