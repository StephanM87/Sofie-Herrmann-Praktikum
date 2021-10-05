class Klettergebiet():
    
    def __init__(self, sicherungsmittel, seil, sicherungsgerät):
        print("der falsche constructor läufrt")

        
    def Einführen(self, sicherungsmittel, seil, sicherungsgerät):
        print("hallo Welt")
        self.sicherungsmittel = sicherungsmittel
        self.seil = seil
        self.sicherungsgerät = sicherungsgerät
    
    def einpacken(self):
        print("Nicht vergessen: " + self.sicherungsmittel + ", " + self.seil + " & " + self.sicherungsgerät)

gebiet = Klettergebiet("Exen", "70m Seil", "ATC")
gebiet.Einführen("Exen", "70m Seil", "ATC")
gebiet.einpacken()



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

'''
class Ettringen(Klettergebiet):
    def __init__(self, sicherungsmittel, seil, sicherungsgerät, friends):
        super().__init__(sicherungsmittel, seil, sicherungsgerät)
        self.friends = friends
    def einpacken(self):
        return "Nicht vergessen: " + self.sicherungsmittel + ", " + self.seil + ", " + self.sicherungsgerät + " & " + self.friends

'''





try:
    bestes_gebiet_der_welt = Glees("Crashpad", "Chalkbag", "Stahlbürsten")
    print(bestes_gebiet_der_welt.einpacken())
except Exception as e:
    print ("Du hast was vergessen", e)
'''
try:
    ettringen = Ettringen("Exen", "70m Seil", "ATC", "Friends")
    ettringen.init()
except Exception as e:
    print ("Wird das ein free solo oder was?", e)
'''