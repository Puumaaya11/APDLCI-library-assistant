from abc import ABC, abstractmethod

class Screen:
    def __init__(self) -> None:
         pass
    
    @abstractmethod
    def display(self, root, config):
         pass