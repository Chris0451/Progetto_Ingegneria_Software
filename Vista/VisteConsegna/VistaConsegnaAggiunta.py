from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFormLayout
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo

class VistaConsegnaAggiunta(QWidget):
    def __init__(self, consegna_aggiunta):
        super().__init__()
        self.consegna_aggiunta = consegna_aggiunta
        self.resize(400,100)
        self.setWindowTitle("Aggiunta consegna confermata")
        if isinstance(consegna_aggiunta, Pacco):
            self.label_conferma = QLabel("Pacco preso in carico correttamente")
            self.click_conferma = QPushButton("Okay", self)
            self.click_conferma.clicked.connect(self.submit)
            self.initUI()
        elif isinstance(consegna_aggiunta, Collo):
            self.label_conferma = QLabel("Collo preso in carico correttamente")
            self.click_conferma = QPushButton("Okay", self)
            self.click_conferma.clicked.connect(self.submit)
            self.initUI()
        
    def initUI(self):
        layout = QFormLayout()
        layout.addRow(self.label_conferma)
        layout.addRow(self.click_conferma)
        self.setLayout(layout)
        self.label_conferma.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.click_conferma.setStyleSheet("font-size: 20px; font-family: Arial; font-weight: bold;")
        
    def submit(self):
        self.close()
        