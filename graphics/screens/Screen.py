from abc import ABC, abstractmethod

class Screen:
    def __init__(self, dfManager):
         self.dfManager = dfManager
    
    @abstractmethod
    def display(self, root, config):
         pass