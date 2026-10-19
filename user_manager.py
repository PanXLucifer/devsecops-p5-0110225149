class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username: str, email: str) -> bool:
        if username in self.users:
            return False
        self.users[username] = {"email": email, "active": True}
        return True

    def get_user(self, username: str) -> dict:
        return self.users.get(username, {})