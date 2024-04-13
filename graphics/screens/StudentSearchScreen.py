from graphics.screens.Screen import Screen
import tkinter as tk

class StudentSearchScreen(Screen):
    def __init__(self, dfManager):
        Screen.__init__(self, dfManager)

    def display(self, root, config):
        tempLabel = tk.Label(root, text="Student Search")
        tempLabel.pack()