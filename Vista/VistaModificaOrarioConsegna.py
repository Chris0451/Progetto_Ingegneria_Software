from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFormLayout

class VistaModificaOrarioConsegna(QWidget):
    def __init__(self, gestoreConsegna, consegna_selezionata):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.consegna_selezionata = consegna_selezionata