class HomeworkAssignment:
    def create(self):
        return "Homework Assignment Created"

class ProjectAssignment:
    def create(self):
        return "Project Assignment Created"

class AssignmentFactory:
    @staticmethod
    def create_assignment(type):
        if type == "homework":
            return HomeworkAssignment()
        elif type == "project":
            return ProjectAssignment()
        else:
            raise ValueError("Invalid assignment type")
