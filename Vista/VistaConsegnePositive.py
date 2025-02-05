from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QHBoxLayout

class VistaConsegnePositive(QWidget):
    def __init__(self, gestoreConsegna):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.resize(600, 250)
        self.setWindowTitle("Consegne positive")
        