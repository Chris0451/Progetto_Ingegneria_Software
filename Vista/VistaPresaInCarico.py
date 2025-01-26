from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit

class VistaPresaInCarico(QWidget):
    def __init__(self):
        super().__init__()
        self.inserimento_codice = QLineEdit(self)
        
    def initUI(self):
        pass