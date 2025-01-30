from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QMainWindow

from Vista.VistaPresaInCarico import VistaPresaInCarico

class VistaAccessoCorriere(QWidget):
    
    def __init__(self, parent=None):
        super(VistaAccessoCorriere, self).__init__(parent)
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        vlayout.addWidget(self.get_generic_button("Presa in Carico Pacco", self.go_presaInCarico))
        hlayout.addWidget(self.get_generic_button("Visualizza lista consegne", self.go_listaConsegne))
        hlayout.addWidget(self.get_generic_button("Visualizza lista ritiri", self.go_listaRitiri))
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.get_generic_button("Deposita pacchi", self.go_deposito))
        self.setLayout(vlayout)
        self.resize(400, 300)
        self.setWindowTitle("Profilo Corriere")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_presaInCarico(self):
        self.presa_in_carico = VistaPresaInCarico()
        self.presa_in_carico.show()

    def go_listaConsegne(self):
        pass

    def go_listaRitiri(self):
        pass

    def go_deposito(self):
        pass