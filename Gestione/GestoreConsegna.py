from Attivita.LettoreFile import LettoreFile
import datetime

class GestoreConsegna():
    def __init__(self):
        self.codiceConsegne = ""
        self.listaConsegneLettura = LettoreFile().leggi_consegne()
        self.listaColliConsegneLettura = LettoreFile().leggi_lista_colli_consegne()
        self.listaConsegne = []
        self.listaColliConsegne = []
        self.listaConsegnePositive = []
        self.listaConsegneNegative = []
        self.listaColliPositivi = []
        self.listaColliNegativi = []
        self.incassoContrassegno = 0.0
    
    def presaInCaricoConsegnaStandard(self, codice):
        consegna_selezionata = self.getConsegnaLetturaByCodice(codice)
        if consegna_selezionata != None:
            self.listaConsegne.append(consegna_selezionata)
            return self.modificaStatoConsegna(consegna_selezionata, "In transito")
        return False
        
    def presaInCaricoCollo(self, codice):
        collo_selezionato = self.getColloLetturaByCodice(codice)
        if collo_selezionato != None:
            self.listaColliConsegne.append(collo_selezionato)
            return self.modificaStatoConsegna(collo_selezionato, "In transito")
        
    def confermaConsegna(self, consegna_confermata):
        if self.ricercaConsegna(consegna_confermata) and consegna_confermata.datiConsegna.statoConsegna!="Consegnato":
            self.listaConsegnePositive.append(consegna_confermata)
            self.getConsegna(consegna_confermata).datiConsegna.setStatoConsegna("Consegnato")
            return True
        return False
    
    def rimandaConsegna(self, consegna_annullata, nuova_data):
        if self.ricercaConsegna(consegna_annullata) and consegna_annullata.datiConsegna.statoConsegna!="Consegna rimandata":
            self.getConsegna(consegna_annullata).datiConsegna.setDataConsegna(nuova_data)
            self.getConsegna(consegna_annullata).datiConsegna.setStatoConsegna("Consegna rimandata")
            self.listaConsegneNegative.append(consegna_annullata)
            return True
        return False
    
    def modificaStatoConsegna(self, consegna, nuovo_stato):
        if self.ricercaConsegna(consegna):
            self.getConsegna(consegna).datiConsegna.setStatoConsegna(nuovo_stato)
            return True
        return False
    
    def modificaOrarioConsegna(self, consegna, nuovo_orario):
        pass

    def aggiornaIncassoContrassegno(self, consegna):
        if self.getConsegna(consegna).datiConsegna.metodoPagamento == "Contrassegno":
            self.incassoContrassegno += self.getConsegna(consegna).datiConsegna.valoreContrassegno
            return True
        return False
    
    def ricercaConsegna(self, consegna):
        if consegna in self.listaConsegne:
            return True
        return False
    
    def ricercaConsegnaByCodice(self, codice):
        for consegna in self.listaConsegne:
            if codice == consegna.datiConsegna.codiceConsegna:
                return True
        return False
    
    def ricercaCollo(self, collo):
        if collo in self.listaColliConsegne:
            return True
        return False
    
    def ricercaColloByCodice(self, codice):
        for collo in self.listaColliConsegne:
            if codice == collo.datiConsegna.codiceConsegna:
                return True
        return False
    
    def getConsegna(self, consegna):
        if consegna in self.listaConsegne:
            return consegna
        return None
    
    def getConsegnaLettura(self, consegna):
        if consegna in self.listaConsegneLettura:
            return consegna
        return None
    
    def getConsegnaByCodice(self, codice):
        for consegna in self.listaConsegne:
            if codice == consegna.datiConsegna.codiceConsegna:
                return consegna
        return None
    
    def getConsegnaLetturaByCodice(self, codice):
        for consegna in self.listaConsegneLettura:
            if codice == consegna.datiConsegna.codiceConsegna:
                return consegna
        return None
    
    def getCollo(self, collo):
        if collo in self.listaColliConsegne:
            return collo
        return None
    
    def getColloByCodice(self, codice):
        for collo in self.listaColliConsegne:
            if codice == collo.datiConsegna.codiceConsegna:
                return True
        return False
    
    def getColloLettura(self, collo):
        if collo in self.listaColliConsegneLettura:
            return collo
        return None
    
    def getColloLetturaByCodice(self, codice):
        for collo in self.listaColliConsegneLettura:
            if codice == collo.datiConsegna.codiceConsegna:
                return True
        return False
        
    