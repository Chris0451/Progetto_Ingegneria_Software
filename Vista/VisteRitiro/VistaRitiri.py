from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QFormLayout, QHBoxLayout, QVBoxLayout
from Vista.VisteRitiro.VistaRitiriStandard import VistaRitiriStandard
from Vista.VisteRitiro.VistaRitiriAziendaliPositivi import VistaRitiriAziendaliPositivi
from Vista.VisteRitiro.VistaRitiriAziendaliNegativi import VistaRitiriAziendaliNegativi
from Vista.VisteRitiro.VistaRitiriAziendali import VistaRitiriAziendali
from Vista.VisteRitiro.VistaRitiriPositivi import VistaRitiriPositivi

from Vista.VisteRitiro.VistaRitiriRimandati import VistaRitiriRimandati


class VistaRitiri(QWidget):
    def __init__(self, gestoreRitiro):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.setFixedSize(600, 250)
        self.setWindowTitle("Visualizzazione ritiri assegnati")
        self.initUI()
        
    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        qlayout = QFormLayout()
        hlayout1.addWidget(self.get_generic_button("Lista Ritiri\n Standard", self.go_ritiriStandard, self.gestoreRitiro))
        hlayout1.addWidget(self.get_generic_button("Ritiri\n Positivi", self.go_ritiriPositivi, self.gestoreRitiro))
        hlayout1.addWidget(self.get_generic_button("Ritiri\n Negativi", self.go_ritiriNegativi, self.gestoreRitiro))
        hlayout2.addWidget(self.get_generic_button("Lista Ritiri\n Aziendali (Colli)", self.go_listaRitiriAziendali, self.gestoreRitiro))
        hlayout2.addWidget(self.get_generic_button("Colli\n Ritirati", self.go_colliRitirati, self.gestoreRitiro))
        hlayout2.addWidget(self.get_generic_button("Colli\n Non Ritirati", self.go_colliNonRitirati, self.gestoreRitiro))
        qlayout.addWidget(self.get_generic_button_2("Indietro", self.go_back))
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)
        vlayout.addLayout(qlayout)
        self.setLayout(vlayout)
        
    def get_generic_button(self, titolo, on_click, argument):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(lambda: on_click(argument))
        return button
    
    def get_generic_button_2(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(lambda : on_click())
        return button
    
    def go_ritiriStandard(self, gestoreRitiro):
        self.ritiri_standard = VistaRitiriStandard(gestoreRitiro)
        self.ritiri_standard.show()
        
    def go_ritiriPositivi(self, gestoreRitiro):
        self.ritiri_positivi = VistaRitiriPositivi(gestoreRitiro)
        self.ritiri_positivi.show()
    
    def go_ritiriNegativi(self, gestoreRitiro):
        self.ritiri_negativi = VistaRitiriRimandati(gestoreRitiro)
        self.ritiri_negativi.show()
    
    def go_listaRitiriAziendali(self, gestoreRitiro):
        self.ritiri_aziendali = VistaRitiriAziendali(gestoreRitiro)
        self.ritiri_aziendali.show()
    
    def go_colliRitirati(self, gestoreRitiro):
        self.colli_ritiri_positivi = VistaRitiriAziendaliPositivi(gestoreRitiro)
        self.colli_ritiri_positivi.show()
    
    def go_colliNonRitirati(self, gestoreRitiro):
        self.colli_ritiri_negativi = VistaRitiriAziendaliNegativi(gestoreRitiro)
        self.colli_ritiri_negativi.show()
        
    def go_back(self):
        self.close()