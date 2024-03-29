from tkinter import *
import tkinter as tk

root = tk.Tk() 
root.title("Calculadora básica")
result = tk.StringVar()
entry = tk.Entry(root, textvariable=result)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

def add_number(number):
    current = result.get()
    result.set(current + number)
button1 = tk.Button(root, text="1", command=lambda:add_number("1"))
button2 = tk.Button(root, text="2", command=lambda:add_number("2"))
button3 = tk.Button(root, text="3", command=lambda:add_number("3"))
button4 = tk.Button(root, text="4", command=lambda:add_number("4"))
button5 = tk.Button(root, text="5", command=lambda:add_number("5"))
button6 = tk.Button(root, text="6", command=lambda:add_number("6"))
button7 = tk.Button(root, text="7", command=lambda:add_number("7"))
button8 = tk.Button(root, text="8", command=lambda:add_number("8"))
button9 = tk.Button(root, text="9", command=lambda:add_number("9"))
button0 = tk.Button(root, text="0", command=lambda:add_number("0"))
button_plus = tk.Button(root, text="+", command=lambda:add_number("+"))
button_minus = tk.Button(root, text="-", command=lambda:add_number("-"))
button_multiply = tk.Button(root, text="*", command=lambda:add_number("*"))
button_divide = tk.Button(root, text="/", command=lambda:add_number("/"))
button_equals = tk.Button(root, text="=", command=lambda:result.set(eval(result.get())))
button7.grid(row=1, column=0, padx=5, pady=5)
button8.grid(row=1, column=1, padx=5, pady=5)
button9.grid(row=1, column=2, padx=5, pady=5)
button_divide.grid(row=1, column=3, padx=5, pady=5)
button4.grid(row=2, column=0, padx=5, pady=5)
button5.grid(row=2, column=1, padx=5, pady=5)
button6.grid(row=2, column=2, padx=5, pady=5)
button_multiply.grid(row=2, column=3, padx=5, pady=5)
button1.grid(row=3, column=1, padx=5, pady=5)
button2.grid(row=3, column=1, padx=5, pady=5)
button3.grid(row=3, column=2, padx=5, pady=5)
button_minus.grid(row=3, column=3, padx=5, pady=5)
button0.grid(row=4, column=0, padx=5, pady=5)
button_equals.grid(row=4, column=1, columnspan=2, padx=5, pady=5)
button_plus.grid(row=4, column=3, padx=5, pady=5)

root.mainloop()