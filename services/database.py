import json
import os

class Database:
    def __init__(self, filename="database.json"):
        self.filename = filename
        self.historik = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data if isinstance(data, list) else []
            except json.JSONDecodeError:
                return []

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.historik, f, indent=4, ensure_ascii=False)

    def spara_resultat(self, email, app):
        info = {
            "Email": email,
            "Köpesumma": app.lägenhetspris,
            "Renovering": app.renoveringskostnad,
            "Försäljningspris": app.försäljningspris,
            "Vinst": app.vinst,
            "Månadskostnad inkl. avgift": app.resultat
        }
        self.historik.append(info)
        self.save_data()
        print("\n Resultatet har sparats i din historik!")

    def visa_historik(self, email):
        user_history = [h for h in self.historik if h["Email"] == email]
        if not user_history:
            print("\nIngen historik hittades.")
            return
        print("\n === Dina affärer ===")
        for i, item in enumerate(user_history, start=1):
            print(f"\nAffär {i}:")
            print(f"  Köpesumma: {item['Köpesumma']:,.0f} kr")
            print(f"  Renovering: {item['Renovering']:,.0f} kr")
            print(f"  Försäljningspris: {item['Försäljningspris']:,.0f} kr")
            print(f"  Vinst: {item['Vinst']:,.0f} kr")
            print(f"  Månadskostnad inkl. avgift: {item['Månadskostnad inkl. avgift']:,.0f} kr/mån")