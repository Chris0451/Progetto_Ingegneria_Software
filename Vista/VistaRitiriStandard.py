from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QFormLayout, QHBoxLayout, QVBoxLayout
from Gestione.GestoreRitiro import GestoreRitiro

class VistaRitiriStandard(QWidget):
    def __init__(self):
        super().__init__()
        gestoreRitiro = GestoreRitiro()
        vlayout = QVBoxLayout()
        self.resize(400, 600)
        self.setWindowTitle("Lista ritiri standard")
        i = 1
        for ritiro in gestoreRitiro.listaRitiri:
            vlayout.addWidget(self.get_generic_button(f"Ritiro {i}\n\n Destinatario: {ritiro.destinatario.nome} {ritiro.destinatario.cognome}\n Indirizzo: {ritiro.destinatario.posizione.via} {ritiro.destinatario.posizione.civico}", self.opzioni_ritiro, gestoreRitiro, ritiro))
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
     
    def opzioni_ritiro(self, gestoreRitiro, ritiro):
        print("Bottone selezionato")
        pass
    
    def submit_chiusura(self):
        self.close()