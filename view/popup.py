from tkinter import messagebox

class Popup:
	def __init__(self, titulo, mensagem):
		messagebox.showinfo(titulo, mensagem)