import json
import os

DATA_FILE = "mental_wellness_cli/data/moods.json"

def show_summary():
    if not os.path.exists(DATA_FILE):
        print("📭 No mood records found.\n")
        return

    username = input("👤 Enter your username to view your mood history: ").strip()

    with open(DATA_FILE, "r") as file:
        moods = json.load(file)

    if username not in moods or not moods[username]:
        print("📭 No entries found for this user.\n")
        return

    print(f"\n📅 Mood History for {username}:")
    print("-" * 40)

    mood_totals = {
        "happy": 0,
        "angry": 0,
        "stressed": 0,
        "relaxed": 0
    }

    for entry in moods[username]:
        print(f"{entry['date']} — 😊{entry['happy']} 😡{entry['angry']} 😫{entry['stressed']} 😌{entry['relaxed']}")
        mood_totals["happy"] += entry["happy"]
        mood_totals["angry"] += entry["angry"]
        mood_totals["stressed"] += entry["stressed"]
        mood_totals["relaxed"] += entry["relaxed"]

    print("\n📈 Mood Averages:")
    count = len(moods[username])
    for mood, total in mood_totals.items():
        avg = total / count
        emoji = {
            "happy": "😊",
            "angry": "😡",
            "stressed": "😫",
            "relaxed": "😌"
        }[mood]
        print(f"{emoji} {mood.capitalize()}: {avg:.2f}")

    print()
