from repositories.inmemory.inmemory_assignment_repository import InMemoryAssignmentRepository

class AssignmentService:

    def __init__(self):
        self.repo = InMemoryAssignmentRepository()

    def create_assignment(self, assignment):

        if not assignment.title:
            raise ValueError("Title required")

        self.repo.save(assignment)
        return assignment

    def get_all_assignments(self):
        return self.repo.find_all()

    def delete_assignment(self, id):
        self.repo.delete(id)
