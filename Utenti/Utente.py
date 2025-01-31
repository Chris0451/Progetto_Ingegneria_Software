class Utente:
    def __init__(self, nome, cognome, codiceFiscale, telefono, email):
        self.nome = nome
        self.cognome = cognome
        self.codiceFiscale = codiceFiscale
        self.telefono = telefono
        self.email = email
    def getInfoUtente(self):
        return f"Nome: {self.nome}, cognome: {self.cognome}, codice fiscale: {self.codiceFiscale}"
    
        