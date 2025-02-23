from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class VistaInfoConsegna(QWidget):
    def __init__(self, gestoreConsegna, tipo, codice):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.tipo = tipo
        self.codice = codice
        self.initUI()
    
    def initUI(self):
        self.resize(500, 250)
        self.setWindowTitle(f"{self.tipo} n. {self.codice}")
        vlayout = QVBoxLayout()
        if self.tipo == "Consegna":
            if self.gestoreConsegna.ricercaConsegnaLetturaByCodice(self.codice):
                consegna_selezionata = self.gestoreConsegna.getConsegnaLetturaByCodice(self.codice)
                info_consegna = QLabel(consegna_selezionata.getInfoPaccoConsegna())
                vlayout.addWidget(info_consegna)
        elif self.tipo == "Collo":
            if self.gestoreConsegna.ricercaColloLetturaByCodice(self.codice):
                collo_selezionato = self.gestoreConsegna.getColloLetturaByCodice(self.codice)
                info_collo = QLabel(collo_selezionato.getInfoColloConsegna())
                vlayout.addWidget(info_collo)
        self.setLayout(vlayout)