from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

def VistaAccessoCorriere(QWidget):
    def __init__(self):
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Presa in Carico Pacco", self.go_presaInCarico), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Visualizza lista consegne", self.go_listaConsegne), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Visualizza lista consegne", self.go_listaRitiri), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Deposita pacchi", self.go_deposito), 1, 1)
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