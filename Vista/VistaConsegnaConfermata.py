import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QLineEdit, QLabel, QFormLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Attivita.LettoreFile import LettoreFile

class VistaConsegnaConfermata(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200,200)
        self.windowTitle("Consegna confermata")
        self.label_conferma = QLabel("Pacco preso in carico correttamente")
        self.click_conferma = QPushButton("Okay", self)
        self.click_conferma.clicked.connect(self.submit)
        self.initUI()
        
    def initUI(self):
        layout = QFormLayout()
        layout.addRow(self.label_conferma)
        layout.addRow(self.click_conferma)
        self.setLayout(layout)
        self.label_conferma.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.click_conferma.setStyleSheet("font-size: 20px; font-family: Arial;")
        
    def submit(self):
        pass
        