class Cliente():
    def __init__(self,  nome, cognome, codiceFiscale, data_nascita, telefono, email, password, identificativo, codiceCliente, posizione):
        self.nome = nome
        self.cognome = cognome
        self.codiceFiscale = codiceFiscale
        self.telefono = telefono
        self.email = email
        self.identificativo = identificativo
        self.codiceCliente = codiceCliente
        self.posizione = posizione
    def getInfoCliente(self):
        return self.getInfoUtente(self) + f", codice cliente: {self.codiceCliente}, info posizione: {self.posizione.getInfoPosizione()}"