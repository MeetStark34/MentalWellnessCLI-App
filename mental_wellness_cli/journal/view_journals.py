import json
import os
from datetime import datetime, timedelta

DATA_FILE = "mental_wellness_cli/data/journals.json"

def show_weekly_journals():
    if not os.path.exists(DATA_FILE):
        print("📭 No journal entries found.\n")
        return

    username = input("👤 Enter your username to view your journals: ").strip()

    with open(DATA_FILE, "r") as file:
        journals = json.load(file)

    if username not in journals or not journals[username]:
        print("📭 No journal entries for this user.\n")
        return

    today = datetime.now()
    week_ago = today - timedelta(days=7)

    recent_entries = [
        entry for entry in journals[username]
        if datetime.strptime(entry["date"], "%Y-%m-%d") >= week_ago
    ]

    if not recent_entries:
        print("📭 No journal entries in the past 7 days.\n")
        return

    print("\n📖 Journal Entries This Week:\n")
    for entry in recent_entries:
        print(f"📅 {entry['date']}")
        print(f"📝 {entry['entry']}\n")
