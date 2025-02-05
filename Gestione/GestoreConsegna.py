from Attivita.LettoreFile import LettoreFile
import datetime

class GestoreConsegna():
    def __init__(self):
        self.codiceConsegne = ""
        self.listaConsegne = LettoreFile().leggi_consegne()
        self.listaColliConsegne = LettoreFile().leggi_lista_colli_consegne()
        self.listaConsegnePositive = []
        self.listaConsegneNegative = []
        self.listaColliPositivi = []
        self.listaColliNegativi = []
        self.incassoContrassegno = 0.0
        
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
        
    