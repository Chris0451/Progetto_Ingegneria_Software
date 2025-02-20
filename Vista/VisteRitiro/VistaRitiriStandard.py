from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QVBoxLayout
from Gestione.GestoreRitiro import GestoreRitiro
from Vista.VisteRitiro.VistaRitiroSelezionato import VistaRitiroSelezionato

class VistaRitiriStandard(QWidget):
    def __init__(self, gestoreRitiro):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        vlayout = QVBoxLayout()
        self.resize(400, 600)
        self.setWindowTitle("Lista ritiri standard")
        i = 1
        for ritiro in gestoreRitiro.listaRitiriLettura:
            vlayout.addWidget(self.get_generic_button(f"Ritiro {i}\n\n Codice Ritiro: {ritiro.datiRitiro.codiceRitiro}\n Destinatario: {ritiro.destinatario.nome} {ritiro.destinatario.cognome}\n Indirizzo: {ritiro.destinatario.posizione.via} {ritiro.destinatario.posizione.civico}\n Stato: {ritiro.datiRitiro.statoRitiro}", self.opzioni_ritiro, gestoreRitiro, ritiro, i))
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
        button.clicked.connect(lambda: on_click(argument1, argument2, argument3))
        return button
    
    def opzioni_ritiro(self, gestoreRitiro, ritiro, contatore):
        self.ritiro_selezionato = VistaRitiroSelezionato(gestoreRitiro, ritiro, contatore)
        self.ritiro_selezionato.show()
    
    def submit_chiusura(self):
        self.close()