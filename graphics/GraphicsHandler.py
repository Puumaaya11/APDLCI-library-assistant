import tkinter as tk
from graphics.screens.DetailsScreen import DetailsScreen
from graphics.screens.HomeScreen import HomeScreen
from graphics.screens.TutorialScreen import TutorialScreen


class GraphicsHandler:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.screenList = {
            "HOME": HomeScreen(),
            "DETAILS": DetailsScreen(),
            "TUTORIAL": TutorialScreen()
        }
    
    def changeScreen(self, screen, config):
        self.removeChildren()
        self.screenList.get(screen).display(self.root, config)
        self.root.mainloop()

    def removeChildren(self):
        for child in self.root.winfo_children():
            child.destroy()