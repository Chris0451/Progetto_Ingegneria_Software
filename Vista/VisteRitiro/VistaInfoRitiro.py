from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class VistaInfoRitiro(QWidget):
    def __init__(self, gestoreRitiro, tipo, codice):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.tipo = tipo
        self.codice = codice
        self.initUI()
    
    def initUI(self):
        self.resize(500, 250)
        self.setWindowTitle(f"{self.tipo} n. {self.codice}")
        vlayout = QVBoxLayout()
        if self.tipo == "Ritiro":
            if self.gestoreRitiro.ricercaRitiroByCodice(self.codice):
                ritiro_selezionato = self.gestoreRitiro.getRitiroLetturaByCodice(self.codice)
                info_ritiro = QLabel(ritiro_selezionato.getInfoPacco())
                vlayout.addWidget(info_ritiro)
                self.setLayout(vlayout)
        elif self.tipo == "Collo":
            if self.gestoreRitiro.ricercaColloByCodice(self.codice):
                collo_selezionato = self.gestoreRitiro.getColloByCodice(self.codice)
                info_collo = QLabel(collo_selezionato.getInfoCollo())
                vlayout.addWidget(info_collo)
                self.setLayout(vlayout)