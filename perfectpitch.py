import customtkinter as ctk
import threading
from playsound import playsound
import random
import os

def playPitch(pitch):
    audio_thread = threading.Thread(target=play_audio, args=(
        "allData/assets/SoundEffects/Pitches/" + pitch,))
    audio_thread.start()


def play_audio(file_path):
    playsound(file_path)


def update_progress(progressbar, completedQst):
    nbr = completedQst / 10
    if completedQst != 0:
        if progressbar is not None:
            progressbar.set(value=nbr)


def DisableButton(btn):
    btn.configure(state='disabled')


def CheckAnswer(choice, sound, canvas, mainMenu, pitchcanvas, btnlist, progressbar, completedQst, nbrquestion, gameplaycanvas, playSoundBtn, mainmenucanvas, selectedmode, btnpitchlist, number, checkbox, root):
    if choice == sound:
        btnpitchlist[number].configure(fg_color='green', hover=False)
        root.after(700, lambda: checkthebox(completedQst))
        def checkthebox(completedQst):
            if checkbox.get() == False:
                NextPitch(canvas, mainMenu, pitchcanvas, btnlist,
                          progressbar, completedQst, nbrquestion, gameplaycanvas, playSoundBtn, mainmenucanvas, selectedmode, checkbox, root)
            else:
                completedQst += 1
                Next(mainMenu, canvas, pitchcanvas,
                        btnlist, nbrquestion, None, completedQst, progressbar, gameplaycanvas, mainmenucanvas, selectedmode, checkbox, root)
                update_progress(progressbar, completedQst)
        for btn in btnlist:
            if btn is not None:
                DisableButton(btn)
    else:
        btnpitchlist[number].configure(fg_color='red', hover=False)


def NextPitch(canvas, mainMenu, pitchcanvas, btnlist, progressbar, completedQst, nbrquestion, gameplaycanvas, playSoundBtn, mainmenucanvas, selectedmode, checkbox, root):
    completedQst = completedQst + 1
    playSoundBtn.place(relx=0.4, rely=0.3, anchor="center")
    nextButton = ctk.CTkButton(canvas, text="Next",
                               width=80, height=40, font=('arial', 15), fg_color='black', text_color='white')
    nextButton.bind("<Button-1>", lambda event: Next(mainMenu, canvas, pitchcanvas,
                    btnlist, nbrquestion, nextButton, completedQst, progressbar, gameplaycanvas, mainmenucanvas, selectedmode, checkbox, root))
    nextButton.place(relx=0.6, rely=0.3, anchor="center")
    update_progress(progressbar, completedQst)


def RandomizePitch(mode):
    folder_path = "allData/assets/SoundEffects/Pitches/"
    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    filtered_list = []
    for pitch in file_list:
        if pitch[0].capitalize() in mode:
            filtered_list.append(pitch)
    file = random.choice(filtered_list)
    
    return file

def DestroyButtons(btnlist):
    for btn in btnlist:
        if btn is not None:
            btn.destroy()


def Next(mainMenu, canvas, pitchcanvas, btnlist, nbrquestion, button, completedQst, progressbar, gameplaycanvas, mainmenucanvas, selectedmode, checkbox, root):
    if button is not None:
        button.destroy()
    Pitch(mainMenu, canvas, pitchcanvas, btnlist,
          nbrquestion, completedQst, progressbar, gameplaycanvas, mainmenucanvas, selectedmode, checkbox, root)



def Pitch(mainMenu, canvas, pitchcanvas, btnlist, nbrquestion, completedQst, progressbar, gameplaycanvas, mainmenucanvas, selectedmode, checkbox, root):
    if nbrquestion == 0:
        pass
    elif completedQst == nbrquestion:
        GetBackToMenu(gameplaycanvas, mainmenucanvas)
        return
    

    randomPitch = RandomizePitch(selectedmode)
    randomLetter = randomPitch[0]
    playPitch(randomPitch)

    DestroyButtons(btnlist)
    btnlist.clear()
    for menus in mainMenu:
        if menus is not None:
            menus.destroy()

    playSoundBtn = ctk.CTkButton(canvas, text="Hear Sound",
                                 width=80, height=40, font=('arial', 15), command=lambda: playPitch(randomPitch), fg_color='black', text_color='white')
    playSoundBtn.place(relx=0.5, rely=0.3, anchor="center")
    btnlist.append(playSoundBtn)
    title = ctk.CTkLabel(canvas, text="Perfect Pitch Test",
                         fg_color="transparent", font=('arial', 30), text_color='black', anchor=ctk.CENTER)
    title.place(relx=0.5, rely=0.15, anchor="center")
    buttonPosition = 0
    boolvalue = True
    btnpitchlist = []
    print(selectedmode)
    if len(selectedmode) == 3:
        buttonPosition = 0.3
    if len(selectedmode) == 7:
        buttonPosition = 0.1
    for pitchbutton in range(len(selectedmode)):
        buttonPosition+=0.1
        btnpitchlist.append(None)
        create_buttons(pitchbutton, btnpitchlist, btnlist, randomLetter, canvas, mainMenu, pitchcanvas, progressbar, completedQst, nbrquestion, gameplaycanvas, playSoundBtn, mainmenucanvas, selectedmode, buttonPosition, checkbox, root)

def create_buttons(pitchbutton, btnpitchlist, btnlist, randomLetter, canvas, mainMenu, pitchcanvas, progressbar, completedQst, nbrquestion, gameplaycanvas, playSoundBtn, mainmenucanvas, selectedmode, buttonPosition, checkbox, root):
    btnpitchlist[pitchbutton] = ctk.CTkButton(canvas, text=selectedmode[pitchbutton],
                             width=60, height=60, font=('arial', 20), command=lambda num=selectedmode[pitchbutton], num2=pitchbutton: CheckAnswer(num, randomLetter, canvas, mainMenu, pitchcanvas, btnlist, progressbar, completedQst, nbrquestion, gameplaycanvas, playSoundBtn, mainmenucanvas, selectedmode, btnpitchlist, num2, checkbox, root))
    btnpitchlist[pitchbutton].place(relx=(buttonPosition), rely=0.5, anchor="center")
    btnlist.append(btnpitchlist[pitchbutton])



def GetBackToMenu(gameplaycanvas, mainmenucanvas):
    for gameplay in gameplaycanvas:
        if gameplay is not None:
            gameplay.destroy()
            print('destoyed :', gameplay)
    mainmenucanvas()


def EnterPitchTest(mainMenu, root, pitchcanvas, questionEntry, gameplaycanvas, mainmenucanvas, optionmenu, checkbox):
    selectedmode=optionmenu.get()
    if selectedmode == 'Simple (C, D, E)':
        mode = ['C', 'D', 'E']
    if selectedmode == '(C, D, E, F, G, A, B)':
        mode = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    completedQst = 0
    nbrquestion = int(questionEntry.get())
    print(nbrquestion)
    btnlist = []
    gameCanvas = ctk.CTkCanvas(root, width=640, height=360)
    gameCanvas.pack()
    gameplaycanvas.append(gameCanvas)
    if nbrquestion != 0:
        label678 = ctk.CTkLabel(gameCanvas, text='Completed :',
                          fg_color="transparent", font=('arial', 15), text_color='black')
        label678.place(relx=0.27, rely=0.865, anchor="center")
        progressbar = ctk.CTkProgressBar(
            gameCanvas, orientation="horizontal", width=100, mode="determinate", progress_color='green')
        progressbar.place(relx=0.27, rely=0.9, anchor="center")
        progressbar.set(0)
    else:
        progressbar = None
    returnbutton = ctk.CTkButton(root, text="🏠",
                                 width=40, height=40, command=lambda: GetBackToMenu(gameplaycanvas, mainmenucanvas), bg_color='white')
    returnbutton.place(x=30, y=300)
    returnbutton.lift()
    Pitch(mainMenu, gameCanvas, pitchcanvas, btnlist,
          nbrquestion, completedQst, progressbar, gameplaycanvas, mainmenucanvas, mode, checkbox, root)


def pitchMenu(mainMenu, root, gameplaycanvas, mainmenucanvas):
    for maincanvas in mainMenu:
        if maincanvas is not None:
            maincanvas.destroy()
            print('destoyed :', maincanvas)
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
                                   "Simple (C, D, E)", '(C, D, E, F, G, A, B)'], font=('arial', 20))
    optionmenu.set("Simple (C, D, E)")
    optionmenu.place(relx=0.5, rely=0.62, anchor="center")
    # questionEntry = ctk.CTkEntry(pitchcanvas, width=200, font=('arial', 20), placeholder_text='Write a Number...')

    def slider_event(flaotvalue):
        nbrquestion = int(flaotvalue)
        valueCTK.configure(text=int(flaotvalue))

    nbrquestion = None
    questionEntry = ctk.CTkSlider(
        pitchcanvas, from_=0, to=40, command=slider_event, bg_color='white', fg_color='grey', progress_color='black')
    questionEntry.place(relx=0.5, rely=0.72, anchor="center")
    questionEntry.set(0)
    questions = ctk.CTkLabel(pitchcanvas, text="Questions :",
                             fg_color="transparent", font=('arial', 20), text_color='black')
    questions.place(x=115, y=243)
    label2 = ctk.CTkLabel(pitchcanvas, text="Leave as 0 for never-ending quiz.",
                          font=('arial', 15), text_color='black')
    label2.place(x=110, y=270)

    valueCTK = ctk.CTkLabel(pitchcanvas, text='',
                            fg_color="transparent", font=('arial', 20), text_color='black')
    valueCTK.place(x=450, y=243)
    checkbox = ctk.CTkCheckBox(pitchcanvas, text="Auto Proceed",
                                onvalue=True, offvalue=False, font=('arial', 18), text_color='black')
    checkbox.place(x=445, y=210)
    prfcPitch = ctk.CTkButton(pitchcanvas, text="Start Quiz",
                              width=80, height=40, command=lambda: EnterPitchTest(mainMenu, root, pitchcanvas, questionEntry, gameplaycanvas, mainmenucanvas, optionmenu, checkbox))
    prfcPitch.place(x=280, y=300)
    
    print(questionEntry.get())
