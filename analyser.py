import tkinter as tk

# Creating the window
root = tk.Tk()
root.title("Code Analyser")
root["background"] = "#303030"

# Creating the intro label
intro_label = tk.Label(root, text = "Code Analyser. \n Type in the tests you want to do")
intro_label["background"] = "#303030"
intro_label["foreground"] = "#FFFFFF"
intro_label["font"] = ("Noto Sans", 25)
intro_label["padx"] = 40
intro_label["pady"] = 30
intro_label.grid(row = 0, column = 0, columnspan = 2)

# Creating the frame for the options
options_frame = tk.LabelFrame(root, text = "Options")
options_frame["background"] = "#303030"
options_frame["foreground"] = "#FFFFFF"
options_frame["font"] = ("Noto Sans", 14)
options_frame["padx"] = 40
options_frame["pady"] = 30
options_frame.grid(row = 1, column = 0, columnspan = 2)

class item:
    def __init__(self, master, name):
        self.box = tk.LabelFrame(master, text = name, padx = 20, pady = 20)
        self.box["background"] = "#505050"
        self.box["foreground"] = "#FFFFFF"
        self.box["font"] = ("Noto Sans", 14)

        self.program_var = tk.StringVar()
        self.args_var = tk.StringVar()
        self.input_var = tk.StringVar()
        self.output_var = tk.StringVar()
        self.ref_var = tk.StringVar()
        self.check = tk.BooleanVar()
        
        self.program_entry = tk.Entry(self.box, textvariable = self.program_var,
                                      font = ("Noto Sans", 14), bg = "#505050", fg = "#FFFFFF")
        self.args_entry = tk.Entry(self.box, textvariable = self.args_var, 
                                   font = ("Noto Sans", 14), bg = "#505050", fg = "#FFFFFF")
        self.input_entry = tk.Entry(self.box, textvariable = self.input_var, 
                                    font = ("Noto Sans", 14), bg = "#505050", fg = "#FFFFFF")
        self.output_entry = tk.Entry(self.box, textvariable = self.output_var,
                                      font = ("Noto Sans", 14), bg = "#505050", fg = "#FFFFFF")
        self.ref_entry = tk.Entry(self.box, textvariable = self.ref_var,
                                      font = ("Noto Sans", 14), bg = "#505050", fg = "#FFFFFF")
        self.checkbox = tk.Checkbutton(self.box, text = "Measure", variable = self.check,
                                        onvalue = True, offvalue = False, font = ("Noto Sans", 14),
                                        bg = "#505050", fg = "#FFFFFF")

        self.program_entry.grid(row = 0, column = 0)
        self.args_entry.grid(row = 0, column = 1)
        self.input_entry.grid(row = 0, column = 2)
        self.output_entry.grid(row = 0, column = 3)
        self.ref_entry.grid(row = 1, column = 1)
        self.checkbox.grid(row = 1, column = 2)
        self.box.pack()

    def get_command(self):
        command = dict()
        command["sys"] = self.program_var.get()
        command["sys"] += " " + self.args_var.get()
        command["sys"] += " < " + self.input_var.get()
        command["sys"] += " > " + self.output_var.get()
        command["sys"] += " 2>> " + "temp.log"
        command["ref"] = self.ref_var.get()
        command["measure"] = self.check.get()
        return command
    
items = []
number = 1
def add_item():
    global number
    items.append(item(options_frame, f"Item {number}"))
    number += 1


# Button to add an item
add_button = tk.Button(root, text = "+", command = add_item)
add_button["background"] = "#505050"
add_button["foreground"] = "#FFFFFF"
add_button["font"] = ("Noto Sans", 20)
add_button["padx"] = 40
add_button["pady"] = 30
add_button.grid(row = 2, column = 0)

# Button to submit
def submit():
    for it in items:
        print(it.get_command())

submit_button = tk.Button(root, text = "Submit", command = submit)
submit_button["background"] = "#505050"
submit_button["foreground"] = "#FFFFFF"
submit_button["font"] = ("Noto Sans", 20)
submit_button["padx"] = 40
submit_button["pady"] = 30
submit_button.grid(row = 2, column = 1)

# Display the window
root.mainloop()

