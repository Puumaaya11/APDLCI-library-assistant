from graphics.screens.Screen import Screen
import tkinter as tk

class TutorialScreen(Screen):
    def __init__(self) -> None:
        pass

    def display(self, root, config):
        tk.Label(root, text="This is the tutorial screen!").pack()
        tk.Button(root, text="Home", command=lambda: config.get("callback")("HOME", config)).pack()
        tk.Button(root, text="Details", command=lambda: config.get("callback")("DETAILS", config)).pack()
