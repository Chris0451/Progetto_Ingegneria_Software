from PyQt5.QtWidgets import QWidget, QPushButton, QFormLayout, QHBoxLayout, QLabel

from Vista.VisteRitiro.VistaRitiroConfermato import VistaRitiroConfermato

class VistaEffettuaRitiro(QWidget):
    def __init__(self, gestoreRitiro, ritiro_selezionato):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.ritiro_selezionato = ritiro_selezionato
        self.setWindowTitle("Effettua ritiro")
        self.setFixedSize(400,100)
        self.titolo = QLabel("Effettuare il ritiro del pacco selezionato?")
        self.conferma = QPushButton("Sì")
        self.indietro = QPushButton("No")
        flayout = QFormLayout()
        hlayout = QHBoxLayout()
        flayout.addRow(self.titolo)
        hlayout.addWidget(self.conferma)
        hlayout.addWidget(self.indietro)
        flayout.addRow(hlayout)
        self.setLayout(flayout)
        self.initUI()
    
    def initUI(self):
        self.titolo.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold")
        self.conferma.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold")
        self.conferma.clicked.connect(lambda : self.submit_conferma(self.gestoreRitiro, self.ritiro_selezionato))
        self.indietro.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold")
        self.indietro.clicked.connect(lambda : self.close())
        
    def submit_conferma(self, gestoreRitiro, ritiro_selezionato):
        self.ritiro_confermato = VistaRitiroConfermato(gestoreRitiro, ritiro_selezionato)
        self.ritiro_confermato.show()
        self.close()