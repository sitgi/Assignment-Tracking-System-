
from repositories.inmemory.inmemory_assignment_repository import InMemoryAssignmentRepository

class UserService:

    def __init__(self):
        self.users = []

    def create_user(self, name, email):

        if not name or not email:
            raise ValueError("Name and email required")

        user = {
            "name": name,
            "email": email
        }

        self.users.append(user)
        return user

    def get_users(self):
        return self.users
