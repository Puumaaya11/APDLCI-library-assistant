import pandas as pd
from data.managers.Util import *

CSV_PATH = "resources/student.csv" 

class StudentManager():
    def __init__(self):
        self.studentDf = pd.read_csv(CSV_PATH)

    def save_df(self):
        self.studentDf.to_csv(CSV_PATH, index = False)

    def search(self, term):
        # search through name
        if type(term) == str:
            return df_to_list(self.studentDf[self.studentDf['first_name'].str.lower().str.contains(term.lower())])

        # search through student_id
        return df_to_list(self.studentDf[self.studentDf['student_id'] == term])

    # TODO make this work
    def checkout(self, studentID, bookID, bookMgr):
        if len(bookMgr.bookDf.loc[bookMgr.bookDf['book_id'] == bookID]) == 1:
            book_entry = bookMgr.bookDf.loc[bookMgr.bookDf['book_id'] == bookID]

            # check availability
            if book_entry['availability'].item() == False:
                raise Exception("Book not available.")
            else:
                bookMgr.bookDf.loc[bookMgr.bookDf['book_id']==bookID, 'availability'] = False

                # book is available, will add to student's record
                if len(self.studentDf.loc[self.studentDf['student_id'] == studentID]) == 1:
                    self.studentDf.loc[self.studentDf['student_id'] == studentID, 'books'] = self.studentDf.loc[self.studentDf['student_id'] == studentID, 'books'].item().append(bookID)
                else:
                    raise Exception("Student does not exist.")
        else:
            raise Exception("Book does not exist.")

    # TODO implement
    def renew(self, studentID, bookID, bookManager):
        pass

    # TODO implement
    def ret(self, studentID, bookID, bookManager):
        pass