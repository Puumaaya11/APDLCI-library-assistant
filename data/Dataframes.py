from data.managers.BookManager import BookManager
from data.managers.FacultyManager import FacultyManager
from data.managers.StudentManager import StudentManager

class Dataframes():
    def __init__(self):
        self.bookMgr = BookManager()
        # self.facultyMgr = FacultyManager()
        self.studentMgr = StudentManager()
        self.__loadFromCSV()

    def saveToCSV(self):
        self.bookMgr.save_df()
        # self.facultyMgr.save_df()
        self.studentMgr.save_df()

    def __loadFromCSV(self):
        self.bookMgr = BookManager()
        # self.facultyMgr = FacultyManager()
        self.studentMgr = StudentManager()
    