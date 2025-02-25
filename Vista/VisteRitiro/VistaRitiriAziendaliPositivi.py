from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QMessageBox
from Vista.VisteRitiro.VistaInfoRitiro import VistaInfoRitiro

class VistaRitiriAziendaliPositivi(QWidget):
    def __init__(self, gestoreRitiro):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.resize(600, 250)
        self.setWindowTitle("Colli positivi")
        self.label = QLabel("Colli da ritirare positivi:")
        self.info_ritiro = QPushButton("Visualizza info")
        self.indietro = QPushButton("Indietro")
        self.initUI()
    
    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.listaColliPositivi = QListWidget()
        self.label.setStyleSheet("font-size: 15px; font-family: Arial; font-weight:bold;")
        j=0
        for colloAssegnato in self.gestoreRitiro.listaColliPositivi:
            self.listaColliPositivi.insertItem(j, f"Collo n. {colloAssegnato.datiRitiro.codiceRitiro}") 
            j+=1
        self.info_ritiro.setStyleSheet("font-size: 12px; font-family: Arial; font-weight:bold;")
        self.indietro.setStyleSheet("font-size: 12px; font-family: Arial; font-weight:bold;")
        self.listaColliPositivi.setCurrentItem(None)
        self.info_ritiro.clicked.connect(lambda : self.show_selected_info(self.gestoreRitiro))
        self.indietro.clicked.connect(self.submit_chiusura)
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.listaColliPositivi)
        hlayout.addWidget(self.info_ritiro)
        hlayout.addWidget(self.indietro)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
    
    def show_selected_info(self, gestoreRitiro):
        # pass
        try:
            collo_selezionato = self.listaColliPositivi.currentItem()
            if collo_selezionato is not None:
                dati_collo_selezionato = collo_selezionato.text()
                dati_collo = dati_collo_selezionato.split(" n. ")
                if len(dati_collo) == 2:  # Controllo se la divisione è valida
                    tipo = dati_collo[0]
                    codice = dati_collo[1]
                    self.visione_ritiro = VistaInfoRitiro(gestoreRitiro, tipo, codice, "Lista Positiva")
                    self.visione_ritiro.show()
                    self.listaColliPositivi.setCurrentRow(-1)
                else:
                    # Se la divisione non è valida, avvisa l'utente
                    QMessageBox.warning(self, "Errore", "Il formato dell'elemento di collo non è valido!")
            else:
                QMessageBox.warning(self, "Errore", "Nessun elemento selezionato!")
        except IndexError:
            print("INDEX ERROR")
            return
    
    def submit_chiusura(self):
        self.close()