from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QVBoxLayout

from Vista.VisteConsegna.VistaEffettuaConsegna import VistaEffettuaConsegna
from Vista.VisteConsegna.VistaRimandaConsegna import VistaRimandaConsegna
from Vista.VisteConsegna.VistaModificaOrarioConsegna import VistaModificaOrarioConsegna


class VistaColloSelezionato(QWidget):
    def __init__(self, gestoreConsegna, collo_selezionato, contatore):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.collo_selezionato = collo_selezionato
        self.contatore = contatore
        self.setWindowTitle(f"Opzioni Consegna {self.contatore}")
        self.setFixedSize(300,350)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.get_generic_button(f"Consegna collo {self.contatore}", self.effettua_consegna, gestoreConsegna, collo_selezionato))
        vlayout.addWidget(self.get_generic_button(f"Rimanda consegna del collo {self.contatore}", self.rimanda_consegna, gestoreConsegna, collo_selezionato))
        vlayout.addWidget(self.get_generic_button(f"Modifica orario consegna del collo {self.contatore}", self.modifica_orario_consegna, gestoreConsegna, collo_selezionato))
        self.setLayout(vlayout)
        
    def get_generic_button(self, titolo, on_click, argument1, argument2):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(lambda : on_click(argument1, argument2))
        return button
    
    def effettua_consegna(self, gestoreConsegna, consegna_selezionata):
        self.effettuaConsegna = VistaEffettuaConsegna(gestoreConsegna, consegna_selezionata)
        self.effettuaConsegna.show()
        self.close()
    
    def rimanda_consegna(self, gestoreConsegna, consegna_selezionata):
        self.rimanda_consegna = VistaRimandaConsegna(gestoreConsegna, consegna_selezionata)
        self.rimanda_consegna.show()
        self.close()
    
    def modifica_orario_consegna(self, gestoreConsegna, consegna_selezionata):
        self.modifica_orario = VistaModificaOrarioConsegna(gestoreConsegna, consegna_selezionata)
        self.modifica_orario.show()
        self.close()