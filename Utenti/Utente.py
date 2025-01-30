class Utente:
    def __init__(self, nome, cognome, codiceFiscale, data_nascita, telefono, email, password, identificativo):
        self.nome = nome
        self.cognome = cognome
        self.codiceFiscale = codiceFiscale
        self.telefono = telefono
        self.email = email
        self.identificativo = identificativo
    def getInfoUtente(self):
        return f"Nome: {self.nome}, cognome: {self.cognome}, codice fiscale: {self.codiceFiscale}"
    
        