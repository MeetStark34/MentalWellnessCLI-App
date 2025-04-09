import json
import os
from datetime import datetime

DATA_FILE = "mental_wellness_cli/data/journals.json"

def write_entry():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    username = input("👤 Enter your username: ").strip()
    entry = input("📝 Write your journal entry for today:\n> ")

    today = datetime.now().strftime("%Y-%m-%d")

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            journals = json.load(file)
    else:
        journals = {}

    if username not in journals:
        journals[username] = []

    journals[username].append({
        "date": today,
        "entry": entry
    })

    with open(DATA_FILE, "w") as file:
        json.dump(journals, file, indent=2)

    print("✅ Journal saved successfully.")
