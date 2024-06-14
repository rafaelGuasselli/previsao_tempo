from tkinter import messagebox

class Popup:
	def __init__(self, title, message):
		messagebox.showinfo(title, message)