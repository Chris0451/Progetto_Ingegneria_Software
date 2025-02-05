from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QFormLayout, QHBoxLayout, QVBoxLayout
from Gestione.GestoreRitiro import GestoreRitiro

class VistaColliRitirati(QWidget):
    def __init__(self):
        super().__init__()
        gestoreRitiro = GestoreRitiro()
        vlayout = QVBoxLayout()
        self.resize(400, 600)
        self.setWindowTitle("Lista colli ritirati")
        i = 1
        for collo in gestoreRitiro.listaColliRitiri:
            vlayout.addWidget(self.get_generic_button(f"Collo {i}\n\n Codice: {collo.codiceCollo}\n Natura: {collo.naturaCollo}\n Azienda Mittente: {collo.aziendaMittente.nomeAzienda}\n Orario apertura: {collo.aziendaMittente.orarioApertura}\n Orario chiusura: {collo.aziendaMittente.orarioChiusura}", self.opzioni_ritiro, gestoreRitiro, collo))
            i += 1
        self.indietro = QPushButton("Indietro")
        vlayout.addWidget(self.indietro)
        self.setLayout(vlayout)
        self.initUI()
        
    def initUI(self):
        self.indietro.setStyleSheet("font-size: 15px; font-family: Arial;")
        self.indietro.clicked.connect(self.submit_chiusura)
    
    def get_generic_button(self, titolo, on_click, argument1, argument2):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(lambda: on_click(argument1, argument2))
        return button
     
    def opzioni_ritiro(self, gestoreRitiro, collo):
        print("Bottone selezionato")
        pass
    
    def submit_chiusura(self):
        self.close()