from services.bolanapp import BolanApp

def test_login_sparar_user():
    app = BolanApp()
    app.anvandare = "test@test.se"
    assert app.anvandare == "test@test.se"

def test_spara_result():
    app = BolanApp()
    app.anvandare = "test@test.se"
    app.resultat = 5000
    langd = len(app.historik)
    app.spara_resultat()
    assert len(app.historik) == langd + 1
