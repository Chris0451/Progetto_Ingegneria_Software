from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QVBoxLayout
from Vista.VistaConsegnaSelezionata import VistaConsegnaSelezionata

class VistaConsegneStandard(QWidget):
    def __init__(self, gestoreConsegna):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        vlayout = QVBoxLayout()
        self.resize(400, 600)
        self.setWindowTitle("Lista consegne standard")
        i = 1
        for consegna in gestoreConsegna.listaConsegne:
            vlayout.addWidget(self.get_generic_button(f"Consegna {i}\n\n Destinatario: {consegna.destinatario.nome} {consegna.destinatario.cognome}\n Indirizzo: {consegna.destinatario.posizione.via} {consegna.destinatario.posizione.civico}\n Stato consegna: {consegna.datiConsegna.statoConsegna}", self.opzioni_consegna, gestoreConsegna, consegna, i))
            i += 1
        self.indietro = QPushButton("Indietro")
        vlayout.addWidget(self.indietro)
        self.setLayout(vlayout)
        self.initUI()
        
    def initUI(self):
        self.indietro.setStyleSheet("font-size: 15px; font-family: Arial;")
        self.indietro.clicked.connect(self.submit_chiusura)
    
    def get_generic_button(self, titolo, on_click, argument1, argument2, argument3):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(lambda : on_click(argument1, argument2, argument3))
        return button
     
    def opzioni_consegna(self, gestoreConsegna, consegna, contatore):
        self.consegna_selezionata = VistaConsegnaSelezionata(gestoreConsegna, consegna, contatore)
        self.consegna_selezionata.show()
    
    def submit_chiusura(self):
        self.close()