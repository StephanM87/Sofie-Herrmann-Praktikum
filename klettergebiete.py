class Klettergebiet():
    def __init__(self, sicherungsmittel, seil, sicherungsgerät):
        self.sicherungsmittel = sicherungsmittel
        self.seil = seil
        self.sicherungsgerät = sicherungsgerät
    def einpacken(self):
        return "Nicht vergessen: " + self.sicherungsmittel + ", " + self.seil + " & " + self.sicherungsgerät
class Bouldergebiet():
    def __init__(self, crashpad, chalk):
        self.crashpad = crashpad
        self.chalk = chalk
    def einpacken(self):
        return self.crashpad + " und " + self.chalk + " mitnehmen"
class Glees(Bouldergebiet):
    def __init__(self, crashpad, chalk, werkzeug):
        super().__init__(crashpad, chalk)
        self.werkzeug = werkzeug
    def einpacken(self):
        return self.crashpad + ", " + self.chalk + " und " + self.werkzeug + " mitnehmen"
class Ettringen(Klettergebiet):
    def __init__(self, sicherungsmittel, seil, sicherungsgerät, friends):
        super().__init__(sicherungsmittel, seil, sicherungsgerät)
        self.friends = friends
    def einpacken(self):
        return "Nicht vergessen: " + self.sicherungsmittel + ", " + self.seil + ", " + self.sicherungsgerät + " & " + self.friends

try:
    bestes_gebiet_der_welt = Glees("Crashpad", "Chalkbag", "Stahlbürsten")
    print(bestes_gebiet_der_welt.einpacken())
except TypeError:
    print ("Du hast was vergessen")

try:
    ettringen = Ettringen("Exen", "70m Seil", "ATC", "Friends")
    print(ettringen.einpacken())
except TypeError:
    print ("Wird das ein free solo oder was?")