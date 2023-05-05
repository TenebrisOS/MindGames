import tkinter
import customtkinter
import webbrowser

def EnterGameplayScene(button) :
    button.pack_forget()

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("640x360")
PlayButton = customtkinter.CTkButton(master=root, text="Play", width=120, height=32, command=EnterGameplayScene)
PlayButton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)



root.mainloop()