# 🧠 Mental Wellness CLI App

A simple, offline, privacy-first terminal application to track your mental well-being — built entirely in Python.

## 📦 Features

- 🔐 Register / Login / Reset Password (with Caesar cipher encryption)
- 😊 Mood Tracking with emoji-based scales
- 📋 Weekly Mood Summary Table (clean terminal output, no graphs)
- 📓 Daily Journal Entry + Weekly Journal Viewer
- 💬 Motivational Quotes Generator
- 🗃️ Local JSON storage — no accounts, no cloud, no leaks
- 🧼 Clean modular structure, beginner-friendly codebase


## 🗂️ Project Structure

```
mental_wellness_cli/
├── auth/              # login, register, reset_password
├── mood/              # track mood, view summary, weekly mood
├── journal/           # write + view journal entries
├── quotes/            # motivational quotes
├── data/              # auto-generated JSON files
├── main.py            # program entry point
```
## 📸 Menu Preview

```
📋 What would you like to do?

1️⃣  Track Mood
2️⃣  Write Journal
3️⃣  View Mood Summary
4️⃣  Get Motivational Quote
5️⃣  Logout
6️⃣  📋 View Weekly Mood Summary
7️⃣  📖 View Weekly Journals
```

## 🔧 Requirements

- Python 3.8 or above
- No third-party libraries needed

## 🚀 Getting Started

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR-USERNAME/mental-wellness-cli.git
cd mental-wellness-cli
```

2. **Run the app:**
```bash
python mental_wellness_cli/main.py
```

## 🧠 Mood Tracking Scale

Each mood is tracked from 1 to 5 using emojis and simple descriptions:

- 😞 Not at all
- 😕 A little
- 😐 Neutral
- 🙂 Quite a bit
- 😄 A lot

Tracked mood types:
- 😊 Happy
- 😡 Angry
- 😫 Stressed
- 😌 Relaxed

## 👨‍💻 Author

Made with ❤️ in Python by **YourNameHere**

## 🛡️ License

MIT License — free to use, remix, and improve!

## 🌱 Contributions Welcome

Feel free to fork the repo, add features, fix bugs, or build your own wellness tool using this as a base.
