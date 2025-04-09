import json
import os

DATA_FILE = "mental_wellness_cli/data/users.json"

def encrypt_password(password, shift=3):
    encrypted = ""
    for char in password:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def create_account():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    print("\n🆕 Register New Account\n")
    username = input("👤 Choose a username: ").strip()
    password = input("🔑 Choose a password: ").strip()

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            users = json.load(file)
    else:
        users = {}

    if username in users:
        print("⚠️ Username already exists. Try logging in.\n")
        return

    encrypted_pw = encrypt_password(password)
    users[username] = {"password": encrypted_pw}

    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=2)

    print("✅ Account created successfully!\n")
