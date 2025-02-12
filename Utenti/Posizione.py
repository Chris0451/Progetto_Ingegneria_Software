class Posizione:
    def __init__(self, via, civico, comune, provincia, CAP):
        self.via = via
        self.civico = civico
        self.comune = comune
        self.provincia = provincia
        self.CAP = CAP
    def getInfoPosizione(self):
        return f"{self.via}, n. {self.civico}\nComune di {self.comune}\nProvincia: {self.provincia}\nCAP: {self.CAP}\n"
