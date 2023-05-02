import tkinter as tk
import numpy as np
class CalculatorWindow:
    data = "0" # string data number
    entry = None
    resultingValue = "0"
    temporaryValue = 0
    isWaitingAnswer = False

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
        self.signLabel = tk.Label(root, text="")
        self.signLabel.grid(row=0, column=3)
        return

    def loadButtons(self):
        self.initNumbersButtons()
        self.functionalButtons = {
            "clear": tk.Button(text="clear", command=self.clearAll),
            "add": tk.Button(text="+", command=self.buttonAdd),
            "mul": tk.Button(text="x", command=self.clearAll),
            "div": tk.Button(text="%", command=self.clearAll),
            "equal": tk.Button(text="=", command=self.getResult)

        }
        self.functionalButtons["clear"].grid(row=4, column=1, padx=2, sticky="nsew")
        self.functionalButtons["add"].grid(row=1, column=3, padx=2, sticky="nsew")
        self.functionalButtons["mul"].grid(row=2, column=3, padx=2, sticky="nsew")
        self.functionalButtons["div"].grid(row=3, column=3, padx=2, sticky="nsew")
        self.functionalButtons["equal"].grid(row=4, column=3, padx=2, sticky="nsew")
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
# ?
    def revertToNumber(self):
        numeric = int(self.data)

        return numeric

# buttons func
    def buttonNumberClicked(self, number):
        self.combinenumberToString(number)
        self.entry.config(text=self.data)

    def buttonAdd(self):
        # check new entrance?
        if self.isWaitingAnswer:
            self.addNumber()
            self.getResultWithoutEqual()

        else:
            self.temporaryValue = int(self.data)
            self.clearEntry()
            self.signLabel.config(text="+")
            self.isWaitingAnswer =True

    def getResult(self):
        self.data = self.resultingValue
        self.entry.config(text=self.data)
        self.signLabel.config(text="")
        self.isWaitingAnswer = False

    def getResultWithoutEqual(self):
        self.data = self.resultingValue
        self.entry.config(text=self.data)
        self.data = "0"
        #self.isWaitingAnswer = False

# functional

    def clearEntry(self):
        self.data = "0"

        return

    def addNumber(self):
        number = int(self.data)
        if self.resultingValue=="0":
            self.resultingValue = self.temporaryValue + int(self.data)
        else:
            self.resultingValue = int(self.resultingValue) + int(self.data)
        return

    def multiply(self):
        return



    def clearAll(self):
        self.data ="0"
        self.resultingValue="0"
        self.entry.config(text=self.data)
        self.signLabel.config(text="")
        self.isWaitingAnswer = False
        return


root = tk.Tk()
root.title("Calculator")
# config row and columns sizes


calculatorW = CalculatorWindow(root)

root.geometry("400x400")
root.mainloop()

