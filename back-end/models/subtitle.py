from dataclasses import dataclass


@dataclass
class Subtitle:
    def __init__(self, sub_name, is_on_main, is_on_backup, has_sub_on_src):
        self.extension = '.stl'

        self.sub_name = sub_name
        self.is_on_m = is_on_main
        self.is_on_b = is_on_backup

        self.has_sub_on_src = has_sub_on_src

    def toJSON(self):
        return self.__dict__