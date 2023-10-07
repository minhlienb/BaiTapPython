from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Style, Entry

class Calculator(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calculator")

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        # Entry widget to display the input and result
        self.entry = Entry(self)
        self.entry.grid(row=0, columnspan=4, sticky=W+E)

        # Button labels
        button_labels = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        # Create buttons and assign them click handlers
        row = 1
        col = 0
        for label in button_labels:
            Button(self, text=label, command=lambda l=label: self.on_button_click(l)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.pack()

    def on_button_click(self, label):
        current_text = self.entry.get()

        if label == "=":
            try:
                # Evaluate the expression and display the result
                result = str(eval(current_text))
                self.entry.delete(0, "end")
                self.entry.insert("end", result)
            except Exception as e:
                # Handle errors in the expression
                self.entry.delete(0, "end")
                self.entry.insert("end", "Error")
        elif label == "Cls":
            # Clear the input field
            self.entry.delete(0, "end")
        elif label == "Back":
            # Remove the last character from the input field
            self.entry.delete(len(current_text) - 1, "end")
        else:
            # Append the clicked button's label to the input field
            self.entry.insert("end", label)

def main():
    root = Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
