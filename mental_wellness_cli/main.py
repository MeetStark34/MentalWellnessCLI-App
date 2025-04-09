from auth import login, register, reset_password
from mood import track_mood, view_summary, view_weekly
from journal import journal_entry, view_journals
from quotes import quote_generator

def main():
    print("\n🧠 Welcome to the Mental Wellness CLI App\n")

    while True:
        print("🔐 1️⃣  Login")
        print("🆕 2️⃣  Register")
        print("🔁 3️⃣  Reset Password")
        print("❌ 4️⃣  Exit\n")

        choice = input("Enter your choice: ").strip()
        print()  # spacing

        if choice == "1":
            if login.authenticate():
                after_login_menu()
        elif choice == "2":
            register.create_account()
        elif choice == "3":
            reset_password.reset_user_password()
        elif choice == "4":
            print("🫶 Take care. See you again!\n")
            break
        else:
            print("❗ Invalid choice. Please try again.\n")

def after_login_menu():
    while True:
        print("📋 What would you like to do?\n")
        print("1️⃣  Track Mood")
        print("2️⃣  Write Journal")
        print("3️⃣  View Mood Summary")
        print("4️⃣  Get Motivational Quote")
        print("5️⃣  Logout")
        print("6️⃣  📋 View Weekly Mood Summary")
        print("7️⃣  📖 View Weekly Journals\n")

        choice = input("Choose an option: ").strip()
        print()

        if choice == "1":
            track_mood.record_mood()
        elif choice == "2":
            journal_entry.write_entry()
        elif choice == "3":
            view_summary.show_summary()
        elif choice == "4":
            quote_generator.show_random_quote()
        elif choice == "5":
            print("🔒 Logged out.\n")
            break
        elif choice == "6":
            view_weekly.show_weekly_mood()
        elif choice == "7":
            view_journals.show_weekly_journals()
        else:
            print("❗ Invalid input. Try again.\n")

if __name__ == "__main__":
    main()
