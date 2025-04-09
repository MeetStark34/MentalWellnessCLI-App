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

def decrypt_password(password, shift=3):
    return encrypt_password(password, -shift)

def authenticate():
    if not os.path.exists(DATA_FILE):
        print("❗ No users found. Please register first.\n")
        return False

    print("\n🔐 Login\n")
    username = input("👤 Username: ").strip()
    password = input("🔑 Password: ").strip()

    with open(DATA_FILE, "r") as file:
        users = json.load(file)

    if username in users:
        stored_encrypted = users[username]["password"]
        if decrypt_password(stored_encrypted) == password:
            print(f"✅ Welcome back, {username}!\n")
            return True

    print("❌ Incorrect username or password.\n")
    return False
