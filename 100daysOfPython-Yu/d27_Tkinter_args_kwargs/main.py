import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="This is a label", font=("Arial", 24, "italic"))
my_label.pack(side='top')


#button
def button_clicked():
    my_label.config(text=input.get())

button = tk.Button(text="Click Me", command=button_clicked)
button.pack(side='top')

# Entry
input = tk.Entry(width=10)
input.pack()
input.get()

window.mainloop()
