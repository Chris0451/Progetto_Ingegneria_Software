from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QVBoxLayout, QListWidget

class VistaConsegnePositive(QWidget):
    def __init__(self, gestoreConsegna):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.resize(600, 250)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Consegne positive")
        layout = QVBoxLayout()
        self.listaConsegnePositive = QListWidget()
        i = 0
        for consegnaPositiva in self.gestoreConsegna.listaConsegnePositive:
            self.listaConsegnePositive.insertItem(i, f"Consegna n. {consegnaPositiva.datiConsegna.codiceConsegna}")
            i+=1
        layout.addWidget(self.listaConsegnePositive)
        self.setLayout(layout)
        
        