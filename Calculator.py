import tkinter as tk
from Constants import *
import time
import tkinter.font as font


WIDTH, HEIGHT = 600, 800

class App(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack() 
		self.widgits()
		global expression 
		expression = ""

	def widgits(self):
		self.master.minsize(WIDTH,HEIGHT)
		self.master.minsize(WIDTH,HEIGHT)
		
		equation = tk.StringVar()
		expression_field = tk.Entry(self, textvariable=equation) 
		expression_field.grid(columnspan=5, ipadx=100,pady=20) 
		equation.set('') 


		button1 = tk.Button(self, text='1', fg='black', bg='white', 
                     command=lambda: press(1.0), height=10, width=20) 
		button1.grid(row=4, column=0) 

		button2 = tk.Button(self, text='2', fg='black', bg='white', 
		             command=lambda: press(2.0), height=10, width=20) 
		button2.grid(row=4, column=1) 

		button3 = tk.Button(self, text='3', fg='black', bg='white', 
		             command=lambda: press(3.0), height=10, width=20) 
		button3.grid(row=4, column=2) 

		button4 = tk.Button(self, text='4', fg='black', bg='white', 
		             command=lambda: press(4.0), height=10, width=20) 
		button4.grid(row=3, column=0) 

		button5 = tk.Button(self, text='5', fg='black', bg='white', 
		             command=lambda: press(5.0), height=10, width=20) 
		button5.grid(row=3, column=1) 

		button6 = tk.Button(self, text='6', fg='black', bg='white', 
		             command=lambda: press(6.0), height=10, width=20) 
		button6.grid(row=3, column=2) 

		button7 = tk.Button(self, text='7', fg='black', bg='white', 
		             command=lambda: press(7.0), height=10, width=20) 
		button7.grid(row=2, column=0) 

		button8 = tk.Button(self, text='8', fg='black', bg='white', 
		             command=lambda: press(8.0), height=10, width=20) 
		button8.grid(row=2, column=1) 

		button9 = tk.Button(self, text='9', fg='black', bg='white', 
		             command=lambda: press(9.0), height=10, width=20) 
		button9.grid(row=2, column=2) 

		button0 = tk.Button(self, text='0', fg='black', bg='white', 
		             command=lambda: press(0.0), height=10, width=20) 
		button0.grid(row=5, column=1) 

		plus = tk.Button(self, text=' + ', fg='black', bg='white', 
		          command=lambda: press("+"), height=10, width=20) 
		plus.grid(row=2, column=3) 

		minus = tk.Button(self, text=' - ', fg='black', bg='white', 
		           command=lambda: press("-"), height=10, width=20) 
		minus.grid(row=3, column=3) 

		multiply = tk.Button(self, text=' * ', fg='black', bg='white', 
		              command=lambda: press("*"), height=10, width=20) 
		multiply.grid(row=4, column=3) 

		divide = tk.Button(self, text=' / ', fg='black', bg='white', 
		            command=lambda: press("/"), height=10, width=20) 
		divide.grid(row=5, column=3) 

		equal = tk.Button(self, text=' = ', fg='black', bg='white', 
		           command=lambda:equalpress(), height=10, width=42) 
		equal.grid(row=6, column=2,columnspan=2) 

		clear = tk.Button(self, text='Clear', fg='black', bg='white', 
		           command=lambda:clear(), height=10, width=20) 
		clear.grid(row=5, column=0) 

		Decimal= tk.Button(self, text='.', fg='black', bg='white', 
		            command=lambda: press('.'), height=10, width=20) 
		Decimal.grid(row=5, column=2,sticky='EWNS') 

		percent = tk.Button(self, text='%',fg='black',bg='white',
			command=lambda:press('%'),height=10,width=42)
		percent.grid(row=6,column=0,columnspan=2, sticky='EWNS')

		def press(num):
			global expression
			num = str(num)
			exclude_decimal = num[:num.find('.')]
			try:
				if num == "%":
					find = expression[ : expression.find('%')]
					expression = expression + str(num)
					expression =expression.replace('%','')
					expression = str(int(expression)/100)
					equation.set(expression)
			
				elif num == "*"	or num =="/" or num == "+" or num =="-":
					expression = expression + num
					equation.set(expression) 


				else:
					expression= expression + exclude_decimal
					equation.set(expression)	

			except:
				expression = "ERROR"	
				equation.set(expression)

		def equalpress():
			global expression
			try:

				total = str(eval(expression))
				equation.set(total)
				expression=''
			except:
				equation.set(" error ") 
				expression = "" 
				
		def clear(): 
    			global expression 
    			expression = "" 
    			equation.set("") 
root = tk.Tk()
myapp = App(root)
myapp.mainloop()