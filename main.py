from services.user_system import UserSystem
from services.bolanapp import BolanApp
from services.database import Database

def main():
    user_system = UserSystem()
    db = Database()
    app = BolanApp()

    while True:
        print("\n=== Huvudmeny ===")
        print("1. Logga in")
        print("2. Skapa nytt konto")
        print("3. Ändra lösenord")
        print("4. Avsluta")
        choice = input("Välj: ")

        if choice == "1":
            user = user_system.login()
            if user:
                app.bolan()
                app.renovering()
                db.spara_resultat(user, app.resultat)
                db.visa_historik(user)
        elif choice == "2":
            user_system.register()
        elif choice == "3":
            user_system.change_password()
        elif choice == "4":
            print("👋 Tack för att du använde bolånekalkylen!")
            break
        else:
            print("❌ Ogiltigt val!")

if __name__ == "__main__":
    main()
