from tkinter import *

m = Tk()
m.title("Simple Calculator")
m.config(bg="#222831")
m.geometry("390x550")
font_style = ("Helvetica", 25, "bold")

input_entry1 = Entry(m, width=15, font=font_style, bg="#EEEEEE")
input_entry1.grid(row=0, column=0, padx=10, pady=20, ipady=10, columnspan=3)

result_label = Label(m, text="", font=font_style, bg="#222831", fg="white")
result_label.grid(row=0, column=3, padx=10, pady=20, columnspan=2)

def calculate(event=None):
    try:
        expression = input_entry1.get()
        result = eval(expression)
        result_label.config(text=f"{result}")
    except Exception as e:  
        result_label.config(text="Error: Invalid Expression")

def update_input(text):
    temp = input_entry1.get()
    input_entry1.delete(0, END)
    input_entry1.insert(0, temp + text)

def clear_input():
    input_entry1.delete(0, END)

# Bind the Enter key to the calculate function
m.bind('<Return>', calculate)

# Buttons and input fields
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('.', 5, 0), ('0', 5, 1), ('%', 5, 2), ('/', 5, 3), 
    ('x²', 6, 0), ('=', 6, 1), ('C', 6, 2)
]

button_width = 3
button_height = 1
margin = 10

for (text, row, col) in buttons:
    if text == "=":
        btn = Button(m, text=text, command=calculate, font=font_style, width=button_width, height=button_height, bg="#31363F")
        btn.grid(row=row, column=col, padx=5, pady=10)
    elif text == 'x²':
        btn = Button(m, text=text, command=lambda: update_input('**2'), font=font_style, width=button_width, height=button_height)
        btn.grid(row=row, column=col, padx=5, pady=10)
    elif text == 'C':
        btn = Button(m, text=text, command=clear_input, font=font_style, width=8, height=button_height, bg="#76ABAE")
        btn.grid(row=row, column=col, padx=5, pady=10, columnspan=2)
    else:
        btn = Button(m, text=text, command=lambda t=text: update_input(t), font=font_style, width=button_width, height=button_height)
        btn.grid(row=row, column=col, padx=5, pady=10)

m.mainloop()
