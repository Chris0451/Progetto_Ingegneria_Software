class Azienda():
    def __init__(self, responsabile, indirizzoAzienda, nomeAzienda, orarioApertura, orarioChiusura, giorniApertura):
        self.responsabile = responsabile
        self.indirizzoAzienda = indirizzoAzienda
        self.nomeAzienda = nomeAzienda
        self.orarioApertura = orarioApertura
        self.orarioChiusura = orarioChiusura
        self.giorniApertura = giorniApertura
    def getInfoAzienda(self):
        return f"Responsabile Azienda: {self.responsabile.getInfoCliente}, indirizzo fatturazione: {self.indirizzoFatturazione}, nome azienda: {self.nomeAzienda}, self. "