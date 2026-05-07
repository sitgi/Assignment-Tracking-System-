import copy

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)
