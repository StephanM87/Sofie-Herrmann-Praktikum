class Glees():
    def __init__(self, sektor, bereich):
        self.sektor = sektor
        self.bereich = bereich     
        
class Planung(Glees):
    def __init__(self, sektor, bereich, tag, uhrzeit):
        super().__init__(sektor, bereich)
        self.tag = tag
        self.uhrzeit = uhrzeit
    def nächstes_wochenende(self):
        print("Treffpunkt: " + self.bereich + ", " + self.sektor + ", " + self.tag + " um " + self.uhrzeit)
        if self.sektor == "Westblöcke":
            print("Werkzeug mitnehmen")

test = Planung("Westblöcke", "Orthank", "Samstag", "10:30")
test.nächstes_wochenende()
