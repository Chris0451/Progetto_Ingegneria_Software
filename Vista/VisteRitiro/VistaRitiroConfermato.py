from PyQt5.QtWidgets import QWidget, QPushButton, QFormLayout, QLabel
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo

class VistaRitiroConfermato(QWidget):
    def __init__(self, gestoreRitiro, ritiro_selezionato):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.ritiro_selezionato = ritiro_selezionato
        self.setWindowTitle("Ritiro effettuato")
        self.setFixedSize(450,100)
        if isinstance(ritiro_selezionato, Pacco):
            if self.gestoreRitiro.confermaRitiro(self.ritiro_selezionato):
                self.label_conferma = QLabel("Ritiro effettuato e inserito nella lista dei ritiri positivi")
                self.button_conferma = QPushButton("Okay")
                flayout = QFormLayout()
                flayout.addRow(self.label_conferma)
                flayout.addRow(self.button_conferma)
                self.setLayout(flayout)
            else:
                self.label_conferma = QLabel("Errore nel ritiro del pacco: pacco ritirato in precedenza")
                self.button_conferma = QPushButton("Okay")
                flayout = QFormLayout()
                flayout.addRow(self.label_conferma)
                flayout.addRow(self.button_conferma)
                self.setLayout(flayout)
        elif isinstance(ritiro_selezionato, Collo):
            if self.gestoreRitiro.confermaRitiro(self.ritiro_selezionato):
                self.label_conferma = QLabel("Ritiro del collo effettuato e inserito nella lista dei colli positivi")
                self.button_conferma = QPushButton("Okay")
                flayout = QFormLayout()
                flayout.addRow(self.label_conferma)
                flayout.addRow(self.button_conferma)
                self.setLayout(flayout)
            else:
                self.label_conferma = QLabel("Errore nel ritiro del collo: collo ritirato in precedenza")
                self.button_conferma = QPushButton("Okay")
                flayout = QFormLayout()
                flayout.addRow(self.label_conferma)
                flayout.addRow(self.button_conferma)
                self.setLayout(flayout)
        self.initUI()
        
    def initUI(self):
        self.label_conferma.setStyleSheet("font-size: 15px; font-family: Arial;")
        self.button_conferma.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold")
        self.button_conferma.clicked.connect(lambda : self.close())