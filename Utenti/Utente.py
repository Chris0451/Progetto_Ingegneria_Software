class Utente:
    def __init__(self, nome, cognome, codiceFiscale, telefono, email):
        self.nome = nome
        self.cognome = cognome
        self.codiceFiscale = codiceFiscale
        self.telefono = telefono
        self.email = email
    def getInfoUtente(self):
        return f"Nome e cognome: {self.nome} {self.cognome}\nCodice fiscale: {self.codiceFiscale}\n"
    
        