from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QVBoxLayout
from Gestione.GestoreRitiro import GestoreRitiro
from Vista.VisteRitiro.VistaRitiroAziendaleSelezionato import VistaRitiroAziendaleSelezionato

class VistaRitiriAziendali(QWidget):
    def __init__(self, gestoreRitiro):
        super().__init__()
        self.gestoreRitiro = GestoreRitiro()
        vlayout = QVBoxLayout()
        self.resize(400, 600)
        self.setWindowTitle("Lista colli da ritirare")
        i = 1
        for collo in gestoreRitiro.listaColliRitiriLettura:
            vlayout.addWidget(self.get_generic_button(f"Collo {i}\n\n Codice: {collo.codiceCollo}\n Natura: {collo.naturaCollo}\n Azienda Mittente: {collo.aziendaMittente.nomeAzienda}\nIndirizzo: {collo.aziendaMittente.responsabile.posizione.getInfoPosizione()} Orario apertura: {collo.aziendaMittente.orarioApertura}\n Orario chiusura: {collo.aziendaMittente.orarioChiusura}", self.opzioni_ritiro, gestoreRitiro, collo, i))
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
        self.ritiro_selezionato = VistaRitiroAziendaleSelezionato(gestoreRitiro, ritiro, contatore)
        self.ritiro_selezionato.show()
    
    def submit_chiusura(self):
        self.close()