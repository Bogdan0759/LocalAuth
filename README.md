# LocalAuth – Simple JSON-based Login System for Python
**EN | RU — scroll down for Russian version**

**LocalAuth** is a plug-and-play, terminal-based user login system written in pure Python.  
It uses a local JSON file for user data and securely hashes passwords.  
Perfect for CLI tools, local apps, prototypes, or any project that doesn’t need a full database.

## Features

- [x] Easy registration and login via terminal
- [x] Password hashing with SHA-256
- [x] Stores data in a simple JSON file
- [x] Uses `getpass` for secure password input
- [x] Fully interactive – no need to write input prompts yourself
- [x] No external dependencies

## Installation

Just download `localauth.py` and put it in your project folder.  
No `pip install` required.

```bash
wget https://raw.githubusercontent.com/YOUR_USERNAME/localauth/main/localauth.py 
Usage - from localauth import LocalAuth

auth = LocalAuth("users.json")

auth.register()  # prompts for username + password
auth.login()     # prompts for login


Russian:
# LocalAuth – Простая система входа на Python

**LocalAuth** — это лёгкая и готовая к использованию система авторизации для терминальных приложений на Python.  
Все данные пользователей хранятся в обычном `.json` файле, а пароли надёжно хешируются.  
Отлично подходит для CLI-утилит, локальных приложений, прототипов и небольших проектов.

---

## Возможности

- [x] Регистрация и вход через терминал
- [x] Хеширование паролей (SHA-256)
- [x] JSON-файл вместо базы данных
- [x] Безопасный ввод пароля через `getpass`
- [x] Интерфейс через терминал – всё спрашивает сам
- [x] Без сторонних зависимостей

---

## Установка

Просто скачайте файл `localauth.py` и положите рядом с вашим проектом.  
Установка через `pip` не требуется.

```bash
wget https://raw.githubusercontent.com/YOUR_USERNAME/localauth/main/localauth.py

Пример использования: 
from localauth import LocalAuth

auth = LocalAuth("users.json")

auth.register()        # спрашивает имя пользователя и пароль
auth.login()           # вход в систему 

By : Bogdan0759


