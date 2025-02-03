from Attivita.Pacco import Pacco
from Attivita.Collo import Collo
from Attivita.Consegna import Consegna

class GestoreConsegna():
    def __init__(self):
        codiceConsegne = ""
        listaConsegne = []
        listaConsegnePositive = []
        listaConsegneNegative = []
        
    def aggiungiConsegne(self, consegne):
        self.listaConsegne = consegne
        
    def confermaConsegna(self, consegna_confermata):
        self.listaConsegnePositive.append(consegna_confermata)
    
    def rimandaConsegna(self, consegna_annullata, nuova_data):
        consegna_annullata.consegna.setDataConsegna(nuova_data)
        self.listaConsegneNegative.append(consegna_annullata)
     
    def ricercaConsegna(self, consegna):
        if consegna in self.listaConsegne:
            return True
        
    
        
    