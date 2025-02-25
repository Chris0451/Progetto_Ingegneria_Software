from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class VistaInfoRitiro(QWidget):
    def __init__(self, gestoreRitiro, tipo, codice, tipoLista):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.tipo = tipo
        self.codice = codice
        self.tipoLista = tipoLista
        self.initUI()
    
    def initUI(self):
        self.resize(500, 250)
        self.setWindowTitle(f"{self.tipo} n. {self.codice}")
        vlayout = QVBoxLayout()
        if self.tipo == "Ritiro" and self.tipoLista=="Lista Negativa":
            ritiro_selezionato = self.gestoreRitiro.getRitiroNegativoByCodice(self.codice)
            info_ritiro = QLabel(ritiro_selezionato.getInfoPaccoRitiro())
            vlayout.addWidget(info_ritiro)
        elif self.tipo == "Collo" and self.tipoLista == "Lista Positiva":
            ritiro_selezionato = self.gestoreRitiro.getColloPositivoByCodice(self.codice)
            info_ritiro = QLabel(ritiro_selezionato.getInfoColloRitiro())
            vlayout.addWidget(info_ritiro)
        elif self.tipo == "Ritiro" and self.tipoLista == "Lista Positiva":
            ritiro_selezionato = self.gestoreRitiro.getRitiroPositivoByCodice(self.codice)
            info_ritiro = QLabel(ritiro_selezionato.getInfoPaccoRitiro())
            vlayout.addWidget(info_ritiro)
        elif self.tipo == "Collo" and self.tipoLista == "Lista Negativa":
            ritiro_selezionato = self.gestoreRitiro.getRitiroPositivoByCodice(self.codice)
            info_ritiro = QLabel(ritiro_selezionato.getInfoPaccoRitiro())
            vlayout.addWidget(info_ritiro)
        self.setLayout(vlayout)