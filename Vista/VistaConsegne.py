from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QFormLayout, QHBoxLayout, QVBoxLayout
from Vista.VistaConsegneStandard import VistaConsegneStandard

class VistaConsegne(QWidget):
    def __init__(self, gestoreConsegne):
        super().__init__()
        self.gestoreConsegne = gestoreConsegne
        self.setFixedSize(600, 250)
        self.setWindowTitle("Visualizzazione consegne assegnate")
        self.initUI()
        
    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        qlayout = QFormLayout()
        hlayout1.addWidget(self.get_generic_button("Lista Consegne\n Standard", self.go_consegneStandard, self.gestoreConsegne))
        hlayout1.addWidget(self.get_generic_button("Consegne Positive", self.go_consegnePositive, self.gestoreConsegne))
        hlayout1.addWidget(self.get_generic_button("Consegne Rimandate", self.go_consegneRimandate, self.gestoreConsegne))
        hlayout2.addWidget(self.get_generic_button("Lista Colli\n da consegnare", self.go_colliConsegna, self.gestoreConsegne))
        hlayout2.addWidget(self.get_generic_button("Colli positivi", self.go_colliPositivi, self.gestoreConsegne))
        hlayout2.addWidget(self.get_generic_button("Colli Rimandati", self.go_colliRimandati, self.gestoreConsegne))
        qlayout.addWidget(self.get_generic_button_2("Indietro", self.go_back))
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)
        vlayout.addLayout(qlayout)
        self.setLayout(vlayout)
        
    def get_generic_button(self, titolo, on_click, argument):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(lambda : on_click(argument))
        return button
    
    def get_generic_button_2(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(lambda : on_click())
        return button
    
    def go_consegneStandard(self, gestoreConsegne):
        self.consegne_standard = VistaConsegneStandard(gestoreConsegne)
        self.consegne_standard.show()
        
    def go_colliConsegna(self):
        pass
    
    def go_consegnePositive(self):
        pass
    
    def go_colliPositivi(self):
        pass
    
    def go_consegneRimandate(self):
        pass
    
    def go_colliRimandati(self):
        pass
    
    def go_back(self):
        self.close()