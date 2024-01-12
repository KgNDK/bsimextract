import customtkinter as ctk

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


app = ctk.CTk()
optionmenu = ctk.CTkOptionMenu(app, values=["option 1", "option 2"], command=optionmenu_callback).pack()

app.mainloop()