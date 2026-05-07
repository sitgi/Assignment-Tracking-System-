class Assignment:
    def __init__(self, id, title, deadline, status="Pending"):
        self.id = id
        self.title = title
        self.deadline = deadline
        self.status = status

    def add(self):
        return "Assignment added"

    def edit(self):
        return "Assignment updated"

    def delete(self):
        return "Assignment deleted"
