class Azienda():
    def __init__(self, responsabile, indirizzoFatturazione, nomeAzienda, orarioApertura, giorniApertura):
        self.responsabile = responsabile
        self.indirizzoFatturazione = indirizzoFatturazione
        self.nomeAzienda = nomeAzienda
        self.orarioApertura = orarioApertura
        self.giorniApertura = giorniApertura
    def getInfoAzienda(self):
        return f"Responsabile Azienda: {self.responsabile.getInfoCliente}, indirizzo fatturazione: {self.indirizzoFatturazione}, nome azienda: {self.nomeAzienda}, self. "