import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QLineEdit, QLabel, QFormLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Attivita.LettoreFile import LettoreFile

class VistaConsegne(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        self.windowTitle("Visualizzazione consegne assegnate")
        
    def initUI(self):
        layout1 = QFormLayout()
        self.setLayout(layout1)
        