import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from services.bolanapp import BolanApp


def test_bolan_calculation():
    app = BolanApp()
    result = app.bolan(lägenhetspris=3000000, lånebelopp=2500000, räntan=5, år=30)
    assert 13000 < result < 14000


def test_renovering_och_avgift():
    app = BolanApp()
    app.bolan(3000000, 2500000, 5, 30)
    total, nytt_resultat = app.renovering(["1", "3"], egen_kostnad=10000)
    app.lägg_till_avgift(3000)
    assert total == 100000
    assert nytt_resultat > 13000
