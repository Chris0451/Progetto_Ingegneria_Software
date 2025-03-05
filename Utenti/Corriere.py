from Utenti.Utente import Utente
class Corriere(Utente):
    def __init__(self, nome, cognome, codiceFiscale, telefono, email, partitaIVA, CAP):
        super().__init__(nome, cognome, codiceFiscale, telefono, email)
        self.partitaIVA = partitaIVA
        self.CAP = CAP
    def infoCorriere(self):
        return self.getInfoUtente() + "\nIdentificativo corriere: {self.partitaIVA}"
    