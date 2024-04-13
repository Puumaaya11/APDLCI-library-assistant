from graphics.screens.Screen import Screen
import tkinter as tk
import tkinter.ttk as ttk

class BookDetailsScreen(Screen):
    def __init__(self, dfManager):
        Screen.__init__(self, dfManager)

    def display(self, root, config):
        newConfig = {
            "callback": config["callback"]
        }
        backButton = tk.Button(
            root, 
            text="Search",
            font=("Arial", 11),
            command=lambda: config["callback"]("BOOK_SEARCH", newConfig))
        
        titleLabel = tk.Label(root, text=config["title"], font=("Arial", 16))

        backButton.grid(column=0, row=0, pady=5)
        titleLabel.grid(column=0, row=1, padx=5)