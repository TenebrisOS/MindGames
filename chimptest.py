# region imports
import json
import random
import threading
from playsound import playsound

# endregion

with open('allData/json/data.json') as f:
    data = json.load(f)

# region vars
mistakes = 0
buttn_list = []

level = data['CHIMP_TEST_LEVEL']
clickedList = []
button_positions = []
dataPath = 'allData/json/data.json'
# endregion


def resetLevelChimp():
    data["CHIMP_TEST_LEVEL"] = 1
    with open(dataPath, "w") as jsonFile:
        json.dump(data, jsonFile)


def AddToList(buttonNumb, chimpcanvas):
    from main import gameplayMenus
    def play_audio(file_path):
        playsound(file_path)
    audio_thread = threading.Thread(target=play_audio, args=(
        'allData/assets/SoundEffects/click.wav',))
    audio_thread.start()
    global mistakes
    level = data['CHIMP_TEST_LEVEL']
    buttn_list[buttonNumb-1].destroy()
    clickedList.append(buttonNumb)
    if len(clickedList) == level + 3:
        for i in range(len(gameplayMenus)):
            if gameplayMenus[i] is not None:
                gameplayMenus[i].destroy()
        clickedList.clear()
        # clickedList.append(buttonNumb)
        print(clickedList)
        level = data['CHIMP_TEST_LEVEL']
        data["CHIMP_TEST_LEVEL"] = level + 1
        with open(dataPath, "w") as jsonFile:
            json.dump(data, jsonFile)

        chimpcanvas.destroy()

        create_buttons()
        print('chimpcanvas')
        return
    elif len(clickedList) == 1:
        # for i in range(len(buttn_list)):
        #    try:
        #        buttn_list[i].configure(text_color='black')
        #    except Exception as e:
        #        pass
        if clickedList[0] != 1:
            mistakes = mistakes + 1
            failedChimp(chimpCanvas=chimpcanvas)
            return
    elif not check_order(lst=clickedList):
        mistakes = mistakes + 1
        failedChimp(chimpCanvas=chimpcanvas)
        return


def check_order(lst):
    var = True
    for i in range(len(lst)):
        if lst[i] == (lst[i-1]+1):
            var = True
        if lst[i] != (lst[i-1]+1):
            var = False
    if var == True:
        return True
    if var == False:
        return False


def generate_random_position(button):
    from main import root, ctk
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
    from main import mainMenu, gameplayMenus
    from main import root, ctk
    level = data['CHIMP_TEST_LEVEL']
    for i in range(len(mainMenu)):
        if mainMenu[i] is not None:
            mainMenu[i].destroy()
    print('test')
    chimpCanvas = ctk.CTkCanvas(root, width=640, height=360)
    chimpCanvas.pack()
    print('test2')
    gameplayMenus.append(chimpCanvas)
    print('test3')
    for numb in range(level + 3):
        numb1 = numb + 1
        buttn_list.append(None)
        print('test4')
        buttn_list[numb] = ctk.CTkButton(chimpCanvas, text=str(
            numb1), width=50, height=50, text_color='white', bg_color='white', hover_color='black', fg_color='black', font=("arial", 22), command=lambda num=numb1: AddToList(buttonNumb=num, chimpcanvas=chimpCanvas))
        print('test5')
        x_coord, y_coord = generate_random_position(buttn_list[numb])
        print('test6')
        buttn_list[numb].place(x=x_coord, y=y_coord)
        button_positions.append(
            (x_coord, y_coord, x_coord + buttn_list[numb].winfo_reqwidth(), y_coord + buttn_list[numb].winfo_reqheight()))
        print('test7')


def EnterChimpTest():
    create_buttons()

    for i in buttn_list:
        pass
        # print('Test: ' + i.__repr__())


def failedChimp(chimpCanvas):
    from main import root, ctk
    global mistakes
    if mistakes == 3:
        GameOverChimp(chimpCanvas)
        mistakes = 0
        return
    else:
        from main import mainMenu, gameplayMenus
        level = data['CHIMP_TEST_LEVEL']
        clickedList.clear()
        chimpCanvas.destroy()
        canvas = ctk.CTkCanvas(root, width=640, height=360)
        canvas.pack()
        mainMenu.append(canvas)
        nmbLabel = ctk.CTkLabel(canvas, text="NUMBERS",
                                fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
        nmbLabel.place(relx=0.5, rely=0.25, anchor="center")
        levelLabel = ctk.CTkLabel(canvas, text=str(int(level)+3),
                                  fg_color="transparent", font=('arial', 40), text_color='black', bg_color='white')
        levelLabel.place(relx=0.5, rely=0.4, anchor="center")
        strikesLabel = ctk.CTkLabel(canvas, text="STRIKES",
                                    fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
        strikesLabel.place(relx=0.5, rely=0.55, anchor="center")
        strikes = ctk.CTkLabel(canvas, text=(str(mistakes) + ' of 3'),
                               fg_color="transparent", font=('arial', 40), text_color='black', bg_color='white')
        strikes.place(relx=0.5, rely=0.7, anchor="center")
        playAgain = ctk.CTkButton(canvas, text="Continue",
                                  width=100, height=50, command=create_buttons)
        playAgain.place(relx=0.5, rely=0.9, anchor="center")


def GameOverChimp(chimpCanvas):
    from main import root, ctk, menu, mainMenu, resetLevelChimp
    level = data['CHIMP_TEST_LEVEL']
    resetLevelChimp()
    clickedList.clear()
    chimpCanvas.destroy()
    failcanvas = ctk.CTkCanvas(root, width=640, height=360)
    failcanvas.pack()
    mainMenu.append(failcanvas)
    pwlabel = ctk.CTkLabel(failcanvas, text="You failed :(",
                           fg_color="transparent", font=('arial', 50), text_color='black', bg_color='white')
    pwlabel.place(x=190, y=100)
    Level = ctk.CTkLabel(failcanvas, text=('Level : %d' % level),
                         fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    Level.place(x=280, y=160)
    playAgain = ctk.CTkButton(failcanvas, text="Play Again ?",
                              width=100, height=50, command=create_buttons)
    playAgain.place(x=200, y=200)
    backToMenu = ctk.CTkButton(failcanvas, text="Back To Menu",
                               width=100, height=50, command=menu)
    backToMenu.place(x=350, y=200)


def ChimpMenu():
    from main import mainMenu, root, ctk
    for i in range(len(mainMenu)):
        if mainMenu[i] is not None:
            mainMenu[i].destroy()
    chimpmainmenu = ctk.CTkCanvas(root, width=640, height=360)
    chimpmainmenu.pack()
    mainMenu.append(chimpmainmenu)
    title = ctk.CTkLabel(chimpmainmenu, text="Are You Smarter Than a Chimpanzee?",
                         fg_color="transparent", font=('arial', 30), text_color='black', bg_color='white', anchor=ctk.CENTER)
    title.place(x=70, y=50)
    text = ctk.CTkLabel(chimpmainmenu, text="Click the squares in order according to their numbers.",
                        fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    text.place(x=90, y=100)
    text2 = ctk.CTkLabel(chimpmainmenu, text="The test will get progressively harder.",
                         fg_color="transparent", font=('arial', 20), text_color='black', bg_color='white')
    text2.place(x=145, y=125)
    ChimpTest = ctk.CTkButton(chimpmainmenu, text="Start Test",
                              width=80, height=40, command=EnterChimpTest)
    ChimpTest.place(x=280, y=200)

