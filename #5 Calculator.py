from tkinter import *
root = Tk()

root.title("Calculator")
root.geometry("280x350+1400+200")
root.resizable(width=False, height=False)

#Entry area:
myEntry = Entry(root, width=35, border=5)
myEntry.grid(row= 0, column=0, columnspan=3, padx=10, pady=30)
myEntry.focus_set()

#function area:
def click(number):
    currentClick = myEntry.get()
    myEntry.delete(0, END)
    myEntry.insert(0, str(currentClick) + str(number))

def clearButton():
    myEntry.delete(0,END)

def AddButton():
    firstNumber = myEntry.get()

    global fNumber 
    global math 
    math = "Add"
    fNumber = firstNumber
    myEntry.delete(0,END)
def subButton():
    firstNumber = myEntry.get()

    global fNumber 
    global math 
    math = "Sub"
    fNumber = firstNumber
    myEntry.delete(0,END)

def mulButton():
    firstNumber = myEntry.get()

    global fNumber 
    global math 
    math = "Mul"
    fNumber = firstNumber
    myEntry.delete(0,END)

def divButton():
    firstNumber = myEntry.get()

    global fNumber 
    global math 
    math = "Div"
    fNumber = firstNumber
    myEntry.delete(0,END)

def equalButton():
    secondNumber = myEntry.get()
    myEntry.delete(0,END)
    if math ==   "Add":
        myEntry.insert(0, int(fNumber) + int(secondNumber))
    elif math ==   "Sub":
        myEntry.insert(0, int(fNumber) - int(secondNumber))
    elif math ==   "Mul":
        myEntry.insert(0, int(fNumber) * int(secondNumber))
    elif math ==   "Div":
        myEntry.insert(0, int(fNumber) / int(secondNumber))

btn1 = Button(root, text="1", padx=40, pady=10, command=lambda: click(1)).grid(row=3, column=0)
btn2 = Button(root, text="2", padx=40, pady=10, command=lambda: click(2)).grid(row=3,column=1)
btn3 = Button(root, text="3", padx=40, pady=10, command=lambda: click(3)).grid(row=3, column=2)

btn4 = Button(root, text="4", padx=40, pady=10, command=lambda: click(4)).grid(row=2, column=0)
btn5 = Button(root, text="5", padx=40, pady=10, command=lambda: click(5)).grid(row=2, column=1)
btn6 = Button(root, text="6", padx=40, pady=10, command=lambda: click(6)).grid(row=2, column=2)

btn7 = Button(root, text="7", padx=40, pady=10, command=lambda: click(7)).grid(row=1, column=0)
btn8 = Button(root, text="8", padx=40, pady=10, command=lambda: click(8)).grid(row=1, column=1)
btn9 = Button(root, text="9", padx=40, pady=10, command=lambda: click(9)).grid(row=1, column=2)



btn0 = Button(root, text="0", padx=40, pady=10, command=lambda: click(0)).grid(row=4, column=0)
btnClear = Button(root, text="Clear", padx=77, pady=10, command=clearButton).grid(row=4, column=1, columnspan=2)
btnAdd = Button(root, text="+", padx=40, pady=10, command= AddButton).grid(row=5, column=0)
btnEq = Button(root, text="=", padx=86, pady=10, command=equalButton).grid(row=5, column=1, columnspan=2)

btnMul = Button(root, text="x", padx=40, pady=10, command= mulButton).grid(row=6, column=0)
btnDiv = Button(root, text="/", padx=40, pady=10, command= divButton).grid(row=6, column=1)
btnSub = Button(root, text="-", padx=40, pady=10, command= subButton).grid(row=6, column=2)

mainloop()