from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QFormLayout, QHBoxLayout, QLabel

from Vista.VistaConsegnaConfermata import VistaConsegnaConfermata

class VistaEffettuaConsegna(QWidget):
    def __init__(self, gestoreConsegna, consegna_selezionata):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.consegna_selezionata = consegna_selezionata
        self.setWindowTitle("Effettua consegna")
        self.setFixedSize(400,100)
        self.titolo = QLabel("Effettuare la consegna del pacco selezionato?")
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
        self.conferma.clicked.connect(lambda : self.submit_conferma(self.gestoreConsegna, self.consegna_selezionata))
        self.indietro.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold")
        self.indietro.clicked.connect(lambda : self.close())
        
    def submit_conferma(self, gestoreConsegna, consegna_selezionata):
        self.consegna_confermata = VistaConsegnaConfermata(gestoreConsegna, consegna_selezionata)
        self.consegna_confermata.show()
        self.close()