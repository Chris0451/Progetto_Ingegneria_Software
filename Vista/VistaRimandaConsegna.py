from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFormLayout

class VistaRimandaConsegna(QWidget):
    def __init__(self, gestoreConsegna):
        self.gestoreConsegna = gestoreConsegna
        