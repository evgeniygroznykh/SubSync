from dataclasses import dataclass


@dataclass
class Clip:
    def __init__(self, clip_name, has_sub_on_m, has_sub_on_b):
        self.extension = ".mxf"

        self.clip_name = clip_name

        self.has_sub_on_m = has_sub_on_m
        self.has_sub_on_b = has_sub_on_b

    def toJSON(self):
        return self.__dict__