
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
def btn_click(values): #Calculator buttons click event
    store=lblText.get()
    if store=="Error":
        lblText.set("")
    else:
        lblText.set(store+values)
#=====================================================================================================================================================================#

def btn_eql_click(): #Equal button click event
    try:
        lblText.set(eval(lblText.get()))
    except:
        lblText.set("Error")
#=====================================================================================================================================================================#

#Text variable for the display screen
lblText = StringVar()

#Display screen design
lbl_Display = Label(canvas, textvariable=lblText, anchor='e', bg='black', fg='red', font=('Digital-7',48)).grid(row=1, columnspan=4, sticky='ew', padx=4, pady=2)
#=====================================================================================================================================================================#

#Buttons design and coding

btn_clr=    Button(canvas, text="C", command=btn_clear, bg=CC, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=2, column=0,padx=4, pady=4)
btn_bck=    Button(canvas, text="<<", command=btn_backspace, bg=CC, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=2, column=1,padx=4, pady=4)
btn_per=    Button(canvas, text="%",  command=btn_percent, bg=CC, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=2, column=2,padx=4, pady=4)
btn_div=    Button(canvas, text="/", command=lambda: btn_click('/'), bg=CC, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=2, column=3,padx=4, pady=4)

btn7=       Button(canvas, text="7", command=lambda: btn_click("7"), bg=WHT, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=3, column=0,padx=4, pady=4)
btn8=       Button(canvas, text="8", command=lambda: btn_click("8"), bg=WHT, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=3, column=1,padx=4, pady=4)
btn9=       Button(canvas, text="9", command=lambda: btn_click("9"), bg=WHT, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=3, column=2,padx=4, pady=4)
btn_multi=  Button(canvas, text="*", command=lambda: btn_click('*'), bg=CC, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=3, column=3,padx=4, pady=4)

btn4=       Button(canvas, text="4", command=lambda: btn_click("4"),bg=WHT, width=7, fg="red", height=2, font=("Digital-7", 28)).grid(row=4, column=0,padx=4, pady=4)
btn5=       Button(canvas, text="5", command=lambda: btn_click("5"), bg=WHT, width=7, fg="red", height=2, font=("Digital-7", 28)).grid(row=4, column=1,padx=4, pady=4)
btn6=       Button(canvas, text="6", command=lambda: btn_click("6"), bg=WHT, width=7, fg="red", height=2, font=("Digital-7", 28)).grid(row=4, column=2,padx=4, pady=4)
btn_sub=    Button(canvas, text="-", command=lambda: btn_click('-'), bg=CC, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=4, column=3,padx=4, pady=4)

btn1=       Button(canvas, text="1", command=lambda: btn_click("1"), bg=WHT, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=5, column=0,padx=4, pady=4)
btn2=       Button(canvas, text="2", command=lambda: btn_click("2"),bg=WHT, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=5, column=1,padx=4, pady=4)
btn3=       Button(canvas, text="3", command=lambda: btn_click("3"),bg=WHT, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=5, column=2,padx=4, pady=4)
btn_add=    Button(canvas, text="+", command=lambda: btn_click('+'),bg=CC, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=5, column=3,padx=4, pady=4)

btn0=       Button(canvas, text="0", command=lambda: btn_click("0"), bg=WHT, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=6, column=0,padx=4, pady=4)
btn_point=  Button(canvas, text=".", command=lambda: btn_click('.'), bg=WHT, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=6, column=1,padx=4, pady=4)
btn_root=   Button(canvas, text='x²', command=btn_square,            bg=WHT, fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=6, column=2,padx=4, pady=4)
btn_eql=    Button(canvas, text="=", command=btn_eql_click,          bg="#F8B605", fg="red", width=7, height=2, font=("Digital-7", 28)).grid(row=6, column=3,padx=4, pady=4)
