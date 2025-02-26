from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLabel

from Vista.VistaPresaInCarico import VistaPresaInCarico
from Vista.VisteConsegna.VistaConsegne import VistaConsegne
from Vista.VisteRitiro.VistaRitiri import VistaRitiri
from Vista.VistaDepositoPacchi import VistaDepositoPacchi

class VistaAccessoCorriere(QWidget):
        
    def __init__(self, gestoreConsegna, gestoreRitiro, corriere):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.gestoreRitiro = gestoreRitiro
        label_corriere = QLabel(f"Ciao {corriere.nome} - Codice Corriere: {corriere.identificativo}")
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        label_corriere.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold")
        vlayout.addWidget(label_corriere)
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
    
    def go_listaRitiri(self, gestoreRitiro):
        self.listaRitiri = VistaRitiri(gestoreRitiro)
        self.listaRitiri.show()
    
    def go_deposito(self, gestoreConsegna, gestoreRitiro):
        self.effettuaDeposito = VistaDepositoPacchi(gestoreConsegna, gestoreRitiro)
        self.effettuaDeposito.show()