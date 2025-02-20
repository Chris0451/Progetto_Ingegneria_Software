from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QFormLayout, QHBoxLayout, QLabel
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo

class VistaConsegnaConfermata(QWidget):
    def __init__(self, gestoreConsegna, consegna_selezionata):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.consegna_selezionata = consegna_selezionata
        self.setWindowTitle("Consegna effettuata")
        self.setFixedSize(450,100)
        if isinstance(consegna_selezionata, Pacco):
            if self.gestoreConsegna.confermaConsegna(self.consegna_selezionata):
                self.label_conferma = QLabel("Consegna effettuata e inserita nella lista delle consegne positive")
                self.button_conferma = QPushButton("Okay")
                flayout = QFormLayout()
                flayout.addRow(self.label_conferma)
                flayout.addRow(self.button_conferma)
                self.setLayout(flayout)
            elif consegna_selezionata.datiConsegna.statoConsegna == "Consegna rimandata":
                self.label_conferma = QLabel("Consegna rimandata in precedenza")
                self.button_conferma = QPushButton("Okay")
                flayout = QFormLayout()
                flayout.addRow(self.label_conferma)
                flayout.addRow(self.button_conferma)
                self.setLayout(flayout)
            else:
                self.label_conferma = QLabel("Errore nella consegna del pacco: pacco consegnato in precedenza")
                self.button_conferma = QPushButton("Okay")
                flayout = QFormLayout()
                flayout.addRow(self.label_conferma)
                flayout.addRow(self.button_conferma)
                self.setLayout(flayout)
        elif isinstance(consegna_selezionata, Collo):
            if self.gestoreConsegna.confermaConsegna(self.consegna_selezionata):
                self.label_conferma = QLabel("Consegna del collo effettuata e inserita nella lista dei colli positive")
                self.button_conferma = QPushButton("Okay")
                flayout = QFormLayout()
                flayout.addRow(self.label_conferma)
                flayout.addRow(self.button_conferma)
                self.setLayout(flayout)
            elif consegna_selezionata.datiConsegna.statoConsegna == "Consegna rimandata":
                self.label_conferma = QLabel("Consegna rimandata in precedenza")
                self.button_conferma = QPushButton("Okay")
                flayout = QFormLayout()
                flayout.addRow(self.label_conferma)
                flayout.addRow(self.button_conferma)
                self.setLayout(flayout)
            else:
                self.label_conferma = QLabel("Errore nella consegna del collo: collo consegnato in precedenza")
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
        