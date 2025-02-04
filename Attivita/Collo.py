class Collo:
    def __init__ (self, codiceCollo, naturaCollo, peso, volume, aziendaMittente, aziendaDestinatario, ritiro, consegna):
        self.codiceCollo = codiceCollo
        self.naturaCollo = naturaCollo
        self.peso = peso
        self.volume = volume
        self.aziendaMittente = aziendaMittente
        self.aziendaDestinatario = aziendaDestinatario
        self.ritiro = ritiro 
        self.consegna = consegna
    def getInfoCollo(self, codiceCollo, naturaCollo, aziendaMittente, aziendaDestinatario):
        print(f"Codice Collo: {self.codiceCollo}\n")
        print(f"Natura Collo: {self.naturaCollo}\n")
        print(f"Azienda Mittente: {self.aziendaMittente}\n")
        print(f"Azienda Destinatario: {self.aziendaDestinatario}\n")
        print("Ritiro: " + self.ritiro.getInfoRitiro())
        print("Consegna: " + self.consegna.getInfoConsegna())
        
        
        