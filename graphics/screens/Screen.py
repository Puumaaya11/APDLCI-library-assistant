from abc import ABC, abstractmethod

class Screen:
    def __init__(self, dfManager, credentialManager=None):
         self.dfManager = dfManager
         self.credentialManager = credentialManager
    
    @abstractmethod
    def display(self, root, config):
         pass