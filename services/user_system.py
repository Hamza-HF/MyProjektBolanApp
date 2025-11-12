import re
import json
from getpass import getpass

class UserSystem:
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_users(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.users, f, indent=4)

    def register(self):
        print("\n=== Skapa nytt konto ===")
        while True:
            email = input("Ange e-post: ").strip()
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("Ogiltig e-postadress, var vänlig och försök igen.")
                continue
            if email in self.users:
                print("Denna e-post är redan registrerad!")
                continue

            password = getpass("Ange lösenord (minst 6 tecken): ")
            if len(password) < 6:
                print("Lösenordet måste innehålla minst 6 tecken!")
                continue

            confirm_password = getpass("Bekräfta lösenord: ")
            if password != confirm_password:
                print("Lösenorden matchar inte, var vänlig och försök igen.")
                continue

            self.users[email] = password
            self.save_users()
            print(f"Konto skapat för {email}!\n")
            break

    def login(self):
        print("\n=== Logga in ===")
        while True:
            email = input("Ange e-post: ").strip()
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("Ogiltig e-postadress!")
                continue

            password = getpass("Ange lösenord: ")

            if email in self.users and self.users[email] == password:
                print(f"Välkommen {email}! Inloggningen lyckades!\n")
                return email
            else:
                print("Fel e-post eller lösenord, var vänlig och försök igen.")

    def change_password(self):
        print("\n=== Ändra lösenord ===")
        email = input("Ange din e-post: ").strip()

        if email not in self.users:
            print("Användaren finns inte.")
            return

        old_password = getpass("Ange ditt nuvarande lösenord: ")

        if self.users[email] != old_password:
            print("Fel lösenord.")
            return

        new_password = getpass("Ange nytt lösenord (minst 6 tecken): ")
        if len(new_password) < 6:
            print("Lösenordet måste innehålla minst 6 tecken!")
            return

        confirm_new_password = getpass("Bekräfta nytt lösenord: ")
        if new_password != confirm_new_password:
            print("Lösenorden matchar inte!")
            return

        self.users[email] = new_password
        self.save_users()
        print("Lösenordet har ändrats!\n")