class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        return f"{self.name} logged in"

    def register(self):
        return f"{self.name} registered"

