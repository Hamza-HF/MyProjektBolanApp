import unittest
import sys
import os
import json
import tempfile
import shutil
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.database import Database
from services.bolanapp import BolanApp

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_database.json")
        self.db = Database(self.test_file)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_spara_och_hamta_resultat(self):
        app = BolanApp()
        app.lägenhetspris = 1000000
        app.renoveringskostnad = 200000
        app.försäljningspris = 1500000
        app.vinst = 300000
        app.resultat = 8000.50

        self.db.spara_resultat("hamza@test.com", app)
        
        self.assertEqual(len(self.db.historik), 1)
        self.assertEqual(self.db.historik[0]["Email"], "hamza@test.com")
        self.assertEqual(self.db.historik[0]["Köpesumma"], 1000000)

    def test_visa_historik_for_anvandare(self):
        app1 = BolanApp()
        app1.lägenhetspris = 1000000
        app1.renoveringskostnad = 200000
        self.db.spara_resultat("alex1@test.com", app1)
        
        app2 = BolanApp()
        app2.lägenhetspris = 2000000
        app2.renoveringskostnad = 300000
        self.db.spara_resultat("kalle2@test.com", app2)
        
        user1_history = [h for h in self.db.historik if h["Email"] == "alex1@test.com"]
        
        self.assertEqual(len(user1_history), 1)
        self.assertEqual(user1_history[0]["Köpesumma"], 1000000)

    def test_tom_historik(self):
        db = Database(self.test_file)
        history = db.load_data()
        
        self.assertEqual(len(history), 0)

    def test_ladda_existerande_data(self):
        test_data = [
            {
                "Email": "hamza@test.com",
                "Köpesumma": 1000000,
                "Renovering": 200000,
                "Försäljningspris": 1500000,
                "Vinst": 300000,
                "Månadskostnad inkl. avgift": 8000.50
            }
        ]
        
        with open(self.test_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)
        
        db = Database(self.test_file)
        self.assertEqual(len(db.historik), 1)
        self.assertEqual(db.historik[0]["Email"], "hamza@test.com")

if __name__ == '__main__':
    unittest.main()