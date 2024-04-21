from graphics.screens.Screen import Screen
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

class ManageScreen(Screen):
    def __init__(self, dfManager, credentialManager=None):
        Screen.__init__(self, dfManager, credentialManager)

    def display(self, root, config):
        mainMenuButton = tk.Button(root, text="Main Menu", font=("Arial", 11), command=lambda: config["callback"]("MAIN_MENU", config))
        quitButton = tk.Button(root, text="Quit", font=("Arial", 11), command=root.destroy)

        # Overall organization and title widgets
        bookTitleLabel = tk.Label(root, text="Manage Books", font=("Arial", 16))
        facultyTitleLabel = tk.Label(root, text="Manage Faculty", font=("Arial", 16))
        bookFrame = tk.Frame(root)
        facultyFrame = tk.Frame(root)
        removeBookFrame = tk.Frame(bookFrame, height=30, bd=2, relief="groove")
        addBookFrame = tk.Frame(bookFrame, height=30, bd=2, relief="groove")
        removeFacultyFrame = tk.Frame(facultyFrame, height=30, bd=2, relief="groove")
        addFacultyFrame = tk.Frame(facultyFrame, height=30, bd=2, relief="groove")

        # Remove book widgets
        removeBookLabel = tk.Label(removeBookFrame, text="Remove Book", font=("Arial", 11))
        removeBookSeparator = ttk.Separator(removeBookFrame, orient="horizontal")
        enterBookIDLabel = tk.Label(removeBookFrame, text="Enter ID:", font=("Arial", 11))
        bookIDEntry = tk.Entry(removeBookFrame, width=20, font=("Arial", 11))
        removeBookSubmitButton = tk.Button(removeBookFrame, text="Submit", font=("Arial", 11), command=lambda: self.__remove_book_callback(bookIDEntry, config))

        # Add book widgets
        addBookLabel = tk.Label(addBookFrame, text="Add Book", font=("Arial", 11))
        addBookSeparator = ttk.Separator(addBookFrame, orient="horizontal")
        enterTitleLabel = tk.Label(addBookFrame, text="Enter Title:", font=("Arial", 11))
        titleEntry = tk.Entry(addBookFrame, width=20, font=("Arial", 11))
        enterAuthorLabel = tk.Label(addBookFrame, text="Enter Author:", font=("Arial", 11))
        authorEntry = tk.Entry(addBookFrame, width=20, font=("Arial", 11))
        enterGenreLabel = tk.Label(addBookFrame, text="Enter Genre:", font=("Arial", 11))
        genreEntry = tk.Entry(addBookFrame, width=20, font=("Arial", 11))
        enterDescriptionLabel = tk.Label(addBookFrame, text="Enter Description:", font=("Arial", 11))
        descriptionTextBox = tk.Text(addBookFrame, width=20, height=10, font=("Arial", 11))
        addBookSubmitButton = tk.Button(addBookFrame, text="Submit", font=("Arial", 11), command=lambda: self.__add_book_callback(titleEntry, authorEntry, genreEntry, descriptionTextBox, config))

        # Remove faculty widgets
        removeFacultyLabel = tk.Label(removeFacultyFrame, text="Remove Faculty", font=("Arial", 11))
        removeFacultySeparator = ttk.Separator(removeFacultyFrame, orient="horizontal")
        enterFacultyIDLabel = tk.Label(removeFacultyFrame, text="Enter ID:", font=("Arial", 11))
        facultyIDEntry = tk.Entry(removeFacultyFrame, width=20, font=("Arial", 11))
        removeFacultySubmitButton = tk.Button(removeFacultyFrame, text="Submit", font=("Arial", 11), command=lambda: self.__remove_faculty_callback(facultyIDEntry, config))

        # Add faculty widgets
        addFacultyLabel = tk.Label(addFacultyFrame, text="Add Faculty", font=("Arial", 11))
        addFacultySeparator = ttk.Separator(addFacultyFrame, orient="horizontal")
        enterNameLabel = tk.Label(addFacultyFrame, text="Enter Name:", font=("Arial", 11))
        nameEntry = tk.Entry(addFacultyFrame, width=20, font=("Arial", 11))
        enterUsernameLabel= tk.Label(addFacultyFrame, text="Enter Username:", font=("Arial", 11))
        usernameEntry = tk.Entry(addFacultyFrame, width=20, font=("Arial", 11))
        enterPasswordLabel = tk.Label(addFacultyFrame, text="Enter Password:", font=("Arial", 11))
        passwordEntry = tk.Entry(addFacultyFrame, width=20, show="*", font=("Arial", 11))
        addFacultySubmitButton = tk.Button(addFacultyFrame, text="Submit", font=("Arial", 11), command=lambda: self.__add_faculty_callback(nameEntry, usernameEntry, passwordEntry, config))

        # Some column configuration stuff
        root.grid_columnconfigure(1, weight=1)
        removeBookFrame.grid_columnconfigure(1, weight=1)

        # Organization grid assignments
        mainMenuButton.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        quitButton.grid(row=0, column=1, pady=5, padx=5, sticky="e")
        bookTitleLabel.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        facultyTitleLabel.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        bookFrame.grid(row=2, column=0)
        facultyFrame.grid(row=2, column=1, sticky="nw")
        removeBookFrame.grid(row=0, column=0, padx=6, sticky="ew")
        addBookFrame.grid(row=1, column=0, padx=6, sticky="ew")
        removeFacultyFrame.grid(row=0, column=0, padx=5, sticky="ew")
        addFacultyFrame.grid(row=1, column=0, padx=5, sticky="ew")

        # Remove book grid assignments
        removeBookLabel.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        removeBookSeparator.grid(row=1, column=0, sticky="ew")
        enterBookIDLabel.grid(row=2, column=0, pady=5, padx=5, sticky="w")
        bookIDEntry.grid(row=2, column=1, pady=5, padx=5, sticky="e")
        removeBookSubmitButton.grid(row=3, column=1, padx=5, pady=5, sticky="e")

        # Add book grid assignments
        addBookLabel.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        addBookSeparator.grid(row=1, column=0, sticky="ew")
        enterTitleLabel.grid(row=3, column=0, pady=5, padx=5, sticky="w")
        titleEntry.grid(row=3, column=1, pady=5, padx=5, sticky="e")
        enterAuthorLabel.grid(row=4, column=0, pady=5, padx=5, sticky="w")
        authorEntry.grid(row=4, column=1, pady=5, padx=5, sticky="e")
        enterGenreLabel.grid(row=5, column=0, pady=5, padx=5, sticky="w")
        genreEntry.grid(row=5, column=1, pady=5, padx=5, sticky="e")
        enterDescriptionLabel.grid(row=6, column=0, pady=5, padx=5, sticky="nw")
        descriptionTextBox.grid(row=6, column=1, pady=5, padx=5, sticky="e")
        addBookSubmitButton.grid(row=7, column=1, padx=5, pady=5, sticky="e")

        # Remove faculty grid assignments
        removeFacultyLabel.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        removeFacultySeparator.grid(row=1, column=0, sticky="ew")
        enterFacultyIDLabel.grid(row=2, column=0, pady=5, padx=5, sticky="w")
        facultyIDEntry.grid(row=2, column=1, pady=5, padx=5, sticky="e")
        removeFacultySubmitButton.grid(row=3, column=1, padx=5, pady=5, sticky="e")

        # Add faculty grid assignments
        addFacultyLabel.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        addFacultySeparator.grid(row=1, column=0, sticky="ew")
        enterNameLabel.grid(row=3, column=0, pady=5, padx=5, sticky="w")
        nameEntry.grid(row=3, column=1, pady=5, padx=5, sticky="e")
        enterUsernameLabel.grid(row=4, column=0, pady=5, padx=5, sticky="w")
        usernameEntry.grid(row=4, column=1, pady=5, padx=5, sticky="e")
        enterPasswordLabel.grid(row=5, column=0, pady=5, padx=5, sticky="w")
        passwordEntry.grid(row=5, column=1, pady=5, padx=5, sticky="e")
        addFacultySubmitButton.grid(row=6, column=1, padx=5, pady=5, sticky="e")

    def __remove_book_callback(self, book_id_entry, config):
        password = simpledialog.askstring("Password", "Enter password:", show='*')
        try:
            # Check that the id is numeric
            bookID = book_id_entry.get()
            if bookID.isnumeric():
                self.dfManager.bookMgr.remove_book(int(bookID), self.credentialManager.getUser(), password, self.dfManager.facultyMgr)
            else:
                raise Exception("Wrong book ID format")

            # Restart the page
            config["callback"]("MANAGE", config)

        except Exception as error:
            book_id_entry.delete(0, 'end')
            messagebox.showerror("Remove Book Error", f"Error: {error}")

    def __add_book_callback(self, title_entry, author_entry, genre_entry, desc_entry, config):
        title = title_entry.get()
        author = author_entry.get()
        genre = genre_entry.get()
        desc = desc_entry.get("1.0", 'end').replace("\n", "")

        try:
            # Check that all fields have been filled out
            if title != "" and author != "" and genre != "" and desc != "":
                self.dfManager.bookMgr.add_book(title, author, genre, desc)
            else:
                raise Exception("Not all fields filled out")

            # Restart the page
            config["callback"]("MANAGE", config)

        except Exception as error:
            messagebox.showerror("Add Book Error", f"Error: {error}")

    def __remove_faculty_callback(self, faculty_id_entry, config):
        password = simpledialog.askstring("Password", "Enter password:", show='*')
        try:
            # Check that the id is numeric
            facultyID = faculty_id_entry.get()
            if facultyID.isnumeric():
                self.dfManager.facultyMgr.removeFaculty(int(facultyID), self.credentialManager.getUser(), password)
            else:
                raise Exception("Wrong faculty ID format")

            # Restart the page
            config["callback"]("MANAGE", config)

        except Exception as error:
            faculty_id_entry.delete(0, 'end')
            messagebox.showerror("Remove User Error", f"Error: {error}")

    def __add_faculty_callback(self, name_entry, username_entry, password_entry, config):
        name = name_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        try:
            # Check that all fields have been filled out
            if name != "" and username != "" and password != "":
                self.dfManager.facultyMgr.addFaculty(username, password, name)
            else:
                raise Exception("Not all fields filled out")

            # Restart the page
            config["callback"]("MANAGE", config)

        except Exception as error:
            messagebox.showerror("Add Faculty Error", f"Error: {error}")