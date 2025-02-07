from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QFormLayout
from Vista.VistaConsegnaAggiunta import VistaConsegnaAggiunta
from Vista.VistaConsegnaNonAggiunta import VistaConsegnaNonAggiunta
from Vista.VistaConsegnaPresente import VistaConsegnaPresente


class VistaPresaInCarico(QWidget) :
    def __init__(self, gestoreConsegna):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.setFixedSize(500,150)
        self.setWindowTitle("Conferma consegna")
        self.titolo = QLabel("Inserisci codice consegna: ")
        self.inserimento_codice = QLineEdit(self)
        self.conferma = QPushButton("Conferma", self)
        self.indietro = QPushButton("Indietro", self)  
        self.initUI()
        
        
    def initUI(self):
        layout1 = QFormLayout()
        layout1.addRow(self.titolo, self.inserimento_codice)
        layout1.addRow(self.conferma)
        layout1.addRow(self.indietro)
        self.setLayout(layout1)
        self.titolo.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.inserimento_codice.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.conferma.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.indietro.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.conferma.clicked.connect(self.submit_lettura)
        self.indietro.clicked.connect(self.submit_chiusura)
        
    def submit_lettura(self):
        codice = self.inserimento_codice.text()
        if self.gestoreConsegna.ricercaConsegnaLetturaByCodice(codice):
            consegna_confermata = self.gestoreConsegna.getConsegnaLetturaByCodice(codice)
            if consegna_confermata.datiConsegna.statoConsegna != "In transito":
                if self.gestoreConsegna.ricercaConsegnaPositiva(consegna_confermata)==False:
                    self.gestoreConsegna.presaInCarico(consegna_confermata)
                    self.consegna_aggiunta = VistaConsegnaAggiunta(consegna_confermata)
                    self.consegna_aggiunta.show()
                else:
                    self.consegna_presente = VistaConsegnaPresente()
                    self.consegna_presente.show()
            else:
                self.consegna_presente = VistaConsegnaPresente()
                self.consegna_presente.show()
        elif self.gestoreConsegna.ricercaColloLetturaByCodice(codice):
                collo_confermato = self.gestoreConsegna.getColloLetturaByCodice(codice)
                if collo_confermato.datiConsegna.statoConsegna != "In transito":
                    if self.gestoreConsegna.ricercaColloPositivo(collo_confermato)==False:
                        self.gestoreConsegna.presaInCarico(collo_confermato)
                        self.consegna_aggiunta = VistaConsegnaAggiunta(collo_confermato)
                        self.consegna_aggiunta.show()
                    else:
                        self.consegna_presente = VistaConsegnaPresente()
                        self.consegna_presente.show()
                else:
                    self.consegna_presente = VistaConsegnaPresente()
                    self.consegna_presente.show()
        else:
            self.consegna_nonAggiunta = VistaConsegnaNonAggiunta()
            self.consegna_nonAggiunta.show()
        self.inserimento_codice.setText("")
        
    
    def submit_chiusura(self):
        self.close()
        
        
        