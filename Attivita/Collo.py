from Attivita.Consegna import Consegna
from Attivita.Ritiro import Ritiro

class Collo:
    def __init__ (self, codiceCollo, naturaCollo, peso, volume, aziendaMittente, aziendaDestinatario, datiRitiro, datiConsegna):
        self.codiceCollo = codiceCollo
        self.naturaCollo = naturaCollo
        self.peso = peso
        self.volume = volume
        self.aziendaMittente = aziendaMittente
        self.aziendaDestinatario = aziendaDestinatario
        self.datiRitiro = datiRitiro 
        self.datiConsegna = datiConsegna
    def getInfoColloConsegna(self):
        return f"Codice Collo: {self.codiceCollo}\nNatura Collo: {self.naturaCollo}\n\nAzienda Mittente:\n"+self.aziendaMittente.getInfoAzienda()+"\nAzienda Destinatario:\n"+self.aziendaDestinatario.getInfoAzienda()+"\nDati Consegna:\n" + self.datiConsegna.getInfoConsegna()
    def getInfoColloRitiro(self):
        return f"Codice Collo: {self.codiceCollo}\nNatura Collo: {self.naturaCollo}\n\nAzienda Mittente:\n"+self.aziendaMittente.getInfoAzienda()+"\nAzienda Destinatario:\n"+self.aziendaDestinatario.getInfoAzienda()+"\nDati Ritiro:\n" + self.datiRitiro.getInfoRitiro()