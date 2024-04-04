from graphics.screens.Screen import Screen
import tkinter as tk

class HomeScreen(Screen):
    def __init__(self) -> None:
        pass

    def display(self, root, config):
        tk.Label(root, text="This is the home screen!").pack()
        tk.Button(root, text="Tutorial", command=lambda: config.get("callback")("TUTORIAL", config)).pack()
        tk.Button(root, text="Details", command=lambda: config.get("callback")("DETAILS", config)).pack()
