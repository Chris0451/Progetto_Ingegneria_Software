from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QVBoxLayout

from Vista.VisteRitiro.VistaEffettuaRitiro import VistaEffettuaRitiro
from Vista.VisteRitiro.VistaRimandaRitiro import VistaRimandaRitiro
from Vista.VisteRitiro.VistaModificaOrarioRitiro import VistaModificaOrarioRitiro


class VistaRitiroSelezionato(QWidget):
    def __init__(self, gestoreRitiro, ritiro_selezionato, contatore):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.ritiro_selezionato = ritiro_selezionato
        self.contatore = contatore
        self.setWindowTitle(f"Opzioni Ritiro {self.contatore}")
        self.setFixedSize(300,350)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.get_generic_button(f"Ritira pacco {self.contatore}", self.effettua_ritiro, gestoreRitiro, ritiro_selezionato))
        vlayout.addWidget(self.get_generic_button(f"Rimanda ritiro {self.contatore}", self.rimanda_ritiro, gestoreRitiro, ritiro_selezionato))
        vlayout.addWidget(self.get_generic_button(f"Modifica orario ritiro {self.contatore}", self.modifica_orario_ritiro, gestoreRitiro, ritiro_selezionato))
        self.setLayout(vlayout)
        
    def get_generic_button(self, titolo, on_click, argument1, argument2):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(lambda : on_click(argument1, argument2))
        return button
    
    def effettua_ritiro(self, gestoreRitiro, ritiro_selezionato):
        self.effettuaRitiro = VistaEffettuaRitiro(gestoreRitiro, ritiro_selezionato)
        self.effettuaRitiro.show()
        self.close()
    
    def rimanda_ritiro(self, gestoreRitiro, ritiro_selezionato):
        pass
        self.rimanda_ritiro = VistaRimandaRitiro(gestoreRitiro, ritiro_selezionato)
        self.rimanda_ritiro.show()
        self.close()
    
    def modifica_orario_ritiro(self, gestoreRitiro, ritiro_selezionato):
        self.modifica_orario = VistaModificaOrarioRitiro(gestoreRitiro, ritiro_selezionato)
        self.modifica_orario.show()
        self.close()