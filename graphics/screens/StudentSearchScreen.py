from graphics.screens.Screen import Screen
import tkinter as tk
import tkinter.ttk as ttk
import numpy

class StudentSearchScreen(Screen):
    def __init__(self, dfManager, credentialManager=None):
        Screen.__init__(self, dfManager)

    def display(self, root, config):
        # Some variables for the search bar updates
        self.after_id = None
        self.searchText = tk.StringVar()

        # Main menu button
        backButton = tk.Button(
            root, 
            text="Main Menu",
            font=("Arial", 11),
            command=lambda: config["callback"]("MAIN_MENU", config))
    
        # Quit application button
        quitButton = tk.Button(root, text="Quit", font=("Arial", 11), command=root.destroy)
        
        # Search bar label
        searchLabel = tk.Label(root, text="Students", font=("Arial", 16))
        
        #Search bar entry box
        entry = tk.Entry(root, font=("Arial", 16), width=30, textvariable=self.searchText)
        entry.bind("<FocusIn>", lambda event: self.__on_entry_click(event, entry))
        entry.bind("<FocusOut>", lambda event: self.__on_focus_out(event, entry))

        self.__on_focus_out(None, entry)

        # Search results table
        columnNames = ["#0", "name", "books"]
        columnHeaders = ["ID", "Name", "Books checked out"]
        columnWidths = [50, 100, 300]
        searchResults = ttk.Treeview(root, columns=tuple(columnNames[1:]), height=20)
        for i in range(len(columnNames)):
            searchResults.column(columnNames[i], minwidth=0, width=columnWidths[i])
            searchResults.heading(columnNames[i], text=columnHeaders[i])
        searchResults.bind("<<TreeviewSelect>>", lambda event: self.__table_callback(event, config))
        self.searchText.trace_add("write", lambda a, b, c: self.__after_callback(searchResults, self.searchText.get()))
        self.__display_search_results(searchResults, "")

        # Formatting the layout on the grid
        quitButton.grid(column=3, row=0, pady=5, padx=5)
        backButton.grid(column=0, row=0, pady=5, padx=5, sticky="w")
        searchLabel.grid(column=0, row=1, padx=5, sticky="w")
        entry.grid(column=1, row=1, pady=5, padx=5, sticky="w")
        searchResults.grid(column=1, row=2, padx=5, columnspan=2, sticky="w")

    # Event callbacks
    def __on_entry_click(self, event, entry):
        if entry.get() == "Search by name or ID...":
            entry.delete(0, tk.END)
            entry.configure(foreground="black")

    def __on_focus_out(self, event, entry):
        if entry.get() == "":
            entry.insert(0, "Search by name or ID...")
            entry.configure(foreground="gray")

    def __after_callback(self, table, term):
        if self.after_id is not None:
            table.after_cancel(self.after_id)
        self.after_id = table.after(1000, lambda: self.__display_search_results(table, term))

    def __display_search_results(self, table, term):
        for item in table.get_children():
            table.delete(item)

        validResults = self.__format_results(self.dfManager.studentMgr.search(int(term) if term.isnumeric() else term))
        for i in range(len(validResults)):
            table.insert("", tk.END, text=validResults[i][0], values=validResults[i][1:])

    def __table_callback(self, event, config):
        tree = event.widget
        if self.after_id is not None:
            tree.after_cancel(self.after_id)
        item = tree.item(tree.focus())
        newConfig = {
            "callback": config["callback"],
            "name": item["values"][0]
        } 
        config["callback"]("STUDENT_DETAILS", newConfig)
    
    def __format_results(self, results):
        formattedList = []
        for student in results:
            checkedOutBooks = list(map(lambda x: x[2], filter(lambda x: x[1] == student[1], results)))
            if student[0] not in list(map(lambda x: x[0], formattedList)):
                formattedList.append(student[0:2])
                if not numpy.isnan(checkedOutBooks[0]):
                    formattedList[-1].append(self.__format_book_list(checkedOutBooks))
                else:
                    formattedList[-1].append("")
        return formattedList
    
    def __format_book_list(self, bookList):
        return ", ".join(list(map(lambda x: self.dfManager.bookMgr.search(x)[0][1], bookList)))
            