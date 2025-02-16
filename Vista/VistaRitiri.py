from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QFormLayout, QHBoxLayout, QVBoxLayout
from Vista.VistaRitiriStandard import VistaRitiriStandard
from Vista.VistaColliRitirati import VistaColliRitirati

class VistaRitiri(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 250)
        self.setWindowTitle("Visualizzazione ritiri assegnati")
        self.initUI()
        
    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        qlayout = QFormLayout()
        hlayout1.addWidget(self.get_generic_button("Lista Ritiri\n Standard", self.go_ritiriStandard))
        hlayout1.addWidget(self.get_generic_button("Ritiri\n Positivi", self.go_ritiriPositivi))
        hlayout1.addWidget(self.get_generic_button("Ritiri\n Negativi", self.go_ritiriNegativi))
        hlayout2.addWidget(self.get_generic_button("Lista Ritiri\n Aziendali", self.go_listaRitiriAziendali))
        hlayout2.addWidget(self.get_generic_button("Colli\n Ritirati", self.go_colliRitirati))
        hlayout2.addWidget(self.get_generic_button("Colli\n Non Ritirati", self.go_colliNonRitirati))
        qlayout.addWidget(self.get_generic_button("Indietro", self.go_back))
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)
        vlayout.addLayout(qlayout)
        self.setLayout(vlayout)
        
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(on_click)
        return button
    
    def go_ritiriStandard(self):
        self.ritiri_standard = VistaRitiriStandard()
        self.ritiri_standard.show()
        pass
        
    def go_ritiriPositivi(self):
        pass
    
    def go_ritiriNegativi(self):
        pass
    
    def go_listaRitiriAziendali(self):
        pass
    
    def go_colliRitirati(self):
        self.colli_ritiri = VistaColliRitirati()
        self.colli_ritiri.show()
        pass
    
    def go_colliNonRitirati(self):
        pass
    
    def go_back(self):
        self.close()