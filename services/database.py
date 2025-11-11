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
                if isinstance(data, list):
                    return data
                else:
                    return []
                
            except json.JSONDecodeError:
                return []

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.historik, f, indent=4)

    def spara_resultat(self, email, resultat):
        self.historik.append({"Email": email, "Resultat": resultat})
        self.save_data()
        print("\nResultatet har sparats.")

    def visa_historik(self, email):
        user_history = [h for h in self.historik if h["Email"] == email]
        if not user_history:
            print("\nIngen historik hittades.")
            return
        print("\nTidigare beräkningar:")
        for item in user_history:
            print(f" - {item['Resultat']} kr/mån")
