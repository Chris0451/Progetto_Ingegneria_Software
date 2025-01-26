from Utente import *
class Corriere(Utente):
    def __init__(self, nome, cognome, codiceFiscale, data_nascita, telefono, email, identificativo):
        super().__init__(nome, cognome, codiceFiscale, data_nascita, telefono, email, password, identificativo)
        self.identificativo = identificativo
    def infoCorriere(self):
        return infoUtente(self) + ", Identificativo corriere: {self.identificativo}"
    