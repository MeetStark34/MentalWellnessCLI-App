import json
import os
from datetime import datetime, timedelta

DATA_FILE = "mental_wellness_cli/data/moods.json"

def show_weekly_mood():
    if not os.path.exists(DATA_FILE):
        print("📭 No mood records found.\n")
        return

    username = input("👤 Enter your username: ").strip()

    with open(DATA_FILE, "r") as file:
        moods = json.load(file)

    if username not in moods or not moods[username]:
        print("📭 No mood data for this user.\n")
        return

    today = datetime.now()
    week_ago = today - timedelta(days=7)

    recent_entries = [
        mood for mood in moods[username]
        if datetime.strptime(mood["date"], "%Y-%m-%d") >= week_ago
    ]

    if not recent_entries:
        print("📭 No mood data in the past 7 days.\n")
        return

    print("\n📋 Your Weekly Mood Summary:\n")
    print("📅 Date       😊Happy  😡Angry  😫Stress  😌Relaxed")
    print("--------------------------------------------------")
    for entry in recent_entries:
        print(f"{entry['date']}     {entry['happy']}       {entry['angry']}       {entry['stressed']}         {entry['relaxed']}")
    print()
