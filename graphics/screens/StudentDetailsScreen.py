from graphics.screens.Screen import Screen
from tkinter import messagebox
from tkinter.messagebox import askyesno
import tkinter as tk
import tkinter.ttk as ttk

class StudentDetailsScreen(Screen):
    def __init__(self, dfManager):
        Screen.__init__(self, dfManager)

    def display(self, root, config):
        newConfig = {
            "callback": config["callback"]
        }

        # Navigation buttons
        quitButton = tk.Button(root, text="Quit", font=("Arial", 11), command=root.destroy)
        backButton = tk.Button(
            root, 
            text="Search",
            font=("Arial", 11),
            command=lambda: config["callback"]("STUDENT_SEARCH", newConfig))

        # All the info
        studentInfo = self.dfManager.studentMgr.search(config["first_name"])[0]
        nameLabel = tk.Label(root, text=studentInfo[1] + " " + studentInfo[2], font=("Arial", 16))
        idLabel = tk.Label(root, text=f"Student ID: {studentInfo[0]}", font=("Arial", 11))
        bookListLabel = tk.Label(root, text="Books checked out:", font=("Arial, 11"))
        bookFrame = tk.Frame(root)

        # TODO make this real since it just gives me "[]"
        studentInfo[3] = [102, 104, 108]
        # Book list widgets
        books = [self.dfManager.bookMgr.search(x)[0] for x in studentInfo[3]]
        for i in range(len(studentInfo[3])):
            curFrame = tk.Frame(bookFrame, relief="groove", bd=2, height=10)
            curLabel = tk.Label(curFrame, text=books[i][1], font=("Arial", 11))
            buttonFrame = tk.Frame(curFrame)
            curReturnButton = tk.Button(buttonFrame, text="Return", font=("Arial", 11), command=lambda book=books[i], studentId=studentInfo[0]: self.__return_callback(book, studentId))
            curRenewButton = tk.Button(buttonFrame, text="Renew", font=("Arial", 11), command=lambda book=books[i], studentId=studentInfo[0]: self.__renew_callback(book, studentId))
            
            curFrame.columnconfigure(1, weight=1)
            curFrame.grid(column=0, row=i, padx=5, sticky="we")
            curLabel.grid(column=0, row=0, pady=5, padx=5, sticky="w")
            buttonFrame.grid(column=1, row=0, sticky="e")
            curReturnButton.grid(column=0, row=0, pady=5, padx=5)
            curRenewButton.grid(column=1, row=0, pady=5, padx=5)

        root.grid_columnconfigure(2, weight=1)

        # Formatting the layout on the grid
        quitButton.grid(column=2, row=0, pady=5, padx=5, sticky="e")
        backButton.grid(column=0, row=0, pady=5, padx=5, sticky="w")
        nameLabel.grid(column=0, row=1, pady=5, padx=5, sticky="w")
        idLabel.grid(column=0, row=2, pady=5, padx=5, sticky="w")
        bookListLabel.grid(column=0, row=3, pady=5, padx=5, sticky="w")
        bookFrame.grid(column=0, row=4, pady=5, padx=5, sticky="w")

    # Event callbacks
    def __return_callback(self, book, studentID):
        answer = askyesno(title="Return", message=f"Return {book[1]}?")
        print(answer)

    def __renew_callback(self, book, studentID): 
        answer = askyesno(title="Renew", message=f"Renew {book[1]}?")
        print(answer)