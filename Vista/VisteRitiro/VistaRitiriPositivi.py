from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget

class VistaRitiriPositivi(QWidget):
    def __init__(self, gestoreRitiro):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.resize(600, 250)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Ritiri positivi")
        layout = QVBoxLayout()
        self.listaRitiriPositivi = QListWidget()
        i = 0
        for ritiroPositivo in self.gestoreRitiro.listaRitiriPositivi:
            self.listaRitiriPositivi.insertItem(i, f"Ritiro n. {ritiroPositivo.datiRitiro.codiceRitiro}")
            i+=1
        layout.addWidget(self.listaRitiriPositivi)
        self.setLayout(layout)