from Utenti.Cliente import Cliente
from enum import Enum
import datetime
class Pacco:
    destinatario: Cliente
    mittente: Cliente
    class StatoPacco(Enum):
        Transito = 1
        PressoFiliale = 2
        Consegnato = 3
    statoPacco = StatoPacco
    def __init__ (self, peso, dimensioni, giornoSpedizione, giornoConsegna, destinatario, mittente):
        self.peso = peso
        self.dimensioni = dimensioni
        self.giornoSpedizione = giornoSpedizione
        self.giornoConsegna = giornoConsegna
        self.destinatario = destinatario
        self.mittente = mittente
        self.statoPacco = None
    def setStatoPacco(self, newState):
        if newState != 1 or newState != 2 or newState != 3:
            self.statoPacco.value = newState
    def getPeso(self):
        return self.peso
    def getDimensioni(self):
        return self.dimensioni
    def getIndirizzoMittente(self):
        return self.indirizzoMittente
    def getMittente(self):
        return self.mittente
    def getDestinatario(self):
        return self.destinatario