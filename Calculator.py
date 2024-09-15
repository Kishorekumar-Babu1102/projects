import tkinter as tk

def click(event):
    global expression
    expression += event.widget.cget("text")
    display_var.set(expression)

def calculate():
    try:
        global expression
        result = str(eval(expression))
        display_var.set(result)
        expression = ""
    except Exception as e:
        display_var.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    display_var.set("")

root = tk.Tk()
root.title("Simple Calculator")

expression = ""
display_var = tk.StringVar()

# Display
display = tk.Entry(root, textvar=display_var, font="Arial 20 bold", bd=10, insertwidth=2, width=14, justify="right")
display.grid(row=0, column=0, columnspan=4)

# Button creation
buttons = [
    '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', 'C', '0', '=', '+'
]

row_value = 1
col_value = 0
for button in buttons:
    btn = tk.Button(root, text=button, font="Arial 15 bold", width=5, height=2)
    btn.grid(row=row_value, column=col_value)
    
    if button == "=":
        btn.bind('<Button-1>', lambda e: calculate())
    elif button == "C":
        btn.bind('<Button-1>', lambda e: clear())
    else:
        btn.bind('<Button-1>', click)
    
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

root.mainloop()
