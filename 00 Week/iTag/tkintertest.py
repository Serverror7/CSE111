# Import Module
from tkinter import *
from iTag_tasks_generator import task_list_import, task_selector, select_tasks

# create root window
root = Tk()
# root window title and dimension
root.title("Welcome to iTag")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New Game')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding a label to the rootc window
lbl = Label(root, text = "Would you like to play a game?")
lbl.grid()

# function to display user text when
# button is clicked
def clicked():	
    tasks = task_list_import(r"D:\Documents\Python\00 Week\iTag\tasklist.txt")
    shuffled_task_list = task_selector(tasks)
    shuffled_task_list, current_task = select_tasks(shuffled_task_list, 5)
    res = current_task
    lbl.configure(text = res)
pass

# button widget with red color text inside
btn = Button(root, text = "Click me" ,
			fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)

# Execute Tkinter
root.mainloop()
