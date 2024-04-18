import pandas as pd
from data.managers.Util import *

CSV_PATH = "resources/student.csv" 

class StudentManager():
    def __init__(self):
        self.studentDf = pd.read_csv(CSV_PATH)

    def save_df(self):
        self.studentDf.to_csv(CSV_PATH, index = False)

    def exist(self, value, attribute: str):
        if self.studentDf[self.studentDf[attribute] == value].empty:
            return False
        else:
            return True

    def search(self, term):
        # search through name
        if type(term) == str:
            results = self.studentDf[self.studentDf['name'].str.lower().str.contains(term.lower())]

        # search through student_id and book
        else:
            results = self.studentDf[self.studentDf['student_id'] == term]
            # look through book to return books that student has checked out
            if results.empty:
                results = self.studentDf[self.studentDf['books'] == term]
        return df_to_list(results)

    def checkout(self, studentID, bookID, bookMgr):
        # check if book is available:
        if bookMgr.bookDf.loc[bookMgr.bookDf['book_id']==bookID, 'availability'].item() == False:
            raise Exception('Book is unavailable for checkout.')

        # add book to student's profile
        name = self.studentDf.loc[self.studentDf['student_id']==studentID,'name'].tolist()[0]

        # TODO actually put in date time stuff
        self.studentDf.loc[len(self.studentDf.index)] = [studentID, name, bookID, "", ""]

        # remove book's availability
        bookMgr.bookDf.loc[bookMgr.bookDf['book_id'] == bookID, 'availability'] = False

    # TODO implement
    def renew(self, studentID, bookID, bookManager):
        pass

    # TODO implement
    def ret(self, studentID, bookID, bookManager):
        pass