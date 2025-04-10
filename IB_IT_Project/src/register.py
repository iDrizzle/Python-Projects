import customtkinter as ctk
import pandas as pd



class RegisterPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title_label = ctk.CTkLabel(self, text="Cadastro de Colaboradores", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)

        back_btn = ctk.CTkButton(self, text="Voltar", width=200, command=lambda: master.show_frame("main_menu"))
        back_btn.pack(pady=20)
