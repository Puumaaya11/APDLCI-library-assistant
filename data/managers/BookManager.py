import pandas as pd
from data.Util import *

CSV_PATH = "resources/book.csv" 

class BookManager():
    def __init__(self):
        self.bookDf = pd.read_csv(CSV_PATH)

    def save_df(self):
        self.bookDf.to_csv(CSV_PATH, index = False)

    def search(self, term):
        results = []

    # search through title, author, genre, description
        if type(term) == str:
            results.append(self.bookDf[self.bookDf['title'].str.lower().str.contains(term.lower())])
            results.append(self.bookDf[self.bookDf['author'].str.lower().str.contains(term.lower())])
            results.append(self.bookDf[self.bookDf['genre'].str.lower().str.contains(term.lower())])

        # search through book_id
        else:
            return df_to_list(self.bookDf[self.bookDf['book_id'] == term])

        # list of dfs to single df
        results = pd.concat(results, ignore_index=True)
        results.drop_duplicates(inplace = True)
        
        return df_to_list(results)

    def add_book(self, title, author, genre, desc):
        new_id = max(self.bookDf['book_id']) + 1
        self.bookDf.loc[len(self.bookDf.index)] = [new_id, title, author, genre, True, desc]
        self.save_df()

    def remove_book(self, book_id, cur_user_id, cur_user_pass, facultyMgr):

        # verify user's credentials
        if exist(cur_user_pass, 'password', facultyMgr.facultyDf[facultyMgr.facultyDf['faculty_id']==cur_user_id]) == False:
            raise Exception("Incorrect credentials")

        # check if book to delete exists
        if exist(book_id, 'book_id', self.bookDf) == False:
            raise Exception("Faculty member does not exist")

        index_remove = self.bookDf[self.bookDf['book_id']==book_id].index[0]
        self.bookDf.drop(index_remove, inplace = True)

        self.save_df()