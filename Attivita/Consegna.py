class Consegna:
    def __init__ (self, codiceConsegna, dataConsegna, oraConsegna, statoConsegna, valoreContrassegno):
        self.codiceConsegna = codiceConsegna
        self.dataConsegna = dataConsegna
        self.oraConsegna = oraConsegna
        self.statoConsegna = statoConsegna
        self.valoreContrassegno = valoreContrassegno
    def setDataConsegna(self, newDataConsegna):
        self.dataConsegna = newDataConsegna
    def setStatoConsegna(self, newStatoConsegna):
        self.statoConsegna = newStatoConsegna
    def setOraConsegna(self, newOraConsegna):
        self.oraConsegna = newOraConsegna
    def getInfoConsegna(self):
        return f"Codice Consegna: {self.codiceConsegna}\nData Consegna: {self.dataConsegna}\nOra Consegna: {self.oraConsegna}\nStato Consegna: {self.statoConsegna}\nValore Contrassegno: {self.valoreContrassegno}\n" 
        
        