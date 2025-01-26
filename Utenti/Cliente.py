from Utente import *
class Cliente(Utente):
    def __init__(self,  nome, cognome, codiceFiscale, data_nascita, telefono, email, password, identificativo, codiceCliente, posizione):
        super().__init__(nome, cognome, codiceFiscale, data_nascita, telefono, email, password, identificativo)
        self.codiceCliente = codiceCliente
        self.posizione = posizione
    def getInfoCliente(self):
        return getInfoUtente(self) + f", codice cliente: {sef.codiceCliente}, info posizione: {self.posizione.getInfoPosizione()}"