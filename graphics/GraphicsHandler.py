import tkinter as tk
from graphics.screens.BookSearchScreen import BookSearchScreen
from graphics.screens.BookDetailsScreen import BookDetailsScreen
from graphics.screens.MainMenuScreen import MainMenuScreen
from graphics.screens.LoginScreen import LoginScreen
from graphics.screens.StudentSearchScreen import StudentSearchScreen
from graphics.screens.StudentDetailsScreen import StudentDetailsScreen
from graphics.screens.ManageScreen import ManageScreen
from data.Dataframes import Dataframes
from credentials.CredentialManager import CredentialManager


class GraphicsHandler:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Library Assistant")
        self.root.geometry("700x600")

        dfManager = Dataframes()
        credentialManager = CredentialManager(dfManager)
        self.screenList = {
            "BOOK_SEARCH": BookSearchScreen(dfManager),
            "BOOK_DETAILS": BookDetailsScreen(dfManager),
            "MAIN_MENU": MainMenuScreen(dfManager),
            "LOGIN": LoginScreen(dfManager, credentialManager),
            "STUDENT_SEARCH": StudentSearchScreen(dfManager),
            "STUDENT_DETAILS": StudentDetailsScreen(dfManager),
            "MANAGE": ManageScreen(dfManager, credentialManager)
        }
    
    def changeScreen(self, screen, config):
        self.__removeChildren()
        for i in range(10):
            self.root.grid_columnconfigure(i, weight=0)
        self.screenList.get(screen).display(self.root, config)
        self.root.mainloop()

    def __removeChildren(self):
        for child in self.root.winfo_children():
            child.destroy()