from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QMessageBox
from Vista.VisteRitiro.VistaInfoRitiro import VistaInfoRitiro

class VistaRitiriPositivi(QWidget):
    def __init__(self, gestoreRitiro):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.resize(600, 250)
        self.setWindowTitle("Ritiri positivi")
        self.label = QLabel("Ritiri positivi registrati:")
        self.info_ritiro = QPushButton("Visualizza info")
        self.indietro = QPushButton("Indietro")
        self.initUI()
    
    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.listaRitiriPositivi = QListWidget()
        self.label.setStyleSheet("font-size: 15px; font-family: Arial; font-weight:bold;")
        
        i = 0
        for ritiroPositivo in self.gestoreRitiro.listaRitiriPositivi:
            self.listaRitiriPositivi.insertItem(i, f"Ritiro n. {ritiroPositivo.datiRitiro.codiceRitiro}")
            i += 1
        
        self.info_ritiro.setStyleSheet("font-size: 12px; font-family: Arial; font-weight:bold;")
        self.indietro.setStyleSheet("font-size: 12px; font-family: Arial; font-weight:bold;")
        
        self.listaRitiriPositivi.setCurrentItem(None)
        self.info_ritiro.clicked.connect(lambda: self.show_selected_info(self.gestoreRitiro))
        self.indietro.clicked.connect(self.close)
        
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.listaRitiriPositivi)
        hlayout.addWidget(self.info_ritiro)
        hlayout.addWidget(self.indietro)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
    
    def show_selected_info(self, gestoreRitiro):
        try:
            ritiro_selezionato = self.listaRitiriPositivi.currentItem()
            if ritiro_selezionato is not None:
                dati_ritiro_selezionato = ritiro_selezionato.text()
                dati_ritiro = dati_ritiro_selezionato.split(" n. ")
                if len(dati_ritiro) == 2:
                    tipo = dati_ritiro[0]
                    codice = dati_ritiro[1]
                    self.visione_ritiro = VistaInfoRitiro(gestoreRitiro, tipo, codice, "Lista Positiva")
                    self.visione_ritiro.show()
                    self.listaRitiriPositivi.setCurrentRow(-1)
                else:
                    QMessageBox.warning(self, "Errore", "Il formato dell'elemento di ritiro non è valido!")
            else:
                QMessageBox.warning(self, "Errore", "Nessun elemento selezionato!")
        except IndexError:
            print("INDEX ERROR")
            return
