from tkinter import *
from tkinter import messagebox
rates = {
    "INR":1,
    "USD":0.012,
    "EUR":0.011,
    "GBP":0.0095,
    "JPY":1.74
}

def convert():
    try:
        amount = float(entry1.get())
        from_curr = x.get()
        to_curr = y.get()
        
        if from_curr not in rates or to_curr not in rates:
            messagebox.showerror("Error", "Invalid Currency selelction!")
            return
        
        inr_value = amount / rates[from_curr]
        converted = inr_value * rates[to_curr]
        
        messagebox.showinfo("Conversion Result:",
                            f"{from_curr} = {to_curr}")
    except ValueError as e:
        messagebox.showwarning("Invalid Input", "Please enter a valid Amount!")

if(__name__ == '__main__'):
    window = Tk()
    window.title('Currency Converter')
    window.config(background='black')
    window.geometry('300x400')
    
    frame1 = Frame(window)
    frame2 = Frame(window)
    frame3 = Frame(window)
    frame4 = Frame(window)
    
    label1 = Label(frame1, text="Currency Converter")
    label1.pack(pady=10)
    frame1.pack()
    
    label2 = Label(frame2, text="Amount:")
    label2.grid(row=0, column=0, pady=5)
    entry1 = Entry(frame2)
    entry1.grid(row=0, column=1, pady=5)
    
    frame2.pack()
    
    label3 = Label(frame3, text='From:')
    label3.grid(row=0, column=0, pady=5)
    x = StringVar(window)
    x.set("INR")
    OptionMenu(frame3,x,*rates.keys()).grid(row=0, column=1,pady=5)
    
    label4 = Label(frame3, text="TO:")
    label4.grid(row=1, column=0, pady=5)
    y = StringVar(window)
    y.set("USD")
    OptionMenu(frame3,y,*rates.keys()).grid(row=1, column=1,pady=5)
    frame3.pack()
    
    btn_convert = Button(frame4, text="Convert", width=10)
    btn_convert.pack(pady=15)
    frame4.pack()
    window.mainloop()
    
    