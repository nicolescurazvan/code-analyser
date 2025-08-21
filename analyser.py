import tkinter as tk
import time
import os

class Item(tk.LabelFrame):
    def __init__(self, parent, name):
        super().__init__(master = parent)
        self.type = name
        self["padx"] = self["pady"] = 5
        self["text"] = name
        self["bg"] = "#404040"
        self["fg"] = "#FFFFFF"
        
        # Program input
        self.program_label = tk.Label(self, text = "Program")
        self.program_label.grid(row = 0, column = 0)
        self.program_var = tk.StringVar()
        self.program = tk.Entry(self, textvariable = self.program_var)
        self.program.grid(row = 0, column = 1, columnspan = 2)

        # Args input
        self.args_label = tk.Label(self, text = "Args")
        self.args_label.grid(row = 1, column = 0)
        self.args_var = tk.StringVar()
        self.args = tk.Entry(self, textvariable = self.args_var)
        self.args.grid(row = 1, column = 1, columnspan = 2)

        # Input file input
        self.input_label = tk.Label(self, text = "Input file")
        self.input_label.grid(row = 2, column = 0)
        self.input_var = tk.StringVar()
        self.input = tk.Entry(self, textvariable = self.input_var)
        self.input.grid(row = 2, column = 1, columnspan = 2)

        # Ref file input
        self.ref_label = tk.Label(self, text = "Reference file")
        if self.type == "Checker":
            self.ref_label.grid(row = 3, column = 0)
        self.ref_var = tk.StringVar()
        self.ref = tk.Entry(self, textvariable = self.ref_var)
        if self.type == "Checker":
            self.ref.grid(row = 3, column = 1, columnspan = 2)
        
        self.pack()

    def run(self):
        exec = "python3 " if self.program_var.get()[-3:] == ".py" else "./"
        program = self.program_var.get()
        args = self.args_var.get()
        input = self.input_var.get()
        output = "out.txt"
        if self.type == "Checker":
            ref = self.ref_var.get()
            os.system(f"{exec}{program} {args} < {input} > {output} 2>> report.log")
            os.system(f"diff {output} {ref} >> report.log")
        else:
            t = time()
            os.system(f"{exec}{program} {args} < {input} > {output} 2>> report.log")
            t = time() - t
            print(t)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Code analyser")
        self.geometry("900x900")
        self.config(background = "#303030")
        
        # Create the intro label
        self.intro = tk.Label(self)
        self.intro["text"] = "Press the '+' to insert a command\n" \
                            "Press the submit button to run the tests\n" \
                            "Choose the right test for you:\n" \
                            "1) Checker, to see if the program runs correctly\n" \
                            "2) Measure, to see how fast a program runs"
        self.intro["font"] = ("Noto Sans", 15)
        self.intro["bg"] = "#303030"
        self.intro["fg"] = "#FFFFFF"
        self.intro.grid(row = 0, column = 0, columnspan = 3)

        # Create the options frame
        self.options = tk.Frame(self)
        self.options["bg"] = "#404040"
        self.options.grid(row = 1, column = 0, columnspan = 3)
        self.items = []

        # Create the buttons
        self.plus_c = tk.Button(self, text = "New Checker")
        self.plus_c["font"] = ("Noto Sans", 15)
        self.plus_c["bg"] = "#303030"
        self.plus_c["fg"] = "#FFFFFF"
        self.plus_c["command"] = lambda: self.items.append(Item(self.options, "Checker"))
        self.plus_c.grid(row = 2, column = 0)

        self.plus_m = tk.Button(self, text = "New Measure")
        self.plus_m["font"] = ("Noto Sans", 15)
        self.plus_m["bg"] = "#303030"
        self.plus_m["fg"] = "#FFFFFF"
        self.plus_m["command"] = lambda: self.items.append(Item(self.options, "Measure"))
        self.plus_m.grid(row = 2, column = 1)

        self.submit = tk.Button(self, text = "Submit")
        self.submit["font"] = ("Noto Sans", 15)
        self.submit["bg"] = "#303030"
        self.submit["fg"] = "#FFFFFF"
        self.submit["command"] = lambda: print("\n".join([it.run() for it in self.items]))
        self.submit.grid(row = 2, column = 2)


if __name__ == "__main__":
    app = App()
    app.mainloop()