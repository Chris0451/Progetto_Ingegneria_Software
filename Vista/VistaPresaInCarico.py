import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QLineEdit, QLabel, QFormLayout, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Attivita.LettoreFile import LettoreFile
from Vista.VistaConsegnaConfermata import VistaConsegnaConfermata

class VistaPresaInCarico(QWidget) :
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,100)
        self.setWindowTitle("Conferma consegna")
        self.titolo = QLabel("Inserisci codice consegna: ")
        self.inserimento_codice = QLineEdit(self)
        self.conferma = QPushButton("Conferma", self)
        self.initUI()
        
        
    def initUI(self):
        layout1 = QFormLayout()
        layout1.addRow(self.titolo, self.inserimento_codice)
        layout1.addRow(self.conferma)
        self.setLayout(layout1)
        self.titolo.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.inserimento_codice.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.conferma.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.conferma.clicked.connect(self.submit)
        
    def submit(self):
        lettore = LettoreFile()
        pacchi = lettore.read_consegne()
        codice = self.inserimento_codice.text()
        for pacco in pacchi:
            if codice == pacco.consegna.codiceConsegna:
                print(f"Codice confermato: {codice}")
                pacco.consegna.setStatoConsegna("In transito")
                print(pacco.consegna.statoConsegna)
                self.consegna_confermata = VistaConsegnaConfermata()
                self.consegna_confermata.show()
            else:
                print("Codice errato o Nessun codice inserito")
        
        