from tkinter  import *
import turtle

window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)
window.config(padx=20, pady=20)


my_label = Label(text="I am Label", font=("Arial", 24, "bold"))
my_label.config(text='New Text')
my_label.grid(column=0, row=0)

my_label["text"] = 'New Text'
my_label.config(text="New Text")

input = Entry(width=10)
input.pack()


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text= new_text)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)



button = Button(text="click me",command=button_clicked)

button.pack()











window.mainloop()