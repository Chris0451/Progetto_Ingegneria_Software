from Attivita.LettoreFile import LettoreFile

class GestoreConsegna():
    def __init__(self):
        self.codiceConsegne = ""
        self.listaConsegne = LettoreFile().read_consegne()
        self.listaColliConsegne = []
        self.listaConsegnePositive = []
        self.listaConsegneNegative = []
        self.listaColliPositivi = []
        self.listaColliNegativi = []
        self.incassoContrassegno = 0.0
        
    def confermaConsegna(self, consegna_confermata):
        self.listaConsegnePositive.append(consegna_confermata)
    
    def rimandaConsegna(self, consegna_annullata, nuova_data):
        consegna_annullata.consegna.setDataConsegna(nuova_data)
        self.listaConsegneNegative.append(consegna_annullata)
    
    def modificaStatoConsegna(self, consegna, nuovo_stato):
        self.getConsegna(consegna).datiConsegna.setStatoConsegna(nuovo_stato)

    def modificaIncassoContrassegno(self, consegna):
        if self.getConsegna(consegna).datiConsegna.metodoPagamento == "Contrassegno":
            self.incassoContrassegno += self.getConsegna(consegna).datiConsegna.valoreContrassegno

    def ricercaConsegna(self, consegna):
        if consegna in self.listaConsegne:
            return True
        return False
    
    def ricercaConsegnaByCodice(self, codice):
        for consegna in self.listaConsegne:
            if codice == consegna.datiConsegna.codiceConsegna:
                return True
        return False
    
    def getConsegna(self, consegna):
        if consegna in self.listaConsegne:
            return consegna
        return None
    
    def getConsegnaByCodice(self, codice):
        for consegna in self.listaConsegne:
            if codice == consegna.datiConsegna.codiceConsegna:
                return consegna
        return None
        
    