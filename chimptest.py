# region Chimp
import customtkinter as ctk
import json
import random
import threading
from playsound import playsound
from client import GetLocalHighScore
# endregion

with open('allData/json/data.json', 'r') as f:
    data = json.load(f)

# region vars
mistakes = 0
buttn_list = []
clickedList = []
button_positions = []
dataPath = 'allData/json/data.json'
# endregion


def play_audio(file_path):
    playsound(file_path)


def hide_numbers():
    for i in range(len(buttn_list)):
        try:
            buttn_list[i].configure(text_color='black')
        except Exception as e:
            pass


def resetLevelChimp():
    from main import resetLevelChimp
    resetLevelChimp()


def AddToList(buttonNumb, chimpcanvas, root, menu, mainMenu, gameplayMenus, screen_width, screen_height, user, online):
    audio_thread = threading.Thread(target=play_audio, args=(
        'allData/assets/SoundEffects/click.wav',))
    audio_thread.start()
    global mistakes
    level = data['CHIMP_TEST_LEVEL']
    buttn_list[buttonNumb-1].destroy()
    clickedList.append(buttonNumb)
    if len(clickedList) == level + 3:
        # for i in range(len(gameplayMenus)):
        #    if gameplayMenus[i] is not None:
        #        gameplayMenus[i].destroy()
        clickedList.clear()
        level = data['CHIMP_TEST_LEVEL']
        data["CHIMP_TEST_LEVEL"] = level + 1
        with open(dataPath, "w") as jsonFile:
            json.dump(data, jsonFile)

        for i in range(len(buttn_list)):
            if buttn_list[i] is not None:
                buttn_list[i].destroy()

        create_buttons(root, mainMenu, gameplayMenus, menu, screen_width, screen_height, user, online)
        return
    elif len(clickedList) == 1:
        hide_numbers()
        if clickedList[0] != 1:
            mistakes = mistakes + 1
            failedChimp(chimpcanvas, root, mainMenu, menu, gameplayMenus, screen_width, screen_height, user, online)
            return
    elif not check_order(lst=clickedList):
        mistakes = mistakes + 1
        failedChimp(chimpcanvas, root, mainMenu, menu, gameplayMenus, screen_width, screen_height, user, online)
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


def generate_random_position(button, root):
    button.lift()
    button_width = button.winfo_reqwidth()
    button_height = button.winfo_reqheight()
    x_min = 0
    x_max = 640 - button_width
    y_min = 0
    y_max = 360 - button_height
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


def create_buttons(root, mainMenu, gameplayMenus, menu, screen_width, screen_height, user, online):
    level = data['CHIMP_TEST_LEVEL']
    for numb in range(level + 3):
        numb1 = numb + 1
        buttn_list.append(None)
        buttn_list[numb] = ctk.CTkButton(chimpCanvas, text=str(
            numb1), width=50, height=50, text_color='white', hover_color='black', fg_color='black', font=("arial", 22),
            command=lambda num=numb1: AddToList(num, chimpCanvas, root, menu, mainMenu, gameplayMenus, screen_width, screen_height, user, online))
        x_coord, y_coord = generate_random_position(buttn_list[numb], root)
        buttn_list[numb].place(x=x_coord, y=y_coord)
        button_positions.append(
            (x_coord, y_coord, x_coord + buttn_list[numb].winfo_reqwidth(), y_coord + buttn_list[numb].winfo_reqheight()))


def EnterChimpTest(root, mainMenu, gameplayMenus, menu, screen_width, screen_height, user, online):
    global chimpCanvas
    for i in range(len(mainMenu)):
        if mainMenu[i] is not None:
            mainMenu[i].destroy()
    chimpCanvas = ctk.CTkCanvas(root, width=screen_width, height=screen_height)
    chimpCanvas.pack()
    create_buttons(root, mainMenu, gameplayMenus, menu, screen_width, screen_height, user, online)

    # for i in buttn_list:
    #    pass
    #    # print('Test: ' + i.__repr__())


def UpdateHSToServer(user):
    from client import requestUrl
    response = requestUrl(mode='update', username=user)
    if response == 'True':
        print('highscore updated! for ', user)
    if response == 'False':
        print('couldnt update highscore for ', user)


def failedChimp(chimpCanvas, root, mainMenu, menu, gameplayMenus, screen_width, screen_height, user, online):
    global mistakes
    if online == True:
        from client import requestUrl
        response = requestUrl(mode='read', username=user)
        if response != 'user not registered':
            if int(response) < GetLocalHighScore():
                print('updating highscore to server...')
                UpdateHSToServer(user)
                print('done')
            else:
                return

    if mistakes == 3:
        GameOverChimp(chimpCanvas, root, mainMenu, menu, gameplayMenus, screen_width, screen_height, user, online)
        print('Game Over')
        mistakes = 0
        return
    else:
        level = data['CHIMP_TEST_LEVEL']
        clickedList.clear()
        chimpCanvas.destroy()
        canvas = ctk.CTkCanvas(root, width=screen_width, height=screen_height)
        canvas.pack()
        mainMenu.append(canvas)
        nmbLabel = ctk.CTkLabel(canvas, text="NUMBERS",
                                fg_color="transparent", font=('arial', 20), text_color='black')
        nmbLabel.place(relx=0.5, rely=0.25, anchor="center")
        levelLabel = ctk.CTkLabel(canvas, text=str(int(level)+3),
                                  fg_color="transparent", font=('arial', 40), text_color='black')
        levelLabel.place(relx=0.5, rely=0.4, anchor="center")
        strikesLabel = ctk.CTkLabel(canvas, text="STRIKES",
                                    fg_color="transparent", font=('arial', 20), text_color='black')
        strikesLabel.place(relx=0.5, rely=0.55, anchor="center")
        strikes = ctk.CTkLabel(canvas, text=(str(mistakes) + ' of 3'),
                               fg_color="transparent", font=('arial', 40), text_color='black')
        strikes.place(relx=0.5, rely=0.7, anchor="center")
        playAgain = ctk.CTkButton(canvas, text="Continue",
                                  width=100, height=50, command=lambda: EnterChimpTest(root, mainMenu, gameplayMenus, menu, screen_width, screen_height, user, online))
        playAgain.place(relx=0.5, rely=0.9, anchor="center")


def GameOverChimp(chimpCanvas, root, mainMenu, menu, gameplayMenus, screen_width, screen_height, user, online):
    level = data['CHIMP_TEST_LEVEL']
    if data["HIGH_SCORE_CHIMP"] < level:
        data["HIGH_SCORE_CHIMP"] = level
        with open(dataPath, "w") as jsonFile:
            json.dump(data, jsonFile)
    resetLevelChimp()
    clickedList.clear()
    chimpCanvas.destroy()
    failcanvas = ctk.CTkCanvas(root, width=screen_width, height=screen_height)
    failcanvas.pack()
    mainMenu.append(failcanvas)
    pwlabel = ctk.CTkLabel(failcanvas, text="You failed :(",
                           fg_color="transparent", font=('arial', 50), text_color='black')
    pwlabel.place(x=190, y=100)
    Level = ctk.CTkLabel(failcanvas, text=('Level : %d' % level),
                         fg_color="transparent", font=('arial', 20), text_color='black')
    Level.place(x=280, y=160)
    playAgain = ctk.CTkButton(failcanvas, text="Play Again ?",
                              width=100, height=50, command=lambda: EnterChimpTest(root, mainMenu, gameplayMenus, menu, screen_width, screen_height, user, online))

    playAgain.place(x=200, y=200)
    backToMenu = ctk.CTkButton(failcanvas, text="Back To Menu",
                               width=100, height=50, command=menu)
    backToMenu.place(x=350, y=200)


def ChimpMenu(root, mainMenu, gameplayMenus, menu, screen_width, screen_height, user, online):
    # menus_to_destroy = mainMenu.copy()
    for i in range(len(mainMenu)):
        if mainMenu[i] is not None:
            mainMenu[i].destroy()
            print('destoyed :', mainMenu[i])
    chimpmainmenu = ctk.CTkCanvas(root, width=screen_width, height=screen_height)
    chimpmainmenu.pack()
    mainMenu.append(chimpmainmenu)

    title = ctk.CTkLabel(chimpmainmenu, text="Are You Smarter Than a Chimpanzee?",
                         fg_color="transparent", font=('arial', 30), text_color='black', anchor=ctk.CENTER)
    title.place(x=70, y=50)
    text = ctk.CTkLabel(chimpmainmenu, text="Click the squares in order according to their numbers.",
                        fg_color="transparent", font=('arial', 20), text_color='black')
    text.place(x=90, y=100)
    text2 = ctk.CTkLabel(chimpmainmenu, text="The test will get progressively harder.",
                         fg_color="transparent", font=('arial', 20), text_color='black')
    text2.place(x=145, y=125)
    ChimpTest = ctk.CTkButton(chimpmainmenu, text="Start Test",
                              width=80, height=40, command=lambda: EnterChimpTest(root, mainMenu, gameplayMenus, menu, screen_width, screen_height, user, online))
    ChimpTest.place(x=280, y=200)
    returnbutton = ctk.CTkButton(root, text="🏠",
                                 width=40, height=40, command=lambda: GetBackToMenu(gameplayMenus, menu), bg_color='white')
    returnbutton.place(x=30, y=300)
    returnbutton.lift()


def GetBackToMenu(gameplaycanvas, mainmenucanvas):
    for gameplay in gameplaycanvas:
        if gameplay is not None:
            gameplay.destroy()
            print('destoyed :', gameplay)
    mainmenucanvas()