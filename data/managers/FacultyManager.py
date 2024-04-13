import pandas as pd

CSV_PATH = "resources/faculty.csv" 

class FacultyManager():
    def __init__(self):
        self.facultyDf = pd.read_csv(CSV_PATH)

    def save_df(self):
        self.facultyDf.to_csv(CSV_PATH, index = False)

    def search(self, term):
        # search through name
        if type(term) == str:
            return self.facultyDf[self.facultyDf['name'].str.lower().str.contains(term.lower())]

        # search through student_id
        return self.facultyDf[self.facultyDf['faculty_id'] == term]

    def addFaculty(self, details):
        pass

    def removeFaculty(self, facultyID):
        pass