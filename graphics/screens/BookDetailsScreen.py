from graphics.screens.Screen import Screen
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk

class BookDetailsScreen(Screen):
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
            command=lambda: config["callback"]("BOOK_SEARCH", newConfig))
        
        # All the info
        bookInfo = self.dfManager.bookMgr.search(config["title"])[0]
        infoFrame = tk.Frame(root, relief="groove", bd=2)
        titleLabel = tk.Label(infoFrame, text=bookInfo[1], font=("Arial", 16))
        authorLabel = tk.Label(infoFrame, text=f"Author: {bookInfo[2]}", font=("Arial", 11))
        genreLabel = tk.Label(infoFrame, text=f"Genre: {bookInfo[3]}", font=("Arial", 11))
        availableLabel = tk.Label(infoFrame, text=f"Availability: {'Available' if bookInfo[4] else 'Checked out'}", font=("Arial", 11))
        descriptionLabel = tk.Label(infoFrame, text=f"Description: {bookInfo[5]}", font=("Arial", 11))
        
        # Checkout widgets
        checkoutFrame = tk.Frame(root, relief="groove", bd=2)
        checkoutLabel = tk.Label(checkoutFrame, text=f"Checkout \"{bookInfo[1]}\"", font=("Arial", 16))
        studentEntry = tk.Entry(checkoutFrame, font=("Arial", 11), width=30)
        studentEntry.bind("<FocusIn>", lambda event: self.__on_entry_click(event, studentEntry))
        studentEntry.bind("<FocusOut>", lambda event: self.__on_focus_out(event, studentEntry))
        self.__on_focus_out(None, studentEntry)
        checkoutButton = tk.Button(checkoutFrame, text="Checkout", font=("Arial", 11), command=lambda: self.__checkout_callback(root, bookInfo[0], studentEntry))

        root.grid_columnconfigure(2, weight=1)

        quitButton.grid(column=4, row=0, pady=5, padx=5, sticky="e")
        backButton.grid(column=0, row=0, pady=5, padx=5, sticky="w")
        infoFrame.grid(column=0, row=1, padx=5, pady=5, sticky="w")
        titleLabel.grid(column=0, row=0, padx=5, sticky="w")
        authorLabel.grid(column=0, row=1, padx=5, pady=5, sticky="w")
        genreLabel.grid(column=0, row=2, padx=5, pady=5, sticky="w")
        availableLabel.grid(column=0, row=3, padx=5, pady=5, sticky="w")
        descriptionLabel.grid(column=0, row=4, padx=5, pady=5, sticky="w")

        checkoutFrame.grid(column=0, row=2, padx=5, pady=5, sticky="w")
        checkoutLabel.grid(column=0, row=0, sticky="w")
        studentEntry.grid(column=0, row=1, columnspan=2, padx=5, pady=5, sticky="w")
        checkoutButton.grid(column=2, row=1, padx=5, pady=5)

    def __on_entry_click(self, event, entry):
        if entry.get() == "Enter student ID...":
            entry.delete(0, tk.END)
            entry.configure(foreground="black")

    def __on_focus_out(self, event, entry):
        if entry.get() == "":
            entry.insert(0, "Enter student ID...")
            entry.configure(foreground="gray")

    def __checkout_callback(self, root, bookID, entry):
        studentID = entry.get()
        try:
            # Make sure the ID provided is numeric
            if studentID.isnumeric():
                studentID = int(studentID)
            else:
                raise Exception("Invalid student ID")
            
            self.dfManager.studentMgr.checkout(studentID, bookID, self.dfManager.bookMgr)
        except Exception as error:
            entry.delete(0, 'end')
            messagebox.showerror("Checkout Error", f"Error: {error}")

