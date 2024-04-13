import pandas as pd

CSV_PATH = "resources/student.csv" 

class StudentManager():
    def __init__(self):
        self.studentDf = pd.read_csv(CSV_PATH)

    def save_df(self):
        self.facultyDf.to_csv(CSV_PATH, index = False)

    def search(self, term):
        # search through name
        if type(term) == str:
            return self.studentDf[self.studentDf['name'].str.lower().str.contains(term.lower())]

        # search through student_id
        return self.studentDf[self.studentDf['student_id'] == term]

    def checkout(self, studentID, bookID, bookManager):
        pass

    def renew(self, studentID, bookID, bookManager):
        pass

    def ret(self, studentID, bookID, bookManager):
        pass