from Attivita.LettoreFile import LettoreFile
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo
from Attivita.LettoreFile import LettoreFile
from datetime import time

class GestoreRitiro():
    def __init__(self):
        self.listaRitiriLettura = LettoreFile().leggi_ritiri()
        self.listaColliRitiriLettura = LettoreFile().leggi_lista_colli()
        self.listaRitiriPositivi = []
        self.listaRitiriNegativi = []
        self.listaColliPositivi = []
        self.listaColliNegativi = []
    
    def ricercaRitiroByCodice(self, codice):
        for ritiro in self.listaRitiriLettura:
            if codice == ritiro.datiRitiro.codiceRitiro:
                return True
        return False
    
    def ricercaColloByCodice(self, codice):
        for collo in self.listaColliRitiriLettura:
            if codice == collo.datiRitiro.codiceRitiro:
                return True
        return False
    
    def ricercaRitiroLettura(self, ritiro):
        if ritiro in self.listaRitiriLettura:
            
            return True
        return False
    
    def ricercaColloLettura(self, collo):
        if collo in self.listaColliRitiriLettura:
            
            return True
        return False
    
    def confermaRitiro(self, ritiro_confermato):
        if isinstance(ritiro_confermato, Pacco):
            if self.ricercaRitiroLettura(ritiro_confermato) and ritiro_confermato.datiRitiro.statoRitiro!="Ritirato":
                self.listaRitiriPositivi.append(ritiro_confermato)
                self.getRitiroLettura(ritiro_confermato).datiRitiro.setStatoRitiro("Ritirato")
                self.listaRitiriLettura.remove(ritiro_confermato)
                return True
        elif isinstance(ritiro_confermato, Collo):
            if self.ricercaColloLettura(ritiro_confermato) and ritiro_confermato.datiRitiro.statoRitiro!="Ritirato":
                self.listaColliPositivi.append(ritiro_confermato)
                self.getColloLettura(ritiro_confermato).datiRitiro.setStatoRitiro("Ritirato")
                self.listaColliRitiriLettura.remove(ritiro_confermato)
                return True
        return False
    
    def rimandaRitiro(self, ritiro_annullato, nuova_data):
        if isinstance(ritiro_annullato, Pacco):
            if self.ricercaRitiroLettura(ritiro_annullato) and ritiro_annullato.datiRitiro.statoRitiro!="Ritiro rimandato":
                self.getRitiroLettura(ritiro_annullato).datiRitiro.setDataRitiro(nuova_data)
                self.getRitiroLettura(ritiro_annullato).datiRitiro.setStatoRitiro("CRitiro rimandato")
                self.listaRitiriNegativi.append(ritiro_annullato)
                self.listaRitiriLettura.remove(ritiro_annullato)
                return True
        elif isinstance(ritiro_annullato, Collo):
            if self.ricercaColloLettura(ritiro_annullato) and ritiro_annullato.datiRitiro.statoRitiro!="Ritiro rimandato":
                self.getColloLettura(ritiro_annullato).datiRitiro.setDataRitiro(nuova_data)
                self.getColloLettura(ritiro_annullato).datiRitiro.setStatoRitiro("Ritiro rimandato")
                self.listaColliNegativi.append(ritiro_annullato)
                self.listaColliRitiriLettura.remove(ritiro_annullato)
                return True
        return False
    
    def modificaStatoRitiro(self, ritiro, nuovo_stato):
        if isinstance(ritiro, Pacco):
            if self.ricercaRitiroLettura(ritiro):
                self.getRitiroLettura(ritiro).datiRitiro.setStatoRitiro(nuovo_stato)
                return True
        elif isinstance(ritiro, Collo):
            if self.ricercaColloLettura(ritiro):
                self.getColloLettura(ritiro).datiRitiro.setStatoRitiro(nuovo_stato)
        return False
    
    def ricercaRitiroPositivo(self, ritiro):
        if ritiro in self.listaRitiriPositivi:
            return True
        return False
    
    def ricercaColloPositivo(self, collo):
        if collo in self.listaColliPositivi:
            return True
        return False
    
    def getRitiroLetturaByCodice(self, codice):
        for ritiro in self.listaRitiriLettura:
            if codice == ritiro.datiRitiro.codiceRitiro:
                return ritiro
        return None
    
    def getRitiroLettura(self, ritiro):
        if ritiro in self.listaRitiriLettura:
            return ritiro
        return None
    
    def getColloLetturaByCodice(self, codice):
        for collo in self.listaColliRitiriLettura:
            if codice == collo.datiRitiro.codiceRitiro:
                return collo
        return None
    
    def getColloLettura(self, collo):
        if collo in self.listaColliRitiriLettura:
            return collo
        return None
    
    def modificaOrarioRitiro(self, ritiro_selezionato, nuovo_orario):

        nuovo_orario = time.fromisoformat(nuovo_orario)
    
        if isinstance(ritiro_selezionato, Pacco):
            for ritiro in self.listaRitiriLettura:

                ritiro.datiRitiro.oraRitiro = time.fromisoformat(ritiro.datiRitiro.oraRitiro)
                
                if nuovo_orario == ritiro.datiRitiro.oraRitiro:
                    return None  
                
                return True
                ritiro_selezionato.datiRitiro.setOraRitiro(nuovo_orario)
    
        elif isinstance(ritiro_selezionato, Collo):
            for collo in self.listaColliRitiriLettura:
                # Converte anche gli orari aziendali
                collo.datiRitiro.oraRitiro = time.fromisoformat(collo.datiRitiro.oraRitiro)
                collo.aziendaMittente.orarioApertura = time.fromisoformat(collo.aziendaMittente.orarioApertura)
                collo.aziendaMittente.orarioChiusura = time.fromisoformat(collo.aziendaMittente.orarioChiusura)
                
                if nuovo_orario == collo.datiRitiro.oraRitiro or nuovo_orario > collo.aziendaMittente.orarioChiusura or nuovo_orario < collo.aziendaMittente.orarioApertura:
                    return None
                
                ritiro_selezionato.datiRitiro.setOraRitiro(nuovo_orario)

        if isinstance(ritiro_selezionato, Pacco):
            for ritiro in self.listaRitiriLettura:
                if nuovo_orario == ritiro.datiRitiro.oraRitiro:
                    return False
                return ritiro_selezionato.datiRitiro.setOraRitiro(nuovo_orario)
        elif isinstance(ritiro_selezionato, Collo):
            for collo in self.listaColliRitiriLettura:
                if nuovo_orario == collo.datiRitiro.oraRitiro:
                    return False
                elif nuovo_orario > ritiro.aziedaMittente.orarioChiusura or nuovo_orario < ritiro.aziendaMittente.orarioApertura:
                    return False
                return ritiro_selezionato.datiRitiro.setOraRitiro(nuovo_orario)
        
    def getColloLetturaByCodice(self, codice):
        for collo in self.listaColliRitiriLettura:
            if codice == collo.datiRitiro.codiceRitiro:
                return collo
        return None
    
    def depositaRitiriPositivi(self):
        self.listaRitiriPositivi.clear()
        self.listaColliPositivi.clear()