import tkinter as tk
from graphics.screens.BookSearchScreen import BookSearchScreen
from graphics.screens.BookDetailsScreen import BookDetailsScreen
from graphics.screens.MainMenuScreen import MainMenuScreen
from graphics.screens.LogoutScreen import LogoutScreen
from graphics.screens.StudentSearchScreen import StudentSearchScreen
from graphics.screens.StudentDetailsScreen import StudentDetailsScreen
from graphics.screens.ManageScreen import ManageScreen
from data.Dataframes import Dataframes


class GraphicsHandler:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Library Assistant")
        self.root.geometry("700x600")

        dfManager = Dataframes()
        self.screenList = {
            "BOOK_SEARCH": BookSearchScreen(dfManager),
            "BOOK_DETAILS": BookDetailsScreen(dfManager),
            "MAIN_MENU": MainMenuScreen(dfManager),
            "LOGOUT": LogoutScreen(dfManager),
            "STUDENT_SEARCH": StudentSearchScreen(dfManager),
            "STUDENT_DETAILS": StudentDetailsScreen(dfManager),
            "MANAGE": ManageScreen(dfManager)
        }
    
    def changeScreen(self, screen, config):
        self.__removeChildren()
        self.screenList.get(screen).display(self.root, config)
        self.root.mainloop()

    def __removeChildren(self):
        for child in self.root.winfo_children():
            child.destroy()