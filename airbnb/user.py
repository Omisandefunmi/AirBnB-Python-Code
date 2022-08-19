import json
from pathlib import Path
import bcrypt
from util import hash_password, validate_password

user = {
    "firstName": "Amaka",
    "lastName": "Adewale",
    "email_address": "amakade@gmail.com",
    "phoneNumber": "09089898989",
    "userName": "amakaluv",
    "password": "1111",
    "role": "owner"
}


def get_file_path():
    path = Path("../data/users/users.json").resolve()
    if not path.exists():
        path.parent.mkdir(exist_ok=True, parents=True)
        path.touch()
    return path


def get_users():
    file_path = get_file_path()

    with file_path.open(mode="r", encoding="utf-8") as file:
        try:
            users = json.load(file)
            return users
        except json.decoder.JSONDecodeError:
            return []


def save_user(user):
    user['password'] = hash_password(user['password'])
    file_path = get_file_path()
    users = get_users()

    if [u for u in users if u['userName'] == user['userName']]:
        print(f"User with username {user['userName']} already exist")
        return

    users.append(user)

    with file_path.open(mode="w", encoding='utf-8') as file:
        json.dump(users, file)


def get_user_by_username(username):
    users = get_users()
    user_list = [u for u in users if u['userName'] == username]
    if user_list:
        return user_list[0]
    return f"User with username {username} not found"


if __name__ == '__main__':
    save_user(user)
    print(get_user_by_username('amakaluv'))
