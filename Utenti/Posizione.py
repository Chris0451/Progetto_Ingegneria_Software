class Posizione:
    def __init__(self, via, civico, comune, provincia, CAP):
        self.via = via
        self.civico = civico
        self.comune = comune
        self.provincia = provincia
        self.CAP = CAP
    def infoPosizione(self):
        return f"Via {self.via}, n. {self.civico} - Comune di {self.comune} - Provincia di {self.provincia} - CAP: {self.CAP}"
