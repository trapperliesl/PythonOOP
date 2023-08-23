class Fahrzeug():
    """ Klasse für das Erstellen von einem Fahrzeug """

    def __init__(self, farbe, baujahr, kmstand, sitze, marke):
        self.farbe   = farbe
        self.baujahr = baujahr
        self.kmstand = kmstand
        self.sitze   = sitze
        self.marke   = marke

    def tut_hupen(self, anzahl):
        # print("Der",self.marke,"hupt jetzt",anzahl,"mal:",anzahl * "tütüt ")
        print(f"Der {self.marke} hupt jetzt {anzahl} mal:" + anzahl * "tütüt ")
    
    def tut_fahren(self, km):
        print(f"Der{self.marke} fährt jetzt {km} Kilometer.")
        self.kmstand += km
        print(f"Der {self.marke} hat jetzt {self.kmstand} Kilometer auf dem Tacho.")

    def tut_parken(self):
        print("Der", self.marke, "parkt jetzt.")

    def zeigt_km_stand_an(self):
        print(f"Der Tacho des {self.marke} zeigt {self.kmstand} km an.")

class Pkw(Fahrzeug):
    """ Klasse für das Erstellen von einem Pkw """

    def __init__(self, farbe, baujahr, kmstand, sitze, marke, radio):
        super().__init__(farbe, baujahr, kmstand, sitze, marke)
        self.radio = radio

    def kofferraumvolumen(self, cbm):
        print(f"Der {self.marke} hat ein Kofferraumvolumen von {cbm} Kubikmeter")

class Lkw(Fahrzeug):
    """ Klasse für das Erstellen von einem Lkw """

    def __init__(self, farbe, baujahr, kmstand, sitze, marke):
        super().__init__(farbe, baujahr, kmstand, sitze, marke) 

    def tut_aufladen(self):
        print(f"Der {self.marke} lädt auf.") 

    def tut_parken(self):
        print(f"Der {self.marke} ist auf dem Firmenhof abgestellt.") 

    def fragt_nach_autoradio(self):
        autoradio = input("Welche Marke hat das Autoradio? ")
        print(f"In dem {self.marke} ist ein {autoradio} Radio verbaut.")

trabi = Pkw("rot", 1981, 143000, 4, "Trabi", "Blaupunkt")
trabi.tut_hupen(3)
trabi.tut_fahren(1000)
trabi.tut_parken()
trabi.zeigt_km_stand_an()
print(f"Der {trabi.marke} hat {trabi.sitze} Sitze.")
print(f"In dem {trabi.marke} ist ein {trabi.radio} Radio.")

volvo = Lkw ("grau", 2001, 245000, 6, "Volvo")
volvo.tut_hupen(5)
volvo.tut_fahren(6300)
volvo.tut_parken()
volvo.zeigt_km_stand_an()
print(f"Der {volvo.marke} hat {volvo.sitze} Sitze.")
volvo.fragt_nach_autoradio()

