class BolanApp:
    def __init__(self):
        self.resultat = 0
        self.lägenhetspris = 0
        self.renoveringskostnad = 0
        self.avgift = 0
        self.försäljningspris = 0
        self.vinst = 0

    def bolan(self, lägenhetspris, lånebelopp, räntan, år):
        self.lägenhetspris = lägenhetspris
        
        månads_räntan = (räntan / 100) / 12
        månader = år * 12
        månads_kostnad = (lånebelopp * månads_räntan) / (1 - (1 + månads_räntan) ** -månader)

        self.resultat = round(månads_kostnad, 2)
        return self.resultat

    def renovering(self, valda_renoveringar, egen_kostnad=0):
        priser = {
            "1": 70000, "2": 130000, "3": 20000, "4": 20000,
            "5": 7000, "6": 10000, "7": 80000, "8": 30000, "9": 0
        }

        total_extra = egen_kostnad
        
        for val in valda_renoveringar:
            if val in priser:
                total_extra += priser[val]

        self.renoveringskostnad = total_extra
        extra_per_månad = total_extra / (10 * 12)
        self.resultat = round(self.resultat + extra_per_månad, 2)

        return total_extra, self.resultat

    def lägg_till_avgift(self, avgift):
        self.avgift = avgift
        self.resultat = round(self.resultat + avgift, 2)
        return self.resultat

    def försäljning(self, försäljningspris):
        self.försäljningspris = försäljningspris
        total_kostnad = self.lägenhetspris + self.renoveringskostnad
        self.vinst = self.försäljningspris - total_kostnad
        return self.vinst