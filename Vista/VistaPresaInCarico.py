from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QFormLayout, QHBoxLayout
from Vista.VisteConsegna.VistaConsegnaAggiunta import VistaConsegnaAggiunta
from Vista.VisteConsegna.VistaConsegnaNonAggiunta import VistaConsegnaNonAggiunta
from Vista.VisteConsegna.VistaConsegnaPresente import VistaConsegnaPresente
from Vista.VisteConsegna.VistaConsegneAssegnate import VistaConsegneAssegnate

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
        self.lista_assegnata = QPushButton("Lista assegnata")
        self.initUI()
        
    def initUI(self):
        layout1 = QFormLayout()
        layout2 = QHBoxLayout()
        layout1.addRow(self.titolo, self.inserimento_codice)
        layout2.addWidget(self.indietro)
        layout2.addWidget(self.conferma)
        layout1.addRow(layout2)
        layout1.addRow(self.lista_assegnata)
        self.setLayout(layout1)
        self.titolo.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.inserimento_codice.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.conferma.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.indietro.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.lista_assegnata.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.conferma.clicked.connect(self.submit_lettura)
        self.indietro.clicked.connect(self.submit_chiusura)
        self.lista_assegnata.clicked.connect(self.submit_consegne_assegnate)
        
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
        
    
    def submit_consegne_assegnate(self):
        self.consegne_assegnate = VistaConsegneAssegnate(self.gestoreConsegna)
        self.consegne_assegnate.show()
    
    def submit_chiusura(self):
        self.close()
        
        
        