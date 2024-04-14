import pandas as pd
from data.managers.Util import *

CSV_PATH = "resources/book.csv" 

class BookManager():
    def __init__(self):
        self.bookDf = pd.read_csv(CSV_PATH)

    def save_df(self):
        self.facultyDf.to_csv(CSV_PATH, index = False)

    def search(self, term):
        results = []

    # search through title, author, genre, description
        if type(term) == str:
            results.append(self.bookDf[self.bookDf['title'].str.lower().str.contains(term.lower())])
            results.append(self.bookDf[self.bookDf['author'].str.lower().str.contains(term.lower())])
            results.append(self.bookDf[self.bookDf['genre'].str.lower().str.contains(term.lower())])
            results.append(self.bookDf[self.bookDf['description'].str.lower().str.contains(term.lower())])

        # search through book_id
        else:
            return df_to_list(self.bookDf[self.bookDf['book_id'] == term])

        # list of dfs to single df
        results = pd.concat(results, ignore_index=True)
        results.drop_duplicates(inplace = True)
        
        return df_to_list(results)

    def addBook(self, details):
        pass

    def removeBook(self, bookID):
        pass