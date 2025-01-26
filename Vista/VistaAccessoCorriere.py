from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

class VistaAccessoCorriere(QWidget):
    
    def __init__(self, parent=None):
        super(VistaAccessoCorriere, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Presa in Carico Pacco", self.go_presaInCarico), 0, 0,)
        grid_layout.addWidget(self.get_generic_button("Visualizza lista consegne", self.go_listaConsegne), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Visualizza lista ritiri", self.go_listaRitiri), 2, 0)
        grid_layout.addWidget(self.get_generic_button("Deposita pacchi", self.go_deposito), 3,0)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Profilo Corriere")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_presaInCarico(self):
        pass

    def go_listaConsegne(self):
        pass

    def go_listaRitiri(self):
        pass

    def go_deposito(self):
        pass