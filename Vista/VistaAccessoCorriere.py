from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy

from Vista.VistaPresaInCarico import VistaPresaInCarico
from Vista.VistaConsegne import VistaConsegne

class VistaAccessoCorriere(QWidget):
        
    def __init__(self, parent=None):
        super(VistaAccessoCorriere, self).__init__(parent)
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        vlayout.addWidget(self.get_generic_button("Presa in Carico Pacco", self.go_presaInCarico))
        hlayout.addWidget(self.get_generic_button("Visualizza lista consegne", self.go_listaConsegne))
        hlayout.addWidget(self.get_generic_button("Visualizza lista ritiri", self.go_listaRitiri))
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.get_generic_button("Deposita pacchi", self.go_deposito))
        self.setLayout(vlayout)
        self.setFixedSize(450,300)
        self.setWindowTitle("Profilo Corriere")
    
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(on_click)
        return button
    
    def go_presaInCarico(self):
        self.presa_in_carico = VistaPresaInCarico()
        self.presa_in_carico.show()
    
    def go_listaConsegne(self):
        self.listaConsegne = VistaConsegne()
        self.listaConsegne.show()
        pass
    
    def go_listaRitiri(self):
        self.visualizza_ritiri = VistaVisualizzaListaRitiri()
        self.visualizza_ritiri.show()
    
    def go_deposito(self):
            pass