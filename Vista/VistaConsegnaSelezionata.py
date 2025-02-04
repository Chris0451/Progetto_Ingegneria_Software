from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QFormLayout, QHBoxLayout, QVBoxLayout

class VistaConsegnaSelezionata(QWidget):
    def __init__(self, gestoreConsegna, consegna_selezionata, contatore):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.consegna_selezionata = consegna_selezionata
        self.contatore = contatore
        self.setWindowTitle(f"Opzioni Consegna {self.contatore}")
        self.setFixedSize(400,250)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.get_generic_button(f"Consegna pacco {self.contatore}", self.effettua_consegna, gestoreConsegna, consegna_selezionata))
        vlayout.addWidget(self.get_generic_button(f"Rimanda consegna {self.contatore}", self.rimanda_consegna, gestoreConsegna, consegna_selezionata))
        vlayout.addWidget(self.get_generic_button(f"Modifica orario consegna {self.contatore}", self.modifica_orario_consegna, gestoreConsegna, consegna_selezionata))
        self.setLayout(vlayout)
        
    def get_generic_button(self, titolo, on_click, argument1, argument2):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        button.clicked.connect(lambda : on_click(argument1, argument2))
        return button
    
    def effettua_consegna(self, gestoreConsegna, consegna_selezionata):
        pass
    
    def rimanda_consegna(self, gestoreConsegna, consegna_selezionata):
        pass
    
    def modifica_orario_consegna(self, gestoreConsegna, consegna_selezionata):
        pass