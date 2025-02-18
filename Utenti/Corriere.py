from Utenti.Utente import Utente
class Corriere(Utente):
    def __init__(self, nome, cognome, codiceFiscale, data_nascita, telefono, email, identificativo):
        super().__init__(nome, cognome, codiceFiscale, data_nascita, telefono, email, identificativo)
        self.identificativo = identificativo
    def infoCorriere(self):
        return self.getInfoUtente() + "\nIdentificativo corriere: {self.identificativo}"
    