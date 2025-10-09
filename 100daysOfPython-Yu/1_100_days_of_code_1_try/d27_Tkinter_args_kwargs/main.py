import tkinter as tk

window = tk.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=600)

#Label
my_label = tk.Label(text='I am a Label', font=('Arial', 24, 'bold'))
my_label.pack()

#Entry
input = tk.Entry(width=30)
input.pack()


#Button
def button_clicked():
    new_input = input.get()
    my_label.config(text=new_input)


my_botton = tk.Button(text='Change title', command=button_clicked)
my_botton.pack()

#Text field
text = tk.Text(height=5, width=30, borderwidth=5, relief="ridge", bg='light blue')
text.pack()

#Spinbox
spinbox = tk.Spinbox(from_=0, to=10, width=10)
spinbox.pack()

#Scale
scale = tk.Scale(from_=0, to=100, orient='vertical')
scale.pack()

#checkbutton
checkbutton = tk.Checkbutton(text='Is on?', )
checkbutton.pack()

#Radio button
test_radio_button_options = ['Option 1', 'Option 2', 'Option 3']

radio_button = tk.Radiobutton(text=test_radio_button_options)
radio_button.pack()


#write a few lines of own radio buttons to understand how it works!

master = tk.Tk()

test = [
    ("test", 5),
    ("test1", 6),
    ("test2", 7),
    ("test3", 8),
]

def ShowChoice(text, v):
    print(text, v.get())

vartest = tk.IntVar()
vartest.set(test[0][1])

tk.Label(master, text='Choose one answer:').pack()

for txt, val in test:
    tk.Radiobutton(master, text=txt, variable=vartest, value=val,
                   command=lambda t=txt, v=vartest: ShowChoice(t, v)).pack(anchor=tk.N)

window.mainloop()
