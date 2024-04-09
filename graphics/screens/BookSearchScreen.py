from graphics.screens.Screen import Screen
import tkinter as tk
import tkinter.ttk as ttk

class BookSearchScreen(Screen):
    def __init__(self) -> None:
        pass

    def display(self, root, config):
        # Main menu button
        backButton = tk.Button(
            root, 
            text="Main Menu",
            font=("Arial", 11),
            command=lambda: config["callback"]("MAIN_MENU", config))
        
        # Search bar label
        searchLabel = tk.Label(root, text="Search", font=("Arial", 16))
        
        #Search bar entry box
        entry = tk.Entry(root, font=("Arial", 16), width=30)
        entry.bind("<FocusIn>", lambda event: self.__on_entry_click(event, entry))
        entry.bind("<FocusOut>", lambda event: self.__on_focus_out(event, entry))
        self.__on_focus_out(None, entry)

        # Search results table frame
        searchResults = ttk.Treeview(root, columns=("name", "town", "age"), height=20)
        searchResults.column("#0", minwidth=0, width=100)
        searchResults.column("name", minwidth=0, width=100)
        searchResults.column("town", minwidth=0, width=100)
        searchResults.column("age", minwidth=0, width=100)
        searchResults.heading("#0", text="ID")
        searchResults.heading("name", text="Name")
        searchResults.heading("town", text="Town")
        searchResults.heading("age", text="Age")

        # Go! button
        goButton=tk.Button(
            root, 
            text="Go!", 
            font=("Arial", 11), 
            command=lambda: self.__display_search_results(searchResults))

        backButton.grid(column=0, row=0, pady=5)
        searchLabel.grid(column=0, row=1, padx=5)
        entry.grid(column=1, row=1, pady=5, padx=5)
        goButton.grid(column=2, row=1)
        searchResults.grid(column=1, row=2, padx=5, columnspan=2)
        
    
    def __on_entry_click(self, event, entry):
        if entry.get() == "Search by name or ID...":
            entry.delete(0, tk.END)
            entry.configure(foreground="black")

    def __on_focus_out(self, event, entry):
        if entry.get() == "":
            entry.insert(0, "Search by name or ID...")
            entry.configure(foreground="gray")

    def __display_search_results(self, table):
        testData = [('Raj','Mumbai',19),
                    ('Aaryan','Pune',18),
                    ('Vaishnavi','Mumbai',20),
                    ('Rachna','Mumbai',21),
                    ('Shubham','Delhi',21)]
        for i in range(len(testData)):
            table.insert("", tk.END, text=i, values=testData[i])