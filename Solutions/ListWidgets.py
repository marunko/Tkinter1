import tkinter as tk
class Field:
    def __init__(self):
        self.packANote()
        return

    def packANote(self):
        self.button1 = tk.Button(text="add")
        self.label = tk.Label(text="some text")
        self.button2 = tk.Button(text="remove")
        self.button1.grid(row=0, column=2)
        self.label.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)


# Create the main window
root = tk.Tk()
root.geometry("500x500")
# Create the Listbox
listbox = tk.Listbox(root, width=50)

fields = [Field(),Field(),Field(),Field()]

# Add some items to the Listbox
for item in fields:
    listbox.insert(tk.END, item)

# Pack the Listbox and Button widgets
listbox.grid()


# Start the main event loop
root.mainloop()