class Collo:
    def __init__ (self, codiceCollo, naturaCollo, aziendaMittente, aziendaDestinatario):
        self.codiceCollo = codiceCollo
        self.naturaCollo = naturaCollo
        self.aziendaMittente = aziendaMittente
        self.aziendaDestinatario = aziendaDestinatario
    def getInfoCollo(self, codiceCollo, naturaCollo, aziendaMittente, aziendaDestinatario):
        print(f"Codice Collo: {self.codiceCollo}\n")
        print(f"Natura Collo: {self.naturaCollo}\n")
        print(f"Azienda Mittente: {self.aziendaMittente}\n")
        print(f"Azienda Destinatario: {self.aziendaDestinatario}\n")
        