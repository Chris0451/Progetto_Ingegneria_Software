class Consegna:
    def __init__ (self, codiceConsegna, dataConsegna, oraConsegna, statoConsegna, valoreContrassegno):
        self.codiceConsegna = codiceConsegna
        self.dataConsegna = dataConsegna
        self.oraConsegna = oraConsegna
        self.statoConsegna = statoConsegna
        self.valoreContrassegno = valoreContrassegno
    def getValoreContrassegno(self):
            return self.valoreContrassegno
    def setDataConsegna(self, newDataConsegna):
        self.dataConsegna = newDataConsegna
    def setStatoConsegna(self, newStatoConsegna):
        self.statoConsegna = newStatoConsegna
    def setOraConsegna(self, newOraConsegna):
        self.oraConsegna = newOraConsegna
    def getInfoConsegna(self, codiceConsegna, dataConsegna, oraConsegna, statoConsegna, valoreContrassegno):
        print(f"Codice Consegna: {self.codiceConsegna}\n")
        print(f"Data Consegna: {self.dataConsegna}\n")
        print(f"Ora Consegna: {self.oraConsegna}\n")
        print(f"Stato Consegna: {self.statoConsegna}\n")
        print(f"Valore Contrassegno: {self.valoreContrassegno}\n")  
        
        