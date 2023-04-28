from tkinter import *

theE = None
def counterButton(root, e):
    global theE
    theE = e
    Button(root, text="clickMe", pady=20, command=clickCounterButton).pack()


def clickCounterButton():
    Label(text="Clicked!!"+theE.get()).pack()

# use MVVM where (FMVVM): (F - functional - extra classes DAO responsible)
# View object create window and manage its items depends on<< ModelView class
# MV - manage model, depends on File/DB class

# example

# class WindowMain: - buttons, labels, tables, texts, media >>initiate
# class Main: upload text, runs animations, counts
# class FileManager/DB: uploads data from Files
# class Person, People, Car - models classes

