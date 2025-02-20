from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QMessageBox
from Vista.VisteConsegna.VistaInfoConsegna import VistaInfoConsegna

class VistaColliPositivi(QWidget):
    def __init__(self, gestoreConsegna):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.resize(600, 250)
        self.setWindowTitle("Colli positivi")
        self.label = QLabel("Colli da consegnare assegnati:")
        self.info_consegna = QPushButton("Visualizza info")
        self.indietro = QPushButton("Indietro")
        self.initUI()
    
    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.listaColliPositivi = QListWidget()
        self.label.setStyleSheet("font-size: 15px; font-family: Arial; font-weight:bold;")
        j=0
        for colloAssegnato in self.gestoreConsegna.listaColliPositivi:
            self.listaColliPositivi.insertItem(j, f"Collo n. {colloAssegnato.datiConsegna.codiceConsegna}") 
            j+=1
        self.info_consegna.setStyleSheet("font-size: 12px; font-family: Arial; font-weight:bold;")
        self.indietro.setStyleSheet("font-size: 12px; font-family: Arial; font-weight:bold;")
        self.listaColliPositivi.setCurrentItem(None)
        self.info_consegna.clicked.connect(lambda : self.show_selected_info(self.gestoreConsegna))
        self.indietro.clicked.connect(self.submit_chiusura)
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.listaColliPositivi)
        hlayout.addWidget(self.info_consegna)
        hlayout.addWidget(self.indietro)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
    
    def show_selected_info(self, gestoreConsegna):
        # pass
        try:
            collo_selezionato = self.listaColliPositivi.currentItem()
            if collo_selezionato is not None:
                dati_collo_selezionato = collo_selezionato.text()
                dati_collo = dati_collo_selezionato.split(" n. ")
                if len(dati_collo) == 2:  # Controllo se la divisione è valida
                    tipo = dati_collo[0]
                    codice = dati_collo[1]
                    self.visione_consegna = VistaInfoConsegna(gestoreConsegna, tipo, codice)
                    self.visione_consegna.show()
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