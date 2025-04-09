import random

QUOTES = [
    "🌈 Keep going, you’re doing better than you think.",
    "💪 Every day is a new beginning.",
    "🧠 Mental health is just as important as physical health.",
    "🌻 You’ve survived 100% of your bad days. Keep going.",
    "☕ Take a deep breath. You’ve got this.",
    "🚀 Progress is progress, no matter how small.",
    "🫶 Be kind to yourself. You’re trying."
]

def show_random_quote():
    quote = random.choice(QUOTES)
    print("\n💬 Motivational Quote:\n")
    print(f"👉 {quote}\n")
