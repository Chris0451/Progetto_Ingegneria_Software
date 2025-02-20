from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QMessageBox
from Vista.VisteConsegna.VistaInfoConsegna import VistaInfoConsegna

class VistaConsegneAssegnate(QWidget):
    def __init__(self, gestoreConsegna):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.resize(600, 250)
        self.setWindowTitle("Consegne assegnate")
        self.label1 = QLabel("Consegne standard assegnate:")
        self.label2 = QLabel("Colli da consegnare assegnati:")
        self.info_consegna = QPushButton("Visualizza info")
        self.indietro = QPushButton("Indietro")
        self.initUI()
    
    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.listaConsegneAssegnate = QListWidget()
        self.listaColliAssegnati = QListWidget()
        self.label1.setStyleSheet("font-size: 15px; font-family: Arial; font-weight:bold;")
        i = 0
        for consegnaAssegnata in self.gestoreConsegna.listaConsegneLettura:
            self.listaConsegneAssegnate.insertItem(i, f"Consegna n. {consegnaAssegnata.datiConsegna.codiceConsegna}")
            i+=1
        self.label2.setStyleSheet("font-size: 15px; font-family: Arial; font-weight:bold;")
        j=0
        for colloAssegnato in self.gestoreConsegna.listaColliConsegneLettura:
            self.listaColliAssegnati.insertItem(j, f"Collo n. {colloAssegnato.datiConsegna.codiceConsegna}") 
            j+=1
        self.info_consegna.setStyleSheet("font-size: 12px; font-family: Arial; font-weight:bold;")
        self.indietro.setStyleSheet("font-size: 12px; font-family: Arial; font-weight:bold;")
        self.listaConsegneAssegnate.setCurrentItem(None)
        self.listaColliAssegnati.setCurrentItem(None)
        self.listaConsegneAssegnate.clearSelection()
        self.listaColliAssegnati.clearSelection()
        self.info_consegna.clicked.connect(lambda : self.show_selected_info(self.gestoreConsegna))
        self.indietro.clicked.connect(self.submit_chiusura)
        vlayout.addWidget(self.label1)
        vlayout.addWidget(self.listaConsegneAssegnate)
        vlayout.addWidget(self.label2)
        vlayout.addWidget(self.listaColliAssegnati)
        hlayout.addWidget(self.info_consegna)
        hlayout.addWidget(self.indietro)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
    
    def show_selected_info(self, gestoreConsegna):
        # pass
        try:
            collo_selezionato = self.listaColliAssegnati.currentItem()
            consegna_selezionata = self.listaConsegneAssegnate.currentItem()
            if consegna_selezionata is not None:
                # Selezionato un elemento da listaConsegneAssegnate
                dati_consegna_selezionata = consegna_selezionata.text()
                dati_cns = dati_consegna_selezionata.split(" n. ")
                if len(dati_cns) == 2:  # Controllo se la divisione è valida
                    tipo = dati_cns[0]
                    codice = dati_cns[1]
                    self.visione_consegna = VistaInfoConsegna(gestoreConsegna, tipo, codice)
                    self.visione_consegna.show()
                    self.listaConsegneAssegnate.setCurrentRow(-1)
                else:
                    # Se la divisione non è valida, avvisa l'utente
                    QMessageBox.warning(self, "Errore", "Il formato dell'elemento di consegna non è valido!")
            elif collo_selezionato is not None:
                # Selezionato un elemento da listaColliAssegnati
                dati_collo_selezionato = collo_selezionato.text()
                dati_collo = dati_collo_selezionato.split(" n. ")
                if len(dati_collo) == 2:  # Controllo se la divisione è valida
                    tipo = dati_collo[0]
                    codice = dati_collo[1]
                    self.visione_consegna = VistaInfoConsegna(gestoreConsegna, tipo, codice)
                    self.visione_consegna.show()
                    self.listaColliAssegnati.setCurrentRow(-1)
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