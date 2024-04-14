from graphics.screens.Screen import Screen
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk

class StudentDetailsScreen(Screen):
    def __init__(self, dfManager):
        Screen.__init__(self, dfManager)

    def display(self, root, config):
        newConfig = {
            "callback": config["callback"]
        }

        # Navigation buttons
        quitButton = tk.Button(root, text="Quit", font=("Arial", 11), command=root.destroy)
        backButton = tk.Button(
            root, 
            text="Search",
            font=("Arial", 11),
            command=lambda: config["callback"]("STUDENT_SEARCH", newConfig))

        tempLabel = tk.Label(root, text=config["first_name"], font=("Arial", 16))

        root.grid_columnconfigure(2, weight=1)

        quitButton.grid(column=2, row=0, pady=5, padx=5, sticky="e")
        backButton.grid(column=0, row=0, pady=5, padx=5, sticky="w")
        tempLabel.grid(column=0, row=1, pady=5, padx=5, sticky="w")

