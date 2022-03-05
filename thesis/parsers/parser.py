import os
from thesis.repr.inter import *
from abc import ABC, abstractmethod

class Parser(ABC):
    def parse(self, path: str, is_module: bool) -> Module:
        if is_module:
            return self.parse_module(path)
        elif os.path.isfile(path):
            return self.parse_file(path)
        else:
            return self.parse_folder(path)

    @abstractmethod
    def parse_file(self, path: str) -> Module:
        pass

    @abstractmethod
    def parse_folder(self, path: str) -> Module:
        pass

    @abstractmethod
    def parse_module(self, path: str) -> Module:
        pass

    def parse_file_structure(self, folder, path):
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                folder.add_file(File(f))
            elif os.path.isdir(os.path.join(path, f)):
                new_folder = Folder(f)
                self.parse_file_structure(new_folder, os.path.join(path, f))
                folder.add_folder(new_folder)