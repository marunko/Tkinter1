from tkinter import *
from tkinter import ttk
import Widgets.grid
import Widgets.buttons
import Widgets.entry

# starts main window
root = Tk()

#Widgets.grid.setGrid(root)
e = Widgets.entry.setEntry(root)
Widgets.buttons.counterButton(root, e)

root.mainloop()

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    # print(111)
