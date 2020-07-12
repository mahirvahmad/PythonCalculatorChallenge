
from tkinter import *

#=====================================================================================================================================================================#
#colors for the  buttons, so we can use this short codes instead of writing color code every time.
WHT = "#FFFFFF" #White
CC = "#ffdead" #Chocolate Chip Cookies

#=====================================================================================================================================================================#
#Prepaing the ground for building the Calculator
calc = Tk()
calc.title("                                   +1-2%3√4/5* CALCULATOR *6/7√8%9-0+")
#calc.iconbitmap('calcico.ico')
calc.config(bg="#2C001E")
canvas=Canvas(calc,bg='#2C001E')
canvas.pack(padx=15, pady=15)
Label(canvas, text='a³k² Tech', anchor='e', bg='#2C001E', fg='white', font=('Corbel Light', 24, 'bold')).grid(row=0, columnspan=4, sticky='ew', padx=4, pady=2)

#=====================================================================================================================================================================#
