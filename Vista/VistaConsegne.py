from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QLineEdit, QLabel, QFormLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Attivita.LettoreFile import LettoreFile

class VistaConsegne(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        self.setWindowTitle("Visualizzazione consegne assegnate")
        self.initUI()
        
        
    def initUI(self):
        hlayout = QHBoxLayout()
        vlayout1 = QVBoxLayout()
        vlayout2 = QVBoxLayout()
        vlayout1.addWidget(self.get_generic_button("Lista Consegne Standard", self.go_consegneStandard))
        vlayout1.addWidget(self.get_generic_button("Lista Colli da consegnare", self.go_colliConsegna))
        vlayout1.addWidget(self.get_generic_button("Consegne Positive", self.go_consegnePositive))
        vlayout2.addWidget(self.get_generic_button("ColliiPositivi", self.go_colliPositivi))
        vlayout2.addWidget(self.get_generic_button("Consegne Rimandate", self.go_consegneRimandate))
        vlayout2.addWidget(self.get_generic_button("Colli Rimandate", self.go_colliRimandati))
        hlayout.addLayout(vlayout1)
        hlayout.addLayout(vlayout2)
        self.setLayout(hlayout)
        
    def get_generic_button(self, titolo, on_click):
        pass
    
    def go_consegneStandard(self):
        pass
    def go_colliConsegna(self):
        pass
    def go_consegnePositive(self):
        pass
    def go_colliPositivi(self):
        pass
    def go_consegneRimandate(self):
        pass
    def go_colliRimandati(self):
        pass