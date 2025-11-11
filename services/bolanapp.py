class BolanApp:
    def __init__(self):
        ##self.anvandare = None
        self.resultat = 0
        ##self.ladda_data()
        
    def bolan(self):
            print("=== bolånekalkylator ===")
            while True:
                try:
                        lånebelopp = float(input("Hur stort är lånet? (SEK): "))
                        räntan = float(input(" Ränta i %: "))
                        år = int(input("År att betala: "))

                        månads_räntan = (räntan / 100) / 12
                        månader = år * 12

                        månads_kostnad = (lånebelopp * månads_räntan) / (1 - (1 + månads_räntan) ** -månader)
                        self.resultat = round(månads_kostnad, 2)

                        print(f"Månadskostnaden är: {self.resultat} Kr")
                        break
                except ValueError:
                        print("Fel inmating, Var vänlig och försök igen")

    def renovering(self):
        print("\n=== Renoveringsval ===")
        print("1. Badrum: 70 000 kr")
        print("2. Kök: 130 000 kr")
        print("3. Målarfärg: 20 000 kr")
        print("4. golv: 40 000 kr")
        print("5. lister: 7000 kr")
        print("6. Dörrar: 15 000 kr")
        print("7. Arbetskostnad: 80 000 kr")
        print("8. Övrigt: 30 000 kr")
        print("9. Ingen renovering")
        
        priser = {"1": 70000, "2": 130000, "3": 20000, "4": 40000, "5": 7000, "6": 15000, "7": 80000, "8": 30000, "9": 0}
        
        while True:
            val = input("Välj 1-9 för att välja renovering: ").strip()
            if val in priser:
                extra = priser[val] / 120
                self.resultat = round(self.resultat + extra, 2)
                print(f"Ny månadskostnad efter renovering: {self.resultat} kr")
                break
            else:
                print("Ogiltigt val, var vänlig och försök igen.")