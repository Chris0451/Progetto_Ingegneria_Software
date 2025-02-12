from Utenti.Utente import Utente
class Cliente(Utente):
    def __init__(self,  nome, cognome, email, telefono, codiceFiscale, codiceCliente, posizione):
        super().__init__(nome, cognome, codiceFiscale, telefono, email)
        self.nome = nome
        self.cognome = cognome
        self.codiceFiscale = codiceFiscale
        self.telefono = telefono
        self.email = email
        self.codiceCliente = codiceCliente
        self.posizione = posizione
    def getInfoCliente(self):
        return self.getInfoUtente() + f"Codice cliente: {self.codiceCliente}\nInfo posizione:\n"+self.posizione.getInfoPosizione()