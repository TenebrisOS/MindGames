import customtkinter as ctk

def EnterPitchTest(mainMenu, root):
    global gameCanvas
    for i in range(len(mainMenu)):
        if mainMenu[i] is not None:
            mainMenu[i].destroy()
    gameCanvas = ctk.CTkCanvas(root, width=640, height=360)
    gameCanvas.pack()


def pitchMenu(mainMenu, root):
    for i in range(len(mainMenu)):
        if mainMenu[i] is not None:
            mainMenu[i].destroy()
            print('destoyed :', mainMenu[i])
    pitchcanvas = ctk.CTkCanvas(root, width=640, height=360)
    pitchcanvas.pack()
    mainMenu.append(pitchcanvas)
    title = ctk.CTkLabel(pitchcanvas, text="Perfect Pitch Quiz",
                         fg_color="transparent", font=('arial', 30), text_color='black', bg_color='white', anchor=ctk.CENTER)
    title.place(relx=0.5, rely=0.23, anchor="center")
    text = ctk.CTkLabel(pitchcanvas, text="In this exercise, you will hear a single note.",
                        fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    text.place(relx=0.5, rely=0.35, anchor="center")
    text2 = ctk.CTkLabel(pitchcanvas, text="Your goal is to identify the name of the note.",
                        fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    text2.place(relx=0.5, rely=0.43, anchor="center")
    text3 = ctk.CTkLabel(pitchcanvas, text="For best results, practice a little bit every day.",
                        fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    text3.place(relx=0.5, rely=0.51, anchor="center")
    notes = ctk.CTkLabel(pitchcanvas, text="Notes :",
                        fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    notes.place(x=140, y=209)
    optionmenu = ctk.CTkOptionMenu(pitchcanvas, width=200, values=["Simple (C, D, E)"], font=('arial', 20))
    optionmenu.set("Simple (C, D, E)")
    optionmenu.place(relx=0.5, rely=0.62, anchor="center")
    optionmenu2 = ctk.CTkTextbox(pitchcanvas, height=1, width=200, font=('arial', 14))
    optionmenu2.place(relx=0.5, rely=0.72, anchor="center")
    questions = ctk.CTkLabel(pitchcanvas, text="Questions :",
                        fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    questions.place(x=115, y=243)
    prfcPitch = ctk.CTkButton(pitchcanvas, text="Start Quiz",
                              width=80, height=40, command= lambda: EnterPitchTest(mainMenu, root))
    prfcPitch.place(x=280, y=300)