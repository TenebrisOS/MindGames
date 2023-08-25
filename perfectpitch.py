import customtkinter as ctk
import threading
from playsound import playsound
import random


def playPitch(pitch):
    play_audio("allData/assets/SoundEffects/Pitches/" + pitch + '.mp3') 

def play_audio(file_path):
    playsound(file_path)


def update_progress(progressbar, completedQst, nbrquestion):
    mlt = 100 / nbrquestion
    progressbar.set(completedQst)


def CheckAnswer(choice, sound, button):
    if choice == sound:
        print('good job!')
        button.configure(fg_color='green')
    else:
        print('try again :(')
        button.configure(fg_color='red')

def EnterPitchTest(mainMenu, root):
    string_list = ['c', 'd', 'e']
    rdmLetter = random.choice(string_list)
    int_list = ['3', '5', '6']
    rdmInt = random.choice(int_list)
    for canvas in mainMenu:
        if canvas is not None:
            canvas.destroy()
    gameCanvas = ctk.CTkCanvas(root, width=640, height=360)
    gameCanvas.pack()
    playSoundBtn = ctk.CTkButton(gameCanvas, text="Hear Sound",
                        width=80, height=40, font=('arial', 15), command=lambda: playPitch(rdmLetter + str(rdmInt)), fg_color='black', text_color='white')
    playSoundBtn.place(relx=0.5, rely=0.3, anchor="center")
    title = ctk.CTkLabel(gameCanvas, text="Perfect Pitch Test",
                         fg_color="transparent", font=('arial', 30), text_color='black', anchor=ctk.CENTER)
    title.place(relx=0.5, rely=0.15, anchor="center")
    completedQst = 0
    progressbar = ctk.CTkProgressBar(
        gameCanvas, orientation="horizontal", width=100, mode="determinate")
    progressbar.place(relx=0.2, rely=0.2, anchor="center")
    progressbar.set(0)
    cBtn = ctk.CTkButton(gameCanvas, text="C",
                        width=40, height=40, font=('arial', 20))
    cBtn.place(relx=0.43, rely=0.5, anchor="center")
    cBtn.bind("<Button-1>", lambda event: CheckAnswer('c', rdmLetter, cBtn))
    dBtn = ctk.CTkButton(gameCanvas, text="D",
                        width=40, height=40, font=('arial', 20))
    dBtn.place(relx=0.5, rely=0.5, anchor="center")
    dBtn.bind("<Button-1>", lambda event: CheckAnswer('d', rdmLetter, dBtn))
    eBtn = ctk.CTkButton(gameCanvas, text="E",
                        width=40, height=40, font=('arial', 20))
    eBtn.place(relx=0.57, rely=0.5, anchor="center")
    eBtn.bind("<Button-1>", lambda event: CheckAnswer('e', rdmLetter, eBtn))
    #playSoundBtn = ctk.CTkButton(gameCanvas, text="Hear Sound",
    #                    width=80, height=40, font=('arial', 15), command=lambda: playPitch(rdmLetter + str(rdmInt)), fg_color='black', text_color='white')
    #playSoundBtn.place(relx=0.5, rely=0.3, anchor="center")
    #playSoundBtn = ctk.CTkButton(gameCanvas, text="Hear Sound",
    #                    width=80, height=40, font=('arial', 15), command=lambda: playPitch(rdmLetter + str(rdmInt)), fg_color='black', text_color='white')
    #playSoundBtn.place(relx=0.5, rely=0.3, anchor="center")
    # def start_thread(function):
    #    thread = threading.Thread(target=function)
    #    thread.start()

    # start_thread(update_progress)
    # text562 = ctk.CTkLabel(gameCanvas, text=str(nbrquestion),
    #                    fg_color="transparent", font=('arial', 20), text_color='black')
    # text562.pack()


def pitchMenu(mainMenu, root):
    for i in range(len(mainMenu)):
        if mainMenu[i] is not None:
            mainMenu[i].destroy()
            print('destoyed :', mainMenu[i])
    pitchcanvas = ctk.CTkCanvas(root, width=640, height=360)
    pitchcanvas.pack()
    mainMenu.append(pitchcanvas)
    title = ctk.CTkLabel(pitchcanvas, text="Perfect Pitch Quiz",
                         fg_color="transparent", font=('arial', 30), text_color='black', anchor=ctk.CENTER)
    title.place(relx=0.5, rely=0.23, anchor="center")
    text = ctk.CTkLabel(pitchcanvas, text="In this exercise, you will hear a single note.",
                        fg_color="transparent", font=('arial', 20), text_color='black')
    text.place(relx=0.5, rely=0.35, anchor="center")
    text2 = ctk.CTkLabel(pitchcanvas, text="Your goal is to identify the name of the note.",
                         fg_color="transparent", font=('arial', 20), text_color='black')
    text2.place(relx=0.5, rely=0.43, anchor="center")
    text3 = ctk.CTkLabel(pitchcanvas, text="For best results, practice a little bit every day.",
                         fg_color="transparent", font=('arial', 20), text_color='black')
    text3.place(relx=0.5, rely=0.51, anchor="center")
    notes = ctk.CTkLabel(pitchcanvas, text="Notes :",
                         fg_color="transparent", font=('arial', 20), text_color='black')
    notes.place(x=140, y=209)
    optionmenu = ctk.CTkOptionMenu(pitchcanvas, width=200, values=[
                                   "Simple (C, D, E)"], font=('arial', 20))
    optionmenu.set("Simple (C, D, E)")
    optionmenu.place(relx=0.5, rely=0.62, anchor="center")
    # questionEntry = ctk.CTkEntry(pitchcanvas, width=200, font=('arial', 20), placeholder_text='Write a Number...')

    def slider_event(flaotvalue):
        nbrquestion = int(flaotvalue)
        valueCTK.configure(text=int(flaotvalue))
        print(int(flaotvalue))

    questionEntry = ctk.CTkSlider(
        pitchcanvas, from_=0, to=20, command=slider_event)
    questionEntry.place(relx=0.5, rely=0.72, anchor="center")
    questionEntry.set(0)
    questions = ctk.CTkLabel(pitchcanvas, text="Questions :",
                             fg_color="transparent", font=('arial', 20), text_color='black')
    questions.place(x=115, y=243)
    label2 = ctk.CTkLabel(pitchcanvas, text="Leave as 0 for never-ending quiz.",
                          font=('', 15), text_color='black')
    label2.place(x=110, y=270)

    valueCTK = ctk.CTkLabel(pitchcanvas, text='',
                            fg_color="transparent", font=('arial', 20), text_color='black')
    valueCTK.place(x=450, y=243)
    prfcPitch = ctk.CTkButton(pitchcanvas, text="Start Quiz",
                              width=80, height=40, command=lambda: EnterPitchTest(mainMenu, root))
    prfcPitch.place(x=280, y=300)
