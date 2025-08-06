import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Code Analyser")
root.geometry("1280x800")
root["background"] = "#303030"

intro = ttk.Label(root, text="Choose the tests you want to make. \n \
                  1) Checker: Checks whether the code is correct or not \n\
                  2) Benchmark: Measure how fast a program runs")
intro["background"] = "#303030"
intro["foreground"] = "#ffffff"
intro["font"] = ("Noto Sans", 16)
intro.pack()

mainField = ttk.Label(root, background="#303030", foreground="#ffffff", font=("Noto Sans", 14))
mainField.pack()

submitBtn = ttk.Button(root, text = "Submit")
intro["background"] = "#303030"
intro["foreground"] = "#ffffff"
intro["font"] = ("Noto Sans", 16)
submitBtn.pack()

root.mainloop()

