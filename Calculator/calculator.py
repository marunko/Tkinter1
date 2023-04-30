import tkinter as tk
import numpy as np
class CalculatorWindow:
    data = "0" # string data number
    entry = None


    def __init__(self, root):
        # init Entry
        self.root = root
        #self.entry = tk.Entry()
        self.entry = tk.Label(root, text=self.data)
        self.entry.grid(row=0, column=0, columnspan=4)
        tk.Grid.rowconfigure(root, 0, weight=1)

        tk.Grid.columnconfigure(root, 0, weight=1)
        tk.Grid.columnconfigure(root, 1, weight=1)
        tk.Grid.columnconfigure(root, 2, weight=1)
        tk.Grid.columnconfigure(root, 3, weight=1)
        self.buttonsNumbers = np.empty(10, dtype=object)
        self.loadButtons()
        return

    def loadButtons(self):
        self.initNumbersButtons()
        self.functionalButtons = {
            "clear": tk.Button(text="clear", command=self.clearAll)
        }

        self.functionalButtons["clear"].grid(row=4, column=1, padx=2,sticky="nsew")
        return 1

    def initNumbersButtons(self):
        #tk.Label(text=len(self.buttonsNumbers)).pack()
        row=1
        column=0
        k=1
        for i in range(1,10):
            f = lambda i=i: self.buttonNumberClicked(i)
            self.buttonsNumbers[i] = tk.Button(self.root, text=i,
                        command=f)\
                .grid(row=row, column=column, padx=2, sticky="nsew")
            tk.Grid.rowconfigure(root, row, weight=1)

            if(column >=2):
                row += 1
                column = 0
            else: column += 1

        self.buttonsNumbers[0] = tk.Button(self.root, text=0,
                                           command=lambda: self.buttonNumberClicked(0))\
               .grid(row=row, column=0, padx=2, sticky="nsew")
        tk.Grid.rowconfigure(root, row, weight=1)
        return


# number utilization
    def combinenumberToString(self, number):
        number = str(number)
        if len(self.data) > 10:
            return
        if len(self.data) <2:
            if self.data == "0":
                self.data = number
            else:
                self.data +=number
        else:
            self.data +=number
        return

    def revertToNumber(self):

        return

# functional
    def buttonNumberClicked(self, number):
        self.combinenumberToString(number)
        self.entry.config(text=self.data)


    def addNumber(self):

        return

    def multiply(self):
        return
    def clearAll(self):
        self.data ="0"
        self.entry.config(text=self.data)
        return


root = tk.Tk()
root.title("Calculator")
# config row and columns sizes


calculatorW = CalculatorWindow(root)

root.geometry("400x400")
root.mainloop()

