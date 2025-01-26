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
    def getInfoRitiro(self, codiceRitiro, dataRitiro, oraRitiro, statoRitiro):
         print(f"Codice Ritiro: {self.codiceRitiro}\n")
         print(f"Data Ritiro: {self.dataRitiro}\n")
         print(f"Ora Ritiro: {self.oraRitiro}\n")
         print(f"Stato Ritiro: {self.statoRitiro}\n")
        
  
         