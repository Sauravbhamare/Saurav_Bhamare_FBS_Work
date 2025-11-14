from tkinter import *
from tkinter import messagebox

def add():
    calculate('+')

def subtract():
    calculate('-')

def multiply():
    calculate('*')

def divide():
    calculate('/')

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2

        label_result.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")

if __name__ == '__main__':
    window = Tk()
    window.title("Basic Calculator")
    window.geometry("300x350")
    window.config(bg="black")

    frame1 = Frame(window, bg="black")
    frame2 = Frame(window, bg="black")
    frame3 = Frame(window, bg="black")
    frame4 = Frame(window, bg="black")

    
    Label(frame1, text="Basic Calculator", font=("Arial", 14, "bold"), fg="white", bg="black").pack(pady=10)
    frame1.pack()

    
    Label(frame2, text="Number 1:", fg="white", bg="black").grid(row=0, column=0, pady=5)
    entry1 = Entry(frame2)
    entry1.grid(row=0, column=1, pady=5)

    Label(frame2, text="Number 2:", fg="white", bg="black").grid(row=1, column=0, pady=5)
    entry2 = Entry(frame2)
    entry2.grid(row=1, column=1, pady=5)
    frame2.pack(pady=10)

    
    Button(frame3, text="+", width=5, command=add).grid(row=0, column=0, padx=5, pady=5)
    Button(frame3, text="-", width=5, command=subtract).grid(row=0, column=1, padx=5, pady=5)
    Button(frame3, text="*", width=5, command=multiply).grid(row=0, column=2, padx=5, pady=5)
    Button(frame3, text="/", width=5, command=divide).grid(row=0, column=3, padx=5, pady=5)
    frame3.pack()


    label_result = Label(frame4, text="Result: ", font=("Arial", 12, "bold"), fg="yellow", bg="black")
    label_result.pack(pady=20)
    frame4.pack()

    window.mainloop()
