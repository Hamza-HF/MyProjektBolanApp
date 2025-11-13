from services.user_system import UserSystem
from services.bolanapp import BolanApp
from services.database import Database

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Fel inmatning, var vänlig och försök igen.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Fel inmatning, var vänlig och försök igen.")

def bolan_beräkning(app):
    print("\n=== Bolånekalkylator ===")
    lägenhetspris = get_float_input("Vad kostar lägenheten? (SEK): ")
    lånebelopp = get_float_input("Hur stort är lånet? (SEK): ")
    räntan = get_float_input("Ränta i %: ")
    år = get_int_input("År att betala: ")

    månadskostnad = app.bolan(lägenhetspris, lånebelopp, räntan, år)
    print(f"\n Månadskostnaden för lånet är: {månadskostnad:.2f} kr/mån\n")

def renoverings_val(app):
    print("\n=== Renoveringsval ===")
    print("1. Badrum: 70 000 kr")
    print("2. Kök: 130 000 kr")
    print("3. Målarfärg: 20 000 kr")
    print("4. Golv: 20 000 kr")
    print("5. Lister: 7 000 kr")
    print("6. Dörrar: 10 000 kr")
    print("7. Arbetskostnad: 80 000 kr")
    print("8. Övrigt: 30 000 kr")
    print("9. Ingen renovering")
    print("10. Egen kostnad")

    valda_renoveringar = []
    egen_kostnad = 0

    while True:
        val = input("Välj renovering(ar) (t.ex. 1,3,6 eller 10): ").strip().split(",")
        val = [v.strip() for v in val]

        ogiltiga = [v for v in val if v not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]]
        if ogiltiga:
            print(f"Ogiltiga val: {', '.join(ogiltiga)}. Försök igen.")
            continue

        if "10" in val:
            egen_kostnad = get_float_input("Ange egen renoveringskostnad (SEK): ")

        valda_renoveringar = [v for v in val if v != "10"]
        break

    total_renovering, ny_månadskostnad = app.renovering(valda_renoveringar, egen_kostnad)
    print(f"\nTotala renoveringskostnaden: {total_renovering:.0f} kr")
    print(f"Ny månadskostnad efter renovering: {ny_månadskostnad:.2f} kr/mån\n")

def lägg_till_avgift(app):
    avgift = get_float_input("Ange månadsavgift för bostaden (SEK): ")
    total_månadskostnad = app.lägg_till_avgift(avgift)
    print(f"Total månadskostnad inkl. avgift: {total_månadskostnad:.2f} kr/mån\n")

def försäljnings_beräkning(app):
    försäljningspris = get_float_input("Vad sålde du bostaden för? (SEK): ")
    vinst = app.försäljning(försäljningspris)
    
    print("\n=== Resultat ===")
    print(f"Köpesumma: {app.lägenhetspris:,.0f} kr")
    print(f"Renovering: {app.renoveringskostnad:,.0f} kr")
    print(f"Försäljningspris: {app.försäljningspris:,.0f} kr")
    print(f"Vinst/Förlust: {app.vinst:,.0f} kr\n")

def main():
    user_system = UserSystem()
    db = Database()

    while True:
        print("\n===  Huvudmeny ===")
        print("1. Logga in")
        print("2. Skapa nytt konto")
        print("3. Ändra lösenord")
        print("4. Avsluta")
        choice = input("Välj: ")

        if choice == "1":
            user = user_system.login()
            if user:
                while True:
                    print("\n===  Inloggad meny ===")
                    print("1. Gör ny bolåneberäkning")
                    print("2. Se mina affärer")
                    print("3. Logga ut")
                    val = input("Välj: ")

                    if val == "1":
                        app = BolanApp()
                        print(f"DEBUG: Skapat nytt BolanApp objekt: {type(app)}")
                        
                        bolan_beräkning(app)
                        renoverings_val(app)
                        lägg_till_avgift(app)
                        försäljnings_beräkning(app)
                        
                        db.spara_resultat(user, app)

                    elif val == "2":
                        db.visa_historik(user)
                    elif val == "3":
                        print("Du har loggat ut.")
                        break
                    else:
                        print("Ogiltigt val, försök igen.")
        elif choice == "2":
            user_system.register()
        elif choice == "3":
            user_system.change_password()
        elif choice == "4":
            print(" Tack för att du använde bolånekalkylen!")
            break
        else:
            print(" Ogiltigt val!")

if __name__ == "__main__":
    main()