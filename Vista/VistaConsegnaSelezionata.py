from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QFormLayout, QHBoxLayout, QVBoxLayout
from Gestione.GestoreConsegna import GestoreConsegna

class VistaConsegnaSelezionata(QWidget):
    def __init__(self, gestoreConsegna, consegna_selezionata):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.consegna_selezionata = consegna_selezionata
        