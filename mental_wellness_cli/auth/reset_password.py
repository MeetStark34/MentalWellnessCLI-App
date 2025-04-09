import json
import os

DATA_FILE = "mental_wellness_cli/data/users.json"

def reset_user_password():
    if not os.path.exists(DATA_FILE):
        print("❗ No users found. Please register first.")
        return

    username = input("👤 Enter your username: ").strip()

    with open(DATA_FILE, "r") as file:
        users = json.load(file)

    if username not in users:
        print("❌ Username not found.")
        return

    new_password = input("🔑 Enter your new password: ").strip()
    confirm_password = input("🔁 Confirm your new password: ").strip()

    if new_password != confirm_password:
        print("⚠️ Passwords do not match. Try again.")
        return

    users[username]["password"] = new_password

    with open(DATA_FILE, "w") as file:
        json.dump(users, file)

    print("✅ Password updated successfully!")
