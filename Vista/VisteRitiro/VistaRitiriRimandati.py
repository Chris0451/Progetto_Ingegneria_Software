from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QMessageBox
from Vista.VisteRitiro.VistaInfoRitiro import VistaInfoRitiro

class VistaRitiriRimandati(QWidget):
    def __init__(self, gestoreRitiro):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.resize(600, 250)
        self.setWindowTitle("Ritiri rimandati")
        self.label = QLabel("Ritiri standard rimandati:")
        self.info_ritiro = QPushButton("Visualizza info")
        self.indietro = QPushButton("Indietro")
        self.initUI()
    
    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.listaRitiriNegativi = QListWidget()
        self.label.setStyleSheet("font-size: 15px; font-family: Arial; font-weight:bold;")
        i = 0
        for ritiroAssegnato in self.gestoreRitiro.listaRitiriNegativi:
            self.listaRitiriNegativi.insertItem(i, f"Ritiro n. {ritiroAssegnato.datiRitiro.codiceRitiro}")
            i+=1
        self.info_ritiro.setStyleSheet("font-size: 12px; font-family: Arial; font-weight:bold;")
        self.indietro.setStyleSheet("font-size: 12px; font-family: Arial; font-weight:bold;")
        self.listaRitiriNegativi.setCurrentItem(None)
        self.info_ritiro.clicked.connect(lambda : self.show_selected_info(self.gestoreRitiro))
        self.indietro.clicked.connect(self.submit_chiusura)
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.listaRitiriNegativi)
        hlayout.addWidget(self.info_ritiro)
        hlayout.addWidget(self.indietro)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
    
    def show_selected_info(self, gestoreRitiro):
        # pass
        try:
            ritiro_selezionato = self.listaRitiriNegativi.currentItem()
            if ritiro_selezionato is not None:
                # Selezionato un elemento da listaConsegnePositive
                dati_ritiro_selezionato = ritiro_selezionato.text()
                dati_cns = dati_ritiro_selezionato.split(" n. ")
                if len(dati_cns) == 2:  # Controllo se la divisione è valida
                    tipo = dati_cns[0]
                    codice = dati_cns[1]
                    self.visione_ritiro = VistaInfoRitiro(gestoreRitiro, tipo, codice, "Lista Negativa")
                    self.visione_ritiro.show()
                    self.listaRitiriNegativi.setCurrentRow(-1)
                else:
                    # Se la divisione non è valida, avvisa l'utente
                    QMessageBox.warning(self, "Errore", "Il formato dell'elemento di ritiro non è valido!")
            else:
                QMessageBox.warning(self, "Errore", "Nessun elemento selezionato!")
        except IndexError:
            print("INDEX ERROR")
            return
    
    def submit_chiusura(self):
        self.close()