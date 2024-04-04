from graphics.screens.Screen import Screen
import tkinter as tk

class DetailsScreen(Screen):
    def __init__(self) -> None:
        pass

    def display(self, root, config):
        tk.Label(root, text="This is the details screen!").pack()
        tk.Button(root, text="Home", command=lambda: config.get("callback")("HOME", config)).pack()
        tk.Button(root, text="Tutorial", command=lambda: config.get("callback")("TUTORIAL", config)).pack()
