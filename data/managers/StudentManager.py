import pandas as pd
from data.Util import *
import datetime
import numpy

CSV_PATH = "resources/student.csv" 

class StudentManager():
    def __init__(self):
        self.studentDf = pd.read_csv(CSV_PATH)

    def save_df(self):
        self.studentDf.to_csv(CSV_PATH, index = False)

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

        # getting dates
        date_today = pd.Timestamp.today().normalize()
        checkout_period = datetime.timedelta(days=14)
        due_date = date_today + checkout_period

        # check if student only has one row with NA
        if self.studentDf.loc[self.studentDf['student_id'] == studentID,'books'].isnull().any():
            # add to their row with info
            self.studentDf.loc[self.studentDf['student_id'] == studentID, 'books'] = bookID
            self.studentDf.loc[self.studentDf['student_id'] == studentID, 'checkout_date'] = str(date_today)
            self.studentDf.loc[self.studentDf['student_id'] == studentID, 'due_date'] = str(due_date)
        # student already has at least one book checked out, add new row
        else:
            name = self.studentDf.loc[self.studentDf['student_id']==studentID,'name'].tolist()[0]
            self.studentDf.loc[len(self.studentDf.index)] = [studentID, name, bookID, str(date_today), str(due_date)]

        # remove book's availability
        bookMgr.bookDf.loc[bookMgr.bookDf['book_id'] == bookID, 'availability'] = False

        # save changes
        self.save_df()
        bookMgr.save_df()

    # TODO implement
    def renew(self, studentID, bookID):
        date_today = pd.Timestamp.today().normalize()
        checkout_period = datetime.timedelta(days=14)
        due_date = date_today + checkout_period
        self.studentDf.loc[((self.studentDf['student_id']==studentID) & (self.studentDf['books']==bookID)), 'checkout_date'] = str(date_today)
        self.studentDf.loc[((self.studentDf['student_id']==studentID) & (self.studentDf['books']==bookID)), 'due_date'] = str(due_date)

    def ret(self, studentID, bookID, bookMgr):
        # check if student has checked out that book
        if exist(bookID, 'books', self.studentDf[self.studentDf['student_id']==studentID]) == False:
            return

        # check is student only has that book checked out
        # if so, just edit that current row
        if len(self.studentDf[self.studentDf['student_id']==studentID]) == 1:
            self.studentDf.loc[self.studentDf['student_id'] == studentID, 'books'] = numpy.nan
            self.studentDf.loc[self.studentDf['student_id'] == studentID, 'checkout_date'] = numpy.nan
            self.studentDf.loc[self.studentDf['student_id'] == studentID, 'due_date'] = numpy.nan

        # if other books checked out, just remove entry
        else:
            index_remove = self.studentDf[self.studentDf['books']==bookID].index[0]
            self.studentDf.drop(index_remove, inplace = True)

        # change availability of book
        bookMgr.bookDf.loc[bookMgr.bookDf['book_id'] == bookID, 'availability'] = True

        # save changes
        self.save_df()
        bookMgr.save_df()