class VistaColliConsegneNegative():
    pass

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QMessageBox
from Vista.VistaInfoConsegna import VistaInfoConsegna

class VistaColliConsegneNegative(QWidget):
    def __init__(self, gestoreConsegna):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.resize(600, 250)
        self.setWindowTitle("Consegne di Colli rimandati")
        self.label = QLabel("Colli rimandate:")
        self.info_consegna = QPushButton("Visualizza info")
        self.indietro = QPushButton("Indietro")
        self.initUI()
    
    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.listaConsegneNegative = QListWidget()
        self.label.setStyleSheet("font-size: 15px; font-family: Arial; font-weight:bold;")
        i = 0
        for consegnaNegativa in self.gestoreConsegna.listaColliNegativi:
            self.listaConsegneNegative.insertItem(i, f"Collo n. {consegnaNegativa.datiConsegna.codiceConsegna}")
            i+=1
        self.info_consegna.setStyleSheet("font-size: 12px; font-family: Arial; font-weight:bold;")
        self.indietro.setStyleSheet("font-size: 12px; font-family: Arial; font-weight:bold;")
        self.listaConsegneNegative.setCurrentItem(None)
        self.info_consegna.clicked.connect(lambda : self.show_selected_info(self.gestoreConsegna))
        self.indietro.clicked.connect(self.submit_chiusura)
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.listaConsegneNegative)
        hlayout.addWidget(self.info_consegna)
        hlayout.addWidget(self.indietro)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
    
    def show_selected_info(self, gestoreConsegna):
        # pass
        try:
            consegna_selezionata = self.listaConsegneNegative.currentItem()
            if consegna_selezionata is not None:
                # Selezionato un elemento da listaConsegnePositive
                dati_consegna_selezionata = consegna_selezionata.text()
                dati_cns = dati_consegna_selezionata.split(" n. ")
                if len(dati_cns) == 2:  # Controllo se la divisione è valida
                    tipo = dati_cns[0]
                    codice = dati_cns[1]
                    self.visione_consegna = VistaInfoConsegna(gestoreConsegna, tipo, codice)
                    self.visione_consegna.show()
                    self.listaConsegneNegative.setCurrentRow(-1)
                else:
                    # Se la divisione non è valida, avvisa l'utente
                    QMessageBox.warning(self, "Errore", "Il formato dell'elemento di consegna non è valido!")
            else:
                QMessageBox.warning(self, "Errore", "Nessun elemento selezionato!")
        except IndexError:
            print("INDEX ERROR")
            return
    
    def submit_chiusura(self):
        self.close()