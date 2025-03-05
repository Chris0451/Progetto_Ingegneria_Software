from Attivita.LettoreFile import LettoreFile
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo
from Attivita.LettoreFile import LettoreFile
from datetime import datetime

class GestoreRitiro():
    def __init__(self):
        self.listaRitiriLettura = LettoreFile().leggi_ritiri()
        self.listaColliRitiriLettura = LettoreFile().leggi_lista_colli()
        self.listaRitiriPositivi = []
        self.listaRitiriNegativi = []
        self.listaColliPositivi = []
        self.listaColliNegativi = []
    
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
                self.getRitiroLettura(ritiro_annullato).datiRitiro.setStatoRitiro("Ritiro rimandato")
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

    def modificaOrarioRitiro(self, ritiro_selezionato, nuovo_orario):
        # Converte il nuovo orario in formato time se non lo è già
        if isinstance(nuovo_orario, str):
            nuovo_orario = datetime.strptime(nuovo_orario, "%H:%M").time()
        # Controllo per oggetto Pacco
        if isinstance(ritiro_selezionato, Pacco):
            for ritiro in self.listaRitiriLettura:
                if nuovo_orario == ritiro.datiRitiro.oraRitiro:
                    return False  # Orario già esistente
            self.getRitiroLettura(ritiro_selezionato).datiRitiro.setOraRitiro(nuovo_orario.strftime("%H:%M"))
            return True  # Orario modificato con successo
    
        # Controllo per oggetto Collo
        elif isinstance(ritiro_selezionato, Collo):
            orario_apertura = ritiro_selezionato.aziendaMittente.orarioApertura
            orario_chiusura = ritiro_selezionato.aziendaMittente.orarioChiusura
    
            # Converte gli orari in formato time se sono stringhe
            if isinstance(orario_apertura, str):
                orario_apertura = datetime.strptime(orario_apertura, "%H:%M").time()
            if isinstance(orario_chiusura, str):
                orario_chiusura = datetime.strptime(orario_chiusura, "%H:%M").time()
    
            # Controllo se l'orario è fuori dall'orario aziendale
            if nuovo_orario < orario_apertura or nuovo_orario > orario_chiusura:
                return False  # Orario non valido
            
            # Controllo se il nuovo orario coincide con un altro ritiro già esistente
            for collo in self.listaColliRitiriLettura:
                if collo != ritiro_selezionato and collo.datiRitiro.oraRitiro == nuovo_orario:
                    return False  # Orario già impostato per un altro ritiro
            
            # Imposta il nuovo orario
            self.getColloLettura(ritiro_selezionato).datiRitiro.setOraRitiro(nuovo_orario.strftime("%H:%M"))
            return True  # Orario modificato con successo
    
        return False  # Caso generico di fallimento

    def modificaStatoRitiro(self, ritiro, nuovo_stato):
        if isinstance(ritiro, Pacco):
            if self.ricercaRitiroLettura(ritiro):
                self.getRitiroLettura(ritiro).datiRitiro.setStatoRitiro(nuovo_stato)
                return True
        elif isinstance(ritiro, Collo):
            if self.ricercaColloLettura(ritiro):
                self.getColloLettura(ritiro).datiRitiro.setStatoRitiro(nuovo_stato)
        return False
    

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

    
    def ricercaRitiroPositivo(self, ritiro):
        if ritiro in self.listaRitiriPositivi:
            return True
        return False
    
    def ricercaColloPositivo(self, collo):
        if collo in self.listaColliPositivi:
            return True
        return False

    ###############################################
    
    def getRitiroLetturaByCodice(self, codice):
        for ritiro in self.listaRitiriLettura:
            if codice == ritiro.datiRitiro.codiceRitiro:
                return ritiro
        return None
    
    def getRitiroLettura(self, ritiro):
        if ritiro in self.listaRitiriLettura:
            return ritiro
        return None
    
    def getRitiroNegativoByCodice(self, codice):
        for ritiro in self.listaRitiriNegativi:
            if codice == ritiro.datiRitiro.codiceRitiro:
                return ritiro
        return None
    
    def getColloPositivoByCodice(self, codice):
        for collo in self.listaColliPositivi:
            if codice == collo.datiRitiro.codiceRitiro:
                return collo
        return None
    
    def getColloNegativoByCodice(self, codice):
        for collo in self.listaColliNegativi:
            if codice == collo.datiRitiro.codiceRitiro:
                return collo
        return None
    
    def getRitiroPositivoByCodice(self, codice):
        for ritiro in self.listaRitiriPositivi:
            if codice == ritiro.datiRitiro.codiceRitiro:
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
    
    def depositaRitiriPositivi(self):
        self.listaRitiriPositivi.clear()
        self.listaColliPositivi.clear()
        

