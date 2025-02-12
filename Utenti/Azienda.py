class Azienda():
    def __init__(self, responsabile, indirizzoAzienda, nomeAzienda, orarioApertura, orarioChiusura, giorniApertura):
        self.responsabile = responsabile
        self.indirizzoAzienda = self.responsabile.posizione
        self.nomeAzienda = nomeAzienda
        self.orarioApertura = orarioApertura
        self.orarioChiusura = orarioChiusura
        self.giorniApertura = giorniApertura
    def getInfoAzienda(self):
        return f"Nome azienda: {self.nomeAzienda}\nResponsabile Azienda:\n" + self.responsabile.getInfoCliente() + f"Orario apertura: {self.orarioApertura} {self.orarioChiusura}\nGiorni apertura: {', '.join(self.giorniApertura)}\n" 