import pandas as pd
from data.Util import *

CSV_PATH = "resources/faculty.csv" 

class FacultyManager():
    def __init__(self):
        self.facultyDf = pd.read_csv(CSV_PATH)

    def save_df(self):
        self.facultyDf.to_csv(CSV_PATH, index = False)

    def search(self, term):
        # search through name
        if type(term) == str:
            results = self.facultyDf[self.facultyDf['name'].str.lower().str.contains(term.lower())]

        # search through faculty_id
        else:
            results = self.facultyDf[self.facultyDf['faculty_id'] == term]

        # convert dataframe slice to list of lists
        return df_to_list(results)

    def addFaculty(self, username, password, name):
        # check duplicates don't exist
        user_exist = self.facultyDf[self.facultyDf['username'] == username].empty
        pass_exist = self.facultyDf[self.facultyDf['password'] == password].empty
        if user_exist == False or pass_exist == False:
            raise Exception('Username or password already taken')

        # check name has first and last (ie a space)
        if ' ' in name == False:
            raise Exception("Must include first and last name")

        # add new row
        new_id = max(self.facultyDf['faculty_id']) + 1
        self.facultyDf.loc[len(self.facultyDf.index)] = [new_id, name, username, password]

        # save changes
        self.save_df()

    def removeFaculty(self, faculty_id, cur_user_id, cur_user_pass):
        # check if faculty member to delete exists
        if exist(faculty_id, 'faculty_id', self.facultyDf) == False:
            raise Exception("Faculty member does not exist")
        
        # verify user's credentials
        if exist(cur_user_pass, 'password', self.facultyDf[self.facultyDf['faculty_id']==cur_user_id]) == False:
            raise Exception("Incorrect credentials")

        # check that user will not delete themselves
        if faculty_id == cur_user_id:
            raise Exception("Cannot delete currently logged in profile")

        index_remove = self.facultyDf[self.facultyDf['faculty_id']==faculty_id].index[0]
        self.facultyDf.drop(index_remove, inplace = True)

        self.save_df()