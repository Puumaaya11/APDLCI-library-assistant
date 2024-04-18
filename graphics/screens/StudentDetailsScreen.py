from graphics.screens.Screen import Screen
from tkinter import messagebox
from tkinter.messagebox import askyesno
import tkinter as tk
import tkinter.ttk as ttk
import numpy
import datetime
import pandas as pd

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
        studentInfo = self.dfManager.studentMgr.search(config["name"])
        nameLabel = tk.Label(root, text=studentInfo[0][1], font=("Arial", 16))
        idLabel = tk.Label(root, text=f"Student ID: {studentInfo[0][0]}", font=("Arial", 11))
        filler = tk.Frame(root, height=20)

        bookFrame = tk.Frame(root, bd=4, relief="groove")
        bookListLabel = tk.Label(bookFrame, text="Books checked out:", font=("Arial", 16))
        titleLabel = tk.Label(bookFrame, text="Title", font=("Arial", 11))
        checkedOutLabel = tk.Label(bookFrame, text="Checked Out", font=("Arial", 11))
        dueByLabel = tk.Label(bookFrame, text="Due Date", font=("Arial", 11))
        separator = ttk.Separator(bookFrame, orient="horizontal")

        # Book list widgets
        books = []
        if not numpy.isnan(studentInfo[0][2]):
            books = [self.dfManager.bookMgr.search(x[2])[0] for x in studentInfo]

        for i in range(len(books)):
            curTitle = tk.Label(bookFrame, text=books[i][1], font=("Arial", 11))

            curCheckedOutDateValue = datetime.datetime.fromisoformat(studentInfo[i][3]).date()
            curDueByDateValue = datetime.datetime.fromisoformat(studentInfo[i][4]).date()
            color = "#f00" if pd.Timestamp.today().date() > curDueByDateValue else "#000"
            curCheckedOutDate = tk.Label(bookFrame, text=curCheckedOutDateValue, font=("Arial", 11))
            curDueByDate = tk.Label(bookFrame, text=curDueByDateValue, font=("Arial", 11), fg=color)
        
            buttonFrame = tk.Frame(bookFrame)
            curReturnButton = tk.Button(buttonFrame, text="Return", font=("Arial", 11), command=lambda book=books[i], studentId=studentInfo[0][0]: self.__return_callback(book, studentId, config))
            curRenewButton = tk.Button(buttonFrame, text="Renew", font=("Arial", 11), command=lambda book=books[i], studentId=studentInfo[0][0]: self.__renew_callback(book, studentId, config))
            
            curTitle.grid(column=0, row=3+i, padx=5, sticky="w")
            curCheckedOutDate.grid(column=1, row=3+i, padx=5, sticky="w")
            curDueByDate.grid(column=2, row=3+i, padx=5, sticky="w")

            buttonFrame.grid(column=3, row=3+i, pady=2, sticky="e")
            curReturnButton.grid(column=0, row=0, padx=5)
            curRenewButton.grid(column=1, row=0, padx=5)

        root.grid_columnconfigure(2, weight=1)

        # Formatting the layout on the grid
        quitButton.grid(column=2, row=0, pady=5, padx=5, sticky="e")
        backButton.grid(column=0, row=0, pady=5, padx=5, sticky="w")
        nameLabel.grid(column=0, row=1, pady=5, padx=5, sticky="w")
        idLabel.grid(column=0, row=2, pady=5, padx=5, sticky="w")
        filler.grid(column=0, row=3, sticky="w")

        bookFrame.grid(column=0, row=4, pady=5, padx=5, sticky="w")
        bookListLabel.grid(column=0, row=0, pady=5, padx=5, sticky="w")
        titleLabel.grid(column=0, row=1, padx=5, sticky="w")
        checkedOutLabel.grid(column=1, row=1, padx=5, sticky="w")
        dueByLabel.grid(column=2, row=1, padx=5, sticky="w")
        separator.grid(column=0, row=2, sticky="ew", columnspan=4)


    # Event callbacks
    def __return_callback(self, book, studentID, config):
        answer = askyesno(title="Return", message=f"Return {book[1]}?")
        if answer:
            self.dfManager.studentMgr.ret(studentID, book[0], self.dfManager.bookMgr)
            config["callback"]("STUDENT_DETAILS", config)

    def __renew_callback(self, book, studentID, config): 
        answer = askyesno(title="Renew", message=f"Renew {book[1]}?")
        if answer:
            self.dfManager.studentMgr.renew(studentID, book[0])
            config["callback"]("STUDENT_DETAILS", config)