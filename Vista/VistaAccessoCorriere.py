from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy

from Vista.VistaPresaInCarico import VistaPresaInCarico
from Vista.VistaConsegne import VistaConsegne

class VistaAccessoCorriere(QWidget):
        
    def __init__(self, gestoreConsegna, gestoreRitiro):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.gestoreRitiro = gestoreRitiro
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        vlayout.addWidget(self.get_generic_button("Presa in Carico Pacco", self.go_presaInCarico, gestoreConsegna))
        hlayout.addWidget(self.get_generic_button("Visualizza lista consegne", self.go_listaConsegne, gestoreConsegna))
        hlayout.addWidget(self.get_generic_button("Visualizza lista ritiri", self.go_listaRitiri, gestoreRitiro))
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.get_generic_button_2("Deposita pacchi", self.go_deposito, gestoreConsegna, gestoreRitiro))
        self.setLayout(vlayout)
        self.setFixedSize(450,300)
        self.setWindowTitle("Profilo Corriere")
    
    def get_generic_button(self, titolo, on_click, argument):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(lambda : on_click(argument))
        return button
    
    def get_generic_button_2(self, titolo, on_click, argument1, argument2):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(lambda : on_click(argument1, argument2))
        return button
    
    def go_presaInCarico(self, gestoreConsegna):
        self.presa_in_carico = VistaPresaInCarico(gestoreConsegna)
        self.presa_in_carico.show()
    
    def go_listaConsegne(self, gestoreConsegna):
        self.listaConsegne = VistaConsegne(gestoreConsegna)
        self.listaConsegne.show()
        pass
    
    def go_listaRitiri(self, gestoreRitiro):
        # self.visualizza_ritiri = VistaVisualizzaListaRitiri(gestoreRitiro)
        # self.visualizza_ritiri.show()
        pass
    
    def go_deposito(self, gestoreConsegna, gestoreRitiro):
        # self.deposito_pacchi = VistaDepositoPacchi(gestoreConsegna, gestoreRitiro)
        # self.deposito_pacchi.show()
        pass