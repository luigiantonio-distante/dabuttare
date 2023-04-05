class Carta:
    def __init__(self, valore, seme):
        self.valore=valore
        self.seme=seme
    def __str__(self):
        return str(self.valore) + " " + self.seme

