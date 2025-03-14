from Attivita.LettoreFile import LettoreFile
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo

class GestoreConsegna():
    def __init__(self):
        self.listaConsegneLettura = LettoreFile().leggi_consegne()
        self.listaColliConsegneLettura = LettoreFile().leggi_lista_colli_consegne()
        self.listaConsegne = []
        self.listaColliConsegne = []
        self.listaConsegnePositive = []
        self.listaConsegneNegative = []
        self.listaColliPositivi = []
        self.listaColliNegativi = []
        self.incassoContrassegno = 0.0
    
    def presaInCarico(self, consegna_selezionata):
        if isinstance(consegna_selezionata, Pacco):
            self.listaConsegne.append(consegna_selezionata)
            return self.modificaStatoConsegna(consegna_selezionata, "In transito")
        elif isinstance(consegna_selezionata, Collo):
            self.listaColliConsegne.append(consegna_selezionata)
            return self.modificaStatoConsegna(consegna_selezionata, "In transito")
        return False
        
    def confermaConsegna(self, consegna_confermata):
        if isinstance(consegna_confermata, Pacco):
            if self.ricercaConsegna(consegna_confermata) and consegna_confermata.datiConsegna.statoConsegna!="Consegnato":
                self.aggiornaIncassoContrassegno(consegna_confermata)
                self.listaConsegnePositive.append(consegna_confermata)
                self.modificaStatoConsegna(consegna_confermata, "Consegnato")
                self.listaConsegne.remove(consegna_confermata)
                return True
        elif isinstance(consegna_confermata, Collo):
            if self.ricercaCollo(consegna_confermata) and consegna_confermata.datiConsegna.statoConsegna!="Consegnato":
                self.listaColliPositivi.append(consegna_confermata)
                self.modificaStatoConsegna(consegna_confermata, "Consegnato")
                self.listaColliConsegne.remove(consegna_confermata)
                return True
        return False
    
    def rimandaConsegna(self, consegna_annullata, nuova_data):
        if isinstance(consegna_annullata, Pacco):
            if self.ricercaConsegna(consegna_annullata) and consegna_annullata.datiConsegna.statoConsegna!="Consegna rimandata":
                self.getConsegna(consegna_annullata).datiConsegna.setDataConsegna(nuova_data)
                self.modificaStatoConsegna(consegna_annullata, "Consegna rimandata")
                self.listaConsegneNegative.append(consegna_annullata)
                self.listaConsegne.remove(consegna_annullata)
                return True
        elif isinstance(consegna_annullata, Collo):
            if self.ricercaCollo(consegna_annullata) and consegna_annullata.datiConsegna.statoConsegna!="Consegna rimandata":
                self.getCollo(consegna_annullata).datiConsegna.setDataConsegna(nuova_data)
                self.modificaStatoConsegna(consegna_annullata, "Consegna rimandata")
                self.listaColliNegativi.append(consegna_annullata)
                self.listaColliConsegne.remove(consegna_annullata)
                return True
        return False
    
    def modificaStatoConsegna(self, consegna, nuovo_stato):
        if isinstance(consegna, Pacco):
            if self.ricercaConsegna(consegna):
                self.getConsegna(consegna).datiConsegna.setStatoConsegna(nuovo_stato)
                return True
        elif isinstance(consegna, Collo):
            if self.ricercaCollo(consegna):
                self.getCollo(consegna).datiConsegna.setStatoConsegna(nuovo_stato)
        return False
    
    def modificaOrarioConsegna(self, consegna, nuovo_orario):
        if isinstance(consegna, Pacco):
            if self.ricercaConsegna(consegna):
                self.getConsegna(consegna).datiConsegna.setOraConsegna(nuovo_orario)
                return True
        elif isinstance(consegna, Collo):
            if self.ricercaCollo(consegna):
                self.getConsegna(consegna).datiConsegna.setOraConsegna(nuovo_orario)
                return True
        return False
    
    def aggiornaIncassoContrassegno(self, consegna):
        if self.getConsegna(consegna).metodoPagamento == "Contrassegno":
            self.incassoContrassegno += self.getConsegna(consegna).datiConsegna.valoreContrassegno
            return True
        return False
    
    def depositaConsegneNegative(self):
        for consegna in self.listaConsegneNegative:
            self.modificaStatoConsegna(consegna, "Ritorno in deposito")
        for consegna in self.listaColliNegativi:
            self.modificaStatoConsegna(consegna, "Ritorno in deposito")
        self.incassoContrassegno = 0.0
        self.listaColliNegativi.clear()
        self.listaConsegneNegative.clear()

    # ******************************************************
    
    def ricercaConsegna(self, consegna):
        if consegna in self.listaConsegne:
            return True
        return False
    
    def ricercaConsegnaByCodice(self, codice):
        for consegna in self.listaConsegne:
            if codice == consegna.datiConsegna.codiceConsegna:
                return True
        return False
    
    def ricercaConsegnaLetturaByCodice(self, codice):
        for consegna in self.listaConsegneLettura:
            if codice == consegna.datiConsegna.codiceConsegna:
                return True
        return False
    
    def ricercaConsegnaPositiva(self, consegna):
        if consegna in self.listaConsegnePositive:
            return True
        return False
    
    def ricercaCollo(self, collo):
        if collo in self.listaColliConsegne:
            return True
        return False
    
    def ricercaColloPositivo(self, collo):
        if collo in self.listaColliPositivi:
            return True
        return False
    
    def ricercaColloByCodice(self, codice):
        for collo in self.listaColliConsegne:
            if codice == collo.datiConsegna.codiceConsegna:
                return True
        return False
    
    def ricercaColloLetturaByCodice(self, codice):
        for collo in self.listaColliConsegneLettura:
            if codice == collo.datiConsegna.codiceConsegna:
                return True
        return False
    
    # *****************************************************
    
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
                return collo
        return None
    
    def getColloLettura(self, collo):
        if collo in self.listaColliConsegneLettura:
            return collo
        return None
    
    def getColloLetturaByCodice(self, codice):
        for collo in self.listaColliConsegneLettura:
            if codice == collo.datiConsegna.codiceConsegna:
                return collo
        return None
        
    