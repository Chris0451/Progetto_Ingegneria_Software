class Ritiro:
    def __init__ (self, codiceRitiro, dataRitiro, oraRitiro, statoRitiro):
        self.codiceRitiro = codiceRitiro
        self.dataRitiro = dataRitiro
        self.oraRitiro = oraRitiro
        self.statoRitiro = statoRitiro
    def setDataRitiro(self, newDataRitiro):
         self.dataRitiro = newDataRitiro
    def setOraRitiro(self, newOraRitiro):
         self.oraRitiro = newOraRitiro
    def setStatoRitiro(self, newStatoRitiro):
         self.statoRitiro = newStatoRitiro
    def getInfoRitiro(self):
         return f"Codice Ritiro: {self.codiceRitiro}\nData Ritiro: {self.dataRitiro}\nOra Ritiro: {self.oraRitiro}\nStato Ritiro: {self.statoRitiro}\n"
        
  
         