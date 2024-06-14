import tkinter as Tk
from tkinter import ttk
from tkinter.constants import *
from view.scrollable_weather_list import ScrollableWeatherList
from controller.home_controller import HomeController

class HomeView(Tk.Tk):
	def __init__(self):
		super().__init__()
		self.geometry("1200x600")
		self.controller = HomeController(self)
		self.initialize()
		
	def initialize(self):
		self.__clearElements()
		self.title("Home")
		self.rowconfigure(2, weight=10)
		self.columnconfigure(0, weight=1)

		self.__addHeader()
		self.__createDivider()
		self.__addWeatherList()

	def __createDivider(self):
		ttk.Separator(self, orient="horizontal").grid(sticky="WE", column=0, row=1)

	def __addWeatherList(self):
		self.list = ScrollableWeatherList(self)
		self.list.grid(sticky="WE", row=2, column=0)

	def __addHeader(self):
		self.header = Tk.Frame(self)
		self.header.grid(row=0, sticky="NSWE")

		self.header.rowconfigure(0, weight=10)
		self.header.columnconfigure((0,1,2,3,4,5, 6), weight=1)

		self.startDateLabel = Tk.Label(self.header, text="Data inicial: ", font=("Arial", 14, "bold"), justify="right")
		self.startDateInput = Tk.Entry(self.header, name="startDate")

		self.endDateLabel = Tk.Label(self.header, text="Data final: ", font=("Arial", 14, "bold"), justify="right")
		self.endDateInput = Tk.Entry(self.header, name="endDate")
		
		self.cityLabel = Tk.Label(self.header, text="Cidade: ", font=("Arial", 14, "bold"), justify="right")
		self.cityInput = Tk.Entry(self.header, name="cidade")

		self.searchButton = Tk.Button(self.header, text="Buscar", font=("Arial", 14), command=self.controller.search)

		self.startDateLabel.grid(row=0, column=0, padx=10, pady=10, sticky="E")
		self.startDateInput.grid(row=0, column=1, padx=10, pady=10, sticky="W")	

		self.endDateLabel.grid(row=0, column=2, padx=10, pady=10, sticky="E")
		self.endDateInput.grid(row=0, column=3, padx=10, pady=10, sticky="W")

		self.cityLabel.grid(row=0, column=4, padx=10, pady=10, sticky="E")
		self.cityInput.grid(row=0, column=5, padx=10, pady=10, sticky="W")

		self.searchButton.grid(row=0, column=6, padx=10, pady=10, sticky="E")
	
	def getStartDate(self):
		return self.startDateInput.get()

	def getEndDate(self):
		return self.endDateInput.get()

	def getCity(self):
		return self.cityInput.get()

	def __clearElements(self):
		for child in self.winfo_children(): 
			child.destroy()