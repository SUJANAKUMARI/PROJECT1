import tkinter as tk

calculation = ""

def add_to_calculate(symbol):
    global calculation
    calculation += str(symbol)
    textresult.delete(1.0, "end")
    textresult.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        textresult.delete(1.0, "end")
        textresult.insert(1.0, calculation)
    except:
        clear_field()
        textresult.insert(1.0, "ERROR")

def clear_field():
    global calculation
    calculation = ""
    textresult.delete(1.0, "end")

root=tk.Tk()
root.title('Simple GUI Calculator')
root.geometry("335x365")

display_frame=tk.Frame(root, width=280, height=90, bd=-7, highlightbackground="grey", highlightthickness=15)
display_frame.grid(row=0, column=0)

button_frame=tk.Frame(root, width=300, height=200, highlightbackground="grey", highlightthickness=15)
button_frame.grid(row=1, column=0, pady=10, padx=10)

textresult = tk.Text(display_frame, height=1, width=14, font= ("Arial", 24))
textresult.grid(row =0, column=0, pady=20, padx=20)

btn1 = tk.Button(button_frame, text='1', width=5,height=1, font = ('Arial', 16),  foreground="white", background="blue",command=lambda: add_to_calculate(1))
btn1.grid(row=0, column=1)

btn2 = tk.Button(button_frame, text='2', width=5,height=1, font = ('Arial', 16), foreground="white", background="blue",command=lambda: add_to_calculate(2))
btn2.grid(row=0, column=2)

btn3 = tk.Button(button_frame, text='3', width=5,height=1, font = ('Arial', 16), foreground="white", background="blue", command=lambda:add_to_calculate(3))
btn3.grid(row=0, column=3)

btnplus = tk.Button(button_frame, text='+', width=5,height=1, font = ('Arial', 16), background="orange", foreground="white", command=lambda: add_to_calculate("+"))
btnplus.grid(row=0, column=4)

btn4 = tk.Button(button_frame, text='4', width=5,height=1, font = ('Arial', 16), foreground="white", background="blue", command=lambda: add_to_calculate(4))
btn4.grid(row=1, column=1)

btn5 = tk.Button(button_frame, text='5', width=5,height=1, font = ('Arial', 16),  foreground="white", background="blue", command=lambda: add_to_calculate(5))
btn5.grid(row=1, column=2)

btn6 = tk.Button(button_frame, text='6', width=5,height=1, font = ('Arial', 16), foreground="white", background="blue",  command=lambda: add_to_calculate(6))
btn6.grid(row=1, column=3)

btnminus = tk.Button(button_frame, text='-', width=5,height=1, font = ('Arial', 16), background="orange", foreground="white", command=lambda: add_to_calculate("-"))
btnminus.grid(row=1, column=4)

btn7 = tk.Button(button_frame, text='7', width=5,height=1, font = ('Arial', 16), foreground="white", background="blue", command=lambda: add_to_calculate(7))
btn7.grid(row=2, column=1)

btn8 = tk.Button(button_frame, text='8', width=5,height=1, font = ('Arial', 16), foreground="white", background="blue", command=lambda: add_to_calculate(8))
btn8.grid(row=2, column=2)

btn9 = tk.Button(button_frame, text='9', width=5,height=1, font = ('Arial', 16), foreground="white", background="blue", command=lambda: add_to_calculate(9))
btn9.grid(row=2, column=3)

btnmultiply = tk.Button(button_frame, text='*', width=5,height=1, font = ('Arial', 16), background = "orange", foreground="white", command= lambda:add_to_calculate("*")) 
btnmultiply.grid(row=2, column=4)

btndot = tk.Button(button_frame, text='.', width=5,height=1, font = ('Arial', 16), foreground="white", background="blue", command=lambda:add_to_calculate("."))
btndot.grid(row=3, column=1)

btn0 = tk.Button(button_frame, text='0', width=5,height=1, font = ('Arial', 16),foreground="white", background="blue", command=lambda: add_to_calculate(0))
btn0.grid(row=3, column=2)

btndouble0 = tk.Button(button_frame, text='00', width=5,height=1, font = ('Arial', 16), foreground="white", background="blue", command=lambda: add_to_calculate("00"))
btndouble0.grid(row=3, column=3)

btndivide = tk.Button(button_frame, text='/', width=5,height=1, font = ('Arial', 16), background = "orange", foreground="white", command=lambda: add_to_calculate("/"))
btndivide.grid(row=3, column=4)

btnequals = tk.Button(button_frame, text='=', width=11, font = ('Arial', 16), background= "green", foreground="white", command = evaluate_calculation)
btnequals.grid(row=4, column=1, columnspan=2)

btnclear = tk.Button(button_frame, text='C', width=11, font = ('Arial' ,16), foreground="white", background="red", command = clear_field)
btnclear.grid(row=4, column=3, columnspan=2)

root.mainloop()