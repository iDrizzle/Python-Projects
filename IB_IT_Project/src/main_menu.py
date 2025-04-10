import customtkinter as ctk
from tkinter import messagebox


class MainMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title_label = ctk.CTkLabel(self, text="Menu Principal", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        options = [
            ("Cadastro de Colaboradores", "register"),
            ("Gerar Mensagem de Comissionamento (Concluído)", "comiss_concl"),
            ("Gerar Termo", "term"),
            ("Gerar Mensagem de Nota (Envio)", "note"),
            ("Gerar Mensagem de Registro Maestro", "msg_maestro")
        ]

        for text, page in options:
            btn = ctk.CTkButton(
                self, text=text, font=("Arial", 15), width=350,
                command=lambda p=page: master.show_frame(p) if p else self.not_ready()
            )
            btn.pack(pady=5)

    def not_ready(self):
        messagebox.showinfo("Atenção", "Essa funcionalidade ainda não está pronta!")
