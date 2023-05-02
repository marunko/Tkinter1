import tkinter as tk

# Create the main window
root = tk.Tk()

# Create the Listbox
listbox = tk.Listbox(root, width=50)

# Create a function to remove the selected item from the Listbox
def remove_item():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        listbox.delete(index)

# Create the Button widget to remove the selected item
button = tk.Button(root, text="Remove", command=remove_item)

# Add some items to the Listbox
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
    listbox.insert(tk.END, item)

# Pack the Listbox and Button widgets
listbox.pack()
button.pack()

# Start the main event loop
root.mainloop()