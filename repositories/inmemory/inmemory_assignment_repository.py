from repositories.assignment_repository import AssignmentRepository

class InMemoryAssignmentRepository(AssignmentRepository):

    def __init__(self):
        self._storage = {}

    def save(self, assignment):
        self._storage[assignment.id] = assignment

    def find_by_id(self, id):
        return self._storage.get(id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, id):
        if id in self._storage:
            del self._storage[id]
