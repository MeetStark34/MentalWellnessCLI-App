import json
import os
from datetime import datetime

DATA_FILE = "mental_wellness_cli/data/moods.json"

def get_scaled_mood(prompt, scale_options):
    print(f"\n{prompt}")
    for num, label in scale_options.items():
        print(f"{num}. {label}")
    while True:
        choice = input("Choose a number (1–5): ").strip()
        if choice in scale_options:
            return int(choice)
        print("❗ Invalid choice. Please select a number from 1 to 5.")

def record_mood():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    username = input("\n👤 Confirm your username: ").strip()

    print("\n🧘 Mood Check-in Time! Rate how you're feeling today:")

    happiness = get_scaled_mood("😊 How happy are you today?", {
        "1": "😞 Not at all",
        "2": "😕 A little",
        "3": "😐 Neutral",
        "4": "🙂 Quite happy",
        "5": "😄 Super happy"
    })

    anger = get_scaled_mood("😡 How angry are you today?", {
        "1": "😇 Not at all",
        "2": "😕 Slightly annoyed",
        "3": "😐 Meh",
        "4": "😠 Pretty mad",
        "5": "🤬 Raging"
    })

    stress = get_scaled_mood("😫 How stressed are you today?", {
        "1": "😌 Totally chill",
        "2": "🙂 Mostly fine",
        "3": "😐 Kind of tense",
        "4": "😣 Stressed",
        "5": "😩 Super stressed"
    })

    relaxed = get_scaled_mood("😌 How relaxed are you today?", {
        "1": "😬 Not at all",
        "2": "😕 Barely relaxed",
        "3": "😐 Somewhat okay",
        "4": "🙂 Pretty calm",
        "5": "🧘 Zen master"
    })

    today = datetime.now().strftime("%Y-%m-%d")
    entry = {
        "date": today,
        "happy": happiness,
        "angry": anger,
        "stressed": stress,
        "relaxed": relaxed
    }

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            moods = json.load(file)
    else:
        moods = {}

    if username not in moods:
        moods[username] = []

    moods[username].append(entry)

    with open(DATA_FILE, "w") as file:
        json.dump(moods, file, indent=2)

    print("\n✅ Mood for today recorded successfully!\n")
