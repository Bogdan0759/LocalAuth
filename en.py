import json
import hashlib
import os
from getpass import getpass


class AuthError(Exception):
    pass


class UserAlreadyExists(AuthError):
    pass


class UserNotFound(AuthError):
    pass


class InvalidPassword(AuthError):
    pass


class LocalAuth:
    def __init__(self, db_path: str = "users.json"):
        self.db_path = db_path
        if not os.path.exists(db_path):
            with open(db_path, 'w') as f:
                json.dump({}, f)
        self._load_db()

    def _load_db(self):
        with open(self.db_path, 'r') as f:
            self.db = json.load(f)

    def _save_db(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f, indent=2)

    def _hash(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self):
        username = input("Enter username: ").strip()
        if username in self.db:
            raise UserAlreadyExists("User already exists.")
        password = getpass("Enter password: ")
        confirm = getpass("Confirm password: ")
        if password != confirm:
            print("Passwords do not match.")
            return
        self.db[username] = {"password_hash": self._hash(password)}
        self._save_db()
        print(f"User '{username}' registered.")

    def login(self) -> str | None:
        username = input("Enter username: ").strip()
        if username not in self.db:
            raise UserNotFound("User not found.")
        password = getpass("Enter password: ")
        if self.db[username]["password_hash"] != self._hash(password):
            raise InvalidPassword("Incorrect password.")
        print(f"Welcome, {username}!")
        return username

    def change_password(self):
        username = input("Username: ").strip()
        old_password = getpass("Old password: ")
        if self.db.get(username, {}).get("password_hash") != self._hash(old_password):
            raise InvalidPassword("Old password is incorrect.")
        new_password = getpass("New password: ")
        confirm = getpass("Confirm new password: ")
        if new_password != confirm:
            print("Passwords do not match.")
            return
        self.db[username]["password_hash"] = self._hash(new_password)
        self._save_db()
        print("Password successfully changed.")

    def delete_user(self):
        username = input("Enter username: ").strip()
        password = getpass("Enter password: ")
        if self.db.get(username, {}).get("password_hash") != self._hash(password):
            raise InvalidPassword("Incorrect password.")
        del self.db[username]
        self._save_db()
        print(f"User '{username}' deleted.")

    def list_users(self):
        print("Users:")
        for user in self.db.keys():
            print("-", user)