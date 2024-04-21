from graphics.screens.Screen import Screen
import tkinter as tk

class MainMenuScreen(Screen):
    def __init__(self, dfManager, credentialManager=None):
        Screen.__init__(self, dfManager)

    def display(self, root, config):
        titleLabel = tk.Label(root, text="Main Menu", font=("Arial", 20))

        bookSearchButton = tk.Button(root, text="Search by Book", font=("Arial", 11), command=lambda: config["callback"]("BOOK_SEARCH", config))
        studentSearchButton = tk.Button(root, text="Search by Student", font=("Arial", 11), command=lambda: config["callback"]("STUDENT_SEARCH", config))
        manageButton = tk.Button(root, text="Manage", font=("Arial", 11), command=lambda: config["callback"]("MANAGE", config))
        logoutButton = tk.Button(root, text="Logout", font=("Arial", 11), command=lambda: config["callback"]("LOGIN", config))
        quitButton = tk.Button(root, text="Quit", font=("Arial", 11), command=root.destroy)

        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(2, weight=1)

        logoutButton.grid(row=0, column=0, sticky="w", pady=5, padx=5)
        quitButton.grid(row=0, column=2, sticky="e", pady=5, padx=5)
        titleLabel.grid(row=1, column=1, pady=2)
        bookSearchButton.grid(row=2, column=1, pady=2)
        studentSearchButton.grid(row=3, column=1, pady=2)
        manageButton.grid(row=4, column=1, pady=2)
        
