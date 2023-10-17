import customtkinter as ctk
from chimptest import ChimpMenu
from perfectpitch import pitchMenu
import json
import os
from client import requestUrl
# region tkinter settings
mainMenu = []
gameplayMenus = []
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("640x360")
screen_width = root.winfo_screenwidth()
root.minsize(640, 360)
root.maxsize(640, 360)
screen_height = root.winfo_screenheight()
root.title("Mind Games")
onlineSys = []
noteslist = []
# endregion


def resetLevelChimp():
    dataPath = 'allData/json/data.json'
    with open(dataPath, 'r') as f:
        data = json.load(f)

    key_to_change = 'CHIMP_TEST_LEVEL'
    new_value = 1
    data[key_to_change] = new_value

    with open(dataPath, 'w') as file:
        json.dump(data, file, indent=2)
    print('level : ', str(data["CHIMP_TEST_LEVEL"]))
    print('level reset!')


def main():
    resetLevelChimp()
    menu()
    root.mainloop()


def menu():
    for canvas in mainMenu:
        if canvas is not None:
            canvas.destroy()
            print('destoyed :', canvas)
    canvasMenu = ctk.CTkCanvas(root, width=screen_width, height=screen_height)
    canvasMenu.pack()
    mainMenu.append(canvasMenu)

    def buttonAction(is_chimp_test):
        canvasMenu.destroy()
        if is_chimp_test:
            if toggleOnline.get() == True:

                if username != '' or " ":
                    ChimpMenu(root, mainMenu, gameplayMenus, menu,
                              screen_width, screen_height, username, toggleOnline.get())
                else:
                    label563651 = ctk.CTkLabel(canvasMenu, text=('Pls enter a correct username!'),
                                               fg_color="transparent", font=('arial', 10), text_color='red')
                    label563651.place(x=100, y=100)
                    noteslist.append(label563651)
            else:
                ChimpMenu(root, mainMenu, gameplayMenus, menu,
                          screen_width, screen_height, None, toggleOnline.get())
            print('Chimp Test!')
        else:
            pitchMenu(mainMenu, root, gameplayMenus,
                      menu, screen_width, screen_height)
            print('Perfect Pitch Test!')
        # if bool is False:
        #     pitchMenu()

    # cap = cv2.VideoCapture('bg.mp4')
    label1 = ctk.CTkLabel(canvasMenu, text='Chimpanzee test',
                          fg_color="transparent", font=('arial', 20), text_color='black')
    label1.place(x=100, y=120)
    toggleOnline = ctk.CTkCheckBox(
        canvasMenu, text='Local Server System (experimental)', text_color='black')
    toggleOnline.place(x=20, y=320)
    toggleOnline.bind("<Button-1>", command=lambda event: toggle_action(
        event=True, toggle=toggleOnline, canvas=canvasMenu))
    ChimpTest = ctk.CTkButton(canvasMenu, text="Test",
                              width=100, height=40)
    ChimpTest.place(x=120, y=150)
    ChimpTest.lift()
    ChimpTest.bind("<Button-1>", lambda event: buttonAction(True))

    label2 = ctk.CTkLabel(canvasMenu, text='Perfect Pitch Quiz',
                          fg_color="transparent", font=('arial', 20), text_color='black')
    label2.place(x=360, y=120)
    perfectPitch = ctk.CTkButton(canvasMenu, text="Quiz",
                                 width=100, height=40)
    perfectPitch.place(x=380, y=150)
    perfectPitch.lift()
    # label3 = ctk.CTkLabel(canvasMenu, text='(experimental)',
    #                      fg_color="transparent", font=('arial', 20), text_color='black')
    # label3.place(x=370, y=200)
    perfectPitch.bind("<Button-1>", lambda event: buttonAction(False))


def Login(event, entry, canvas):
    for element in noteslist:
        if element is not None:
            element.destroy()
    global username
    username = entry.get()

    print(username)
    from client import requestUrl
    response = requestUrl(mode='read', username=username)
    if response == 'server offline':
        label56 = ctk.CTkLabel(canvas, text=('Server error or offline :('),
                               fg_color="transparent", font=('arial', 10), text_color='red')
        label56.place(x=180, y=90)
        noteslist.append(label56)
    elif response != 'user not registered':
        label3 = ctk.CTkLabel(canvas, text=('Highest Score : ' + str(response)),
                              fg_color="transparent", font=('arial', 20), text_color='black')
        label3.place(x=100, y=200)
        label56987 = ctk.CTkLabel(canvas, text=('Logged In Successfully!'),
                                  fg_color="transparent", font=('arial', 10), text_color='green')
        label56987.place(x=180, y=90)
        noteslist.append(label56987)
    else:
        label56 = ctk.CTkLabel(canvas, text=('User not Registered! Try register instead'),
                               fg_color="transparent", font=('arial', 10), text_color='red')
        label56.place(x=180, y=90)
        noteslist.append(label56)
    entry.delete(0, ctk.END)


def toggle_action(event, toggle, canvas):
    for element in noteslist:
        if element is not None:
            element.destroy()
    if toggle.get():
        label4 = ctk.CTkLabel(canvas, text='Enter Your Username :',
                              fg_color="transparent", font=('arial', 20), text_color='black')
        label4.place(x=200, y=30)
        onlineSys.append(label4)
        global usernameEntry
        usernameEntry = ctk.CTkEntry(canvas, font=(
            'arial', 20), text_color='white', width=200)
        usernameEntry.place(x=180, y=60)
        usernameEntry.bind('<Return>', lambda event: Login(
            True, entry=usernameEntry, canvas=canvas))
        onlineSys.append(usernameEntry)
        registerButton = ctk.CTkButton(canvas, text='Register', width=50)
        registerButton.place(x=465, y=60)
        registerButton.bind(
            "<Button-1>", lambda event: Register(True, entry=usernameEntry, canvas=canvas))
        onlineSys.append(registerButton)
        loginButton = ctk.CTkButton(canvas, text='Login', width=50)
        loginButton.place(x=400, y=60)
        loginButton.bind("<Button-1>", lambda event: Login(True,
                         entry=usernameEntry, canvas=canvas))
        onlineSys.append(loginButton)
    else:
        for element in onlineSys:
            if element is not None:
                element.destroy()


def Register(event, entry, canvas):
    for element in noteslist:
        if element is not None:
            element.destroy()
    text = entry.get()
    print(text)

    response = requestUrl(mode='submit', username=text)
    print(response)
    if response == 'server offline':
        label56 = ctk.CTkLabel(canvas, text=('Server error or offline :('),
                               fg_color="transparent", font=('arial', 10), text_color='red')
        label56.place(x=180, y=90)
    elif response == 'already exist':
        label563 = ctk.CTkLabel(canvas, text=('User Already Registered! Try login instead'),
                                fg_color="transparent", font=('arial', 10), text_color='red')
        label563.place(x=100, y=100)
        noteslist.append(label563)
    elif response == 'success':
        print('Registered Successfully!')
        label3 = ctk.CTkLabel(canvas, text=('Highest Score : ' + str(requestUrl(mode='read', username=text))),
                              fg_color="transparent", font=('arial', 20), text_color='black')
        label3.place(x=100, y=200)
        noteslist.append(label3)
        label566 = ctk.CTkLabel(canvas, text=('Registered Successfully!'),
                                fg_color="transparent", font=('arial', 10), text_color='green')
        label566.place(x=100, y=100)
        noteslist.append(label566)
        entry.delete(0, ctk.END)


if __name__ == "__main__":
    main()
