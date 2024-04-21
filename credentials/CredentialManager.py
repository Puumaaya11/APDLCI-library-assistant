from data.Util import *

class CredentialManager():
    def __init__(self, dfManager):
        self.dfManager = dfManager
        self.curUser = None
    
    def getUser(self):
        return self.curUser

    def login(self, username: str, password: str):
        if exist(username, 'username', self.dfManager.facultyMgr.facultyDf):
            if exist(password, 'password', self.dfManager.facultyMgr.facultyDf[self.dfManager.facultyMgr.facultyDf['username']==username]):
                self.curUser = self.dfManager.facultyMgr.search(username)[0][0]
                return True
            else:
                return False
        else:
            return False