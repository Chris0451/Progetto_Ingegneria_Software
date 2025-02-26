from Utenti.Utente import Utente
class Corriere(Utente):
    def __init__(self, nome, cognome, codiceFiscale, telefono, email, identificativo):
        super().__init__(nome, cognome, codiceFiscale, telefono, email)
        self.identificativo = identificativo
    def infoCorriere(self):
        return self.getInfoUtente() + "\nIdentificativo corriere: {self.identificativo}"
    