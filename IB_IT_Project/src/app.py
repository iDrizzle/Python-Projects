import customtkinter as ctk
from main_menu import MainMenu
from comiss_concl import comiss_concl
from msg_maestro import msg_maestro
from note import note
from register import RegisterPage
from term import term


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Automação - TI")
        self.geometry("400x300")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1) 
        self.grid_columnconfigure(0, weight=1)

        
        self.frames = {
            "main_menu": MainMenu(self), 
            "comiss_concl":comiss_concl(self),
            "msg_maestro":msg_maestro(self),
            "note": note(self),
            "register": RegisterPage(self),
            "term": term(self),
        }

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("main_menu")  

    def show_frame(self, name):
        """Exibe uma tela pelo nome"""
        frame = self.frames[name]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
