import customtkinter as ctk
from chimptest import resetLevel, menu
# region tkinter settings
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("640x360")
root.minsize(640, 360)
root.maxsize(640, 360)
root.title("Mind Games")
root.iconbitmap("allData/assets/PNG/icon.ico")
# endregion
resetLevel()
menu()
root.mainloop()
