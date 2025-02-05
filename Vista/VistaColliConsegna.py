from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFormLayout

class VistaColliConsegna(QWidget):
    def __init__(self, gestoreConsegna):
        self.gestoreConsegna = gestoreConsegna