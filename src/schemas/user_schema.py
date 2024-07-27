
class UserCreate:
    name: str
    email: str
    password: str

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password