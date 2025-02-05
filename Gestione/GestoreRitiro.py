from Attivita.LettoreFile import LettoreFile

class GestoreRitiro():
    def __init__(self):
        # self.codiceConsegne = ""
        self.listaRitiri = LettoreFile().leggi_ritiri()
        self.listaColliRitiri = LettoreFile().leggi_lista_colli()
        self.listaRitiriPositivi = []
        self.listaRitiriNegativi = []
        self.listaColliPositivi = []
        self.listaColliNegativi = []
        
        
    def confermaRitiro(self, ritiro_confermato):
        self.listaRitiriPositivi.append(ritiro_confermato)
    
    def rimandaRitiro(self, ritiro_annullato, nuova_data):
        ritiro_annullato.datiRitiro.setDatiRitiro(nuova_data)
        self.listaRitiriNegativi.append(ritiro_annullato)
    
    def modificaStatoRitiro(self, ritiro, nuovo_stato):
        self.getRitiro(ritiro).datiRitiro.setStatoRitiro(nuovo_stato)

    def ricercaRitiro(self, ritiro):
        if ritiro in self.listaRitiri:
            return True
        return False
    
    def ricercaRitiroByCodice(self, codice):
        for ritiro in self.listaRitiri:
            if codice == ritiro.datiRitiro.codiceRitiro:
                return True
        return False
    
    def getRitiro(self, ritiro):
        if ritiro in self.listaRitiri:
            return ritiro
        return None
    
    def getRitiroByCodice(self, codice):
        for ritiro in self.listaRitiri:
            if codice == ritiro.datiRitiro.codiceRitiro:
                return ritiro
        return None
        
        
    