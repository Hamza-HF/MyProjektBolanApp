import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.bolanapp import BolanApp

class TestBolanApp(unittest.TestCase):

    def setUp(self):
        self.app = BolanApp()

    def test_bolan_berakning(self):

        resultat = self.app.bolan(2000000, 1500000, 3.5, 30)
       
        self.assertIsInstance(resultat, float)
        self.assertGreater(resultat, 0)
        self.assertAlmostEqual(resultat, 6735.77, delta=100)

    def test_renovering(self):
        self.app.bolan(1000000, 800000, 4.0, 20)
        initial_kostnad = self.app.resultat
        
        total_renovering, ny_kostnad = self.app.renovering(["1", "2"], 50000)
        
        self.assertEqual(total_renovering, 250000)
    
        self.assertGreater(ny_kostnad, initial_kostnad)

    def test_forsaljning_med_vinst(self):
       
        self.app.lägenhetspris = 1000000
        self.app.renoveringskostnad = 200000
        vinst = self.app.försäljning(1500000)
        
        self.assertEqual(vinst, 300000) 

    def test_forsaljning_med_forlust(self):
        
        self.app.lägenhetspris = 1000000
        self.app.renoveringskostnad = 200000
        vinst = self.app.försäljning(800000)
        
        self.assertEqual(vinst, -400000)  

if __name__ == '__main__':
    unittest.main()