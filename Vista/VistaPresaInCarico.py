from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QLineEdit, QLabel, QFormLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class VistaPresaInCarico(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conferma consegna")
        self.resize(500,200)
        self.titolo = QLabel("Inserisci codice consegna: ")
        self.inserimento_codice = QLineEdit(self)
        self.conferma = QPushButton("Conferma", self)
        self.initUI()
        
    def initUI(self):
        layout1 = QFormLayout()
        layout1.addRow(self.titolo, self.inserimento_codice)
        layout1.addRow(self.conferma)
        self.conferma.setGeometry(0,0,100,80)
        self.setLayout(layout1)
        self.titolo.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.inserimento_codice.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.conferma.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.conferma.clicked.connect(self.submit)
        
    def submit(self):
        codice = self.inserimento_codice.text()
        if codice is not "":
            print(f"Codice confermato: {codice}")
        