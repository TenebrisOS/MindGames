import customtkinter as ctk
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
    title.place(relx=0.5, rely=0.3, anchor="center")
    text = ctk.CTkLabel(pitchcanvas, text="In this exercise, you will hear a single note. Your goal is to identify the name of the note. For best results, practice a little bit every day.",
                        fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    text.place(relx=0.5, rely=0.5, anchor="center")
    optionmenu = ctk.CTkOptionMenu(pitchcanvas, width=400, values=["Simple (C, D, E)"])
    optionmenu.set("Simple (C, D, E)")
    optionmenu.place(relx=0.5, rely=0.7, anchor="center")
    optionmenu2 = ctk.CTkTextbox(pitchcanvas, width=200)
    optionmenu2.place(relx=0.5, rely=0.7, anchor="center")
    #prfcPitch = ctk.CTkButton(pitchcanvas, text="Start Quiz",
    #                          width=80, height=40, command=pitchcanvas)
    #prfcPitch.place(x=280, y=200)