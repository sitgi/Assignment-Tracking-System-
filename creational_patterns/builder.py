class Assignment:
    def __init__(self):
        self.details = []

    def add_detail(self, detail):
        self.details.append(detail)

class AssignmentBuilder:
    def __init__(self):
        self.assignment = Assignment()

    def add_title(self):
        self.assignment.add_detail("Title Added")
        return self

    def add_deadline(self):
        self.assignment.add_detail("Deadline Added")
        return self

    def add_description(self):
        self.assignment.add_detail("Description Added")
        return self

    def build(self):
        return self.assignment
