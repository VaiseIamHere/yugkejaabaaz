import timetable as tt


class Person:

    def __init__(self, name, branch, img):
        self.name = name
        self.branch = branch
        self.tt = tt.get_tt(img)
