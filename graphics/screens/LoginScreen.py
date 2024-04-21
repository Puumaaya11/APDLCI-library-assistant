from graphics.screens.Screen import Screen
import tkinter as tk
from tkinter import messagebox

class LoginScreen(Screen):
    def __init__(self, dfManager, credentialManager=None):
        Screen.__init__(self, dfManager, credentialManager)

    def display(self, root, config):
        quitButton = tk.Button(root, text="Quit", font=("Arial", 11), command=root.destroy)
        padding = tk.Frame(root)
        titleLabel = tk.Label(root, text="Library Assistant", font=("Arial", 20))
        usernameLabel = tk.Label(root, text="Username:", font=("Arial", 11))
        passwordLabel = tk.Label(root, text="Password:", font=("Arial", 11))
        usernameEntry = tk.Entry(root, width=30, font=("Arial", 11))
        passwordEntry = tk.Entry(root, width=30, font=("Arial", 11), show="*")
        loginButton = tk.Button(root, text="Login", font=("Arial", 11), command=lambda: self.__login_callback(usernameEntry, passwordEntry, config))

        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(3, weight=1)

        quitButton.grid(column=3, row=0, pady=5, padx=5, sticky="e")
        padding.grid(column=0, row=0, pady=5, padx=5, sticky="w")
        titleLabel.grid(column=1, row=1, columnspan=2, padx=5, pady=10, sticky="ew")
        usernameLabel.grid(column=1, row=2, padx=5, pady=5, sticky="w")
        usernameEntry.grid(column=2, row=2, padx=5, pady=5, sticky="e")
        passwordLabel.grid(column=1, row=3, padx=5, pady=5, sticky="w")
        passwordEntry.grid(column=2, row=3, padx=5, pady=5, sticky="e")
        loginButton.grid(column=1, row=4, columnspan=2, pady=5, padx=5)

    def __login_callback(self, usernameEntry, passwordEntry, config):
        username = usernameEntry.get()
        password = passwordEntry.get()
        if self.credentialManager.login(username, password):
             config["callback"]("MAIN_MENU", config)
        else:
            usernameEntry.delete(0, 'end')
            passwordEntry.delete(0, 'end')
            messagebox.showerror("Login Error", "Error: Invalid credentials")


        