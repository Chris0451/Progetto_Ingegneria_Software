from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFormLayout

class VistaConsegnaPresente(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,100)
        self.setWindowTitle("Consegna presente")
        self.label_conferma = QLabel("Codice consegna inserito precedentemente")
        self.click_conferma = QPushButton("Okay", self)
        self.click_conferma.clicked.connect(self.submit)
        self.initUI()
        
    def initUI(self):
        layout = QFormLayout()
        layout.addRow(self.label_conferma)
        layout.addRow(self.click_conferma)
        self.setLayout(layout)
        self.label_conferma.setStyleSheet("font-size: 20px; font-family: Arial; font-weight: bold;")
        self.click_conferma.setStyleSheet("font-size: 20px; font-family: Arial; font-weight: bold;")
        
    def submit(self):
        self.close()