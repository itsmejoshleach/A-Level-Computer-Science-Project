import tkinter as tk
from tkinter import ttk


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	def __init__(self, *args, **kwargs): # __init__ function for class tkinterApp
		tk.Tk.__init__(self, *args, **kwargs) # __init__ function for class Tk

		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, ConsumerPage, SupplierPage):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, ConsumerPage, SupplierPage respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage
class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		# label of frame Layout 2
		label = ttk.Label(self, text ="Startpage", font = LARGEFONT)

		# putting the grid in its place by using grid
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

  # button to show Consumer Page with text
		button1 = ttk.Button(self, text ="Consumer Page",
							command = lambda : controller.show_frame(ConsumerPage))
		button1.grid(row = 1, column = 1, padx = 10, pady = 10) # putting the button in its place

		# button to show Supplier Page with text
		button2 = ttk.Button(self, text ="Supplier Page",
							command = lambda : controller.show_frame(SupplierPage))
		button2.grid(row = 2, column = 1, padx = 10, pady = 10) # putting the button in its place by using grid


# second window frame ConsumerPage
class ConsumerPage(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Consumer Page", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show StartPage with text
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
		button1.grid(row = 1, column = 1, padx = 10, pady = 10) # putting the button in its place

		# button to show Supplier Page with text
		button2 = ttk.Button(self, text ="Supplier Page",
							command = lambda : controller.show_frame(SupplierPage))
		button2.grid(row = 2, column = 1, padx = 10, pady = 10) # putting the button in its place by using grid




# third window frame SupplierPage
class SupplierPage(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Supplier Page", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show StartPage with text
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
		button1.grid(row = 1, column = 1, padx = 10, pady = 10) # putting the button in its place

		# button to show Consumer Page with text
		button2 = ttk.Button(self, text ="Consumer Page",
							command = lambda : controller.show_frame(ConsumerPage))
		button2.grid(row = 2, column = 1, padx = 10, pady = 10) # putting the button in its place by using grid


# Driver Code
app = tkinterApp()
app.mainloop()
