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
        username = input("Введите имя пользователя: ").strip()
        if username in self.db:
            raise UserAlreadyExists("Пользователь уже существует.")
        password = getpass("Введите пароль: ")
        confirm = getpass("Подтвердите пароль: ")
        if password != confirm:
            print("Пароли не совпадают.")
            return
        self.db[username] = {"password_hash": self._hash(password)}
        self._save_db()
        print(f"Пользователь '{username}' зарегистрирован.")

    def login(self) -> Optional[str]:
        username = input("Введите имя пользователя: ").strip()
        if username not in self.db:
            raise UserNotFound("Пользователь не найден.")
        password = getpass("Введите пароль: ")
        if self.db[username]["password_hash"] != self._hash(password):
            raise InvalidPassword("Неверный пароль.")
        print(f"Добро пожаловать, {username}!")
        return username

    def change_password(self):
        username = input("Имя пользователя: ").strip()
        old_password = getpass("Старый пароль: ")
        if self.db.get(username, {}).get("password_hash") != self._hash(old_password):
            raise InvalidPassword("Старый пароль неверен.")
        new_password = getpass("Новый пароль: ")
        confirm = getpass("Подтвердите новый пароль: ")
        if new_password != confirm:
            print("Пароли не совпадают.")
            return
        self.db[username]["password_hash"] = self._hash(new_password)
        self._save_db()
        print("Пароль успешно изменён.")

    def delete_user(self):
        username = input("Введите имя пользователя: ").strip()
        password = getpass("Введите пароль: ")
        if self.db.get(username, {}).get("password_hash") != self._hash(password):
            raise InvalidPassword("Неверный пароль.")
        del self.db[username]
        self._save_db()
        print(f"Пользователь '{username}' удалён.")

    def list_users(self):
        print("Пользователи:")
        for user in self.db.keys():
            print("-", user)