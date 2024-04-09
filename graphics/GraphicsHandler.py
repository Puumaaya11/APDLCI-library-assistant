import tkinter as tk
from graphics.screens.BookSearchScreen import BookSearchScreen
from graphics.screens.MainMenuScreen import MainMenuScreen


class GraphicsHandler:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Library Assistant")
        self.root.geometry("1000x600")
        self.screenList = {
            "BOOK_SEARCH": BookSearchScreen(),
            "MAIN_MENU": MainMenuScreen()
        }
    
    def changeScreen(self, screen, config):
        self.removeChildren()
        self.screenList.get(screen).display(self.root, config)
        self.root.mainloop()

    def removeChildren(self):
        for child in self.root.winfo_children():
            child.destroy()