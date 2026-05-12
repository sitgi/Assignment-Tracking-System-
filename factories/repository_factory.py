from repositories.inmemory.inmemory_assignment_repository import InMemoryAssignmentRepository

class RepositoryFactory:

    @staticmethod
    def get_assignment_repository(storage_type):

        if storage_type == "MEMORY":
            return InMemoryAssignmentRepository()

        else:
            raise ValueError("Invalid storage type")
