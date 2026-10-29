# Exercício
# Crie uma aplicação que pergunte o nome e o ano de nascimento do usuário
import tkinter as tk
from tkinter import messagebox
def calcular_idade():
    nome_usuario = ent_nome_usuario.get()
    ano_nascimento = ent_ano_nascimento.get()
    if nome_usuario == "" or ano_nascimento == "":
        messagebox.showwarning("verificar dados", "verificar os campos")
    else:


janela = tk.Tk()
janela.title("calculo idade")
janela.geometry("500x500")
janela.configure(bg="white")

lbl_idade = tk.label(janela, text="digite sua idade:", font=("arial", 12), fg="grey", bg="white")
lbl_idade.grid(row=0, column=0, pady=20, padx=20)

lbl_resultado = tk.label(janela, text="sua idade é:", font=("arial", 12), fg="grey", bg="white")
lbl_resultado.grid(row=1, column=0, pady=20, padx=20)







