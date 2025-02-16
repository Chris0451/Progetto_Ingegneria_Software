from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QTimeEdit, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import QTime
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo
from datetime import datetime

class VistaModificaOrarioConsegna(QWidget):
    def __init__(self, gestoreConsegna, consegna_selezionata):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.consegna_selezionata = consegna_selezionata
        self.setWindowTitle("Modifica orario consegna")
        self.setFixedSize(400,150)
        self.label = QLabel("Seleziona un nuovo orario compatibile (non deve superare le 19:00):")
        self.imposta_orario = QTimeEdit(self)
        self.imposta_orario.editingFinished.connect(self.verifica_orario)
        self.conferma = QPushButton("Conferma nuovo orario")
        self.indietro = QPushButton("Indietro")
        self.imposta_orario.setTime(QTime.currentTime())
        self.initUI()
        
    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.label.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.imposta_orario)
        hlayout.addWidget(self.conferma)
        hlayout.addWidget(self.indietro)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
        self.conferma.clicked.connect(lambda : self.submit_modifica_orario(self.gestoreConsegna, self.consegna_selezionata))
        self.indietro.clicked.connect(self.submit_chiusura)
    
    def verifica_orario(self):
        orario_selezionato = self.imposta_orario.time()
        minuti = orario_selezionato.minute()
        if minuti != 0 and minuti != 30:
           if minuti < 30:
               nuovo_orario = QTime(orario_selezionato.hour(), 0)
           else:
               nuovo_orario = QTime(orario_selezionato.hour(), 30)
           self.imposta_orario.setTime(nuovo_orario)
    
    def submit_modifica_orario(self, gestoreConsegna, consegna_selezionata):
        orario_selezionato = self.imposta_orario.time()
        if consegna_selezionata.datiConsegna.statoConsegna != "Consegnato" and consegna_selezionata.datiConsegna.statoConsegna != "Consegna rimandata":
            if isinstance(consegna_selezionata, Pacco):
                trovato=False
                orario_minimo = datetime.strptime("08:00", "%H:%M").time()
                orario_massimo = datetime.strptime("19:00", "%H:%M").time()
                for consegna in self.gestoreConsegna.listaConsegne:
                    if consegna == consegna_selezionata:
                        continue
                    if consegna.datiConsegna.oraConsegna == consegna_selezionata.datiConsegna.oraConsegna:
                        trovato=True
                if trovato==False:
                    if orario_minimo <= orario_selezionato <= orario_massimo:
                        if self.gestoreConsegna.modificaOrarioConsegna(consegna_selezionata, orario_selezionato):
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Orario modificato con successo")
                            msg.setWindowTitle("Successo")
                            msg.setStandardButtons(QMessageBox.Ok)
                            self.close()
                    else:
                        QMessageBox.warning(self, "Avviso", "Orario non valido",QMessageBox.Ok)
                else:
                    QMessageBox.warning(self, "Avviso", "Orario già impostato per un'altra consegna", QMessageBox.Ok) 
            elif isinstance(consegna_selezionata, Collo):
                trovato=False
                orario_minimo = datetime.strptime(consegna_selezionata.aziendaDestinatario.orarioApertura, "%H:%M").time()
                orario_massimo = datetime.strptime(consegna_selezionata.aziendaDestinatario.orarioChiusura, "%H:%M").time()
                for consegna in self.gestoreConsegna.listaColliConsegne:
                    if consegna.datiConsegna.oraConsegna == consegna_selezionata.datiConsegna.oraConsegna:
                        trovato=True
                if trovato==False:
                    if orario_minimo <= orario_selezionato <= orario_massimo:
                        if self.gestoreConsegna.modificaOrarioConsegna(consegna_selezionata, orario_selezionato):
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Orario modificato con successo")
                            msg.setWindowTitle("Successo")
                            msg.setStandardButtons(QMessageBox.Ok)
                            self.close()
                    else:
                        QMessageBox.warning(self, "Avviso", "Orario non valido",QMessageBox.Ok)
                else:
                    QMessageBox.warning(self, "Avviso", "Orario già impostato per un'altra consegna", QMessageBox.Ok) 
        else:
            QMessageBox.warning(self, "Avviso","Pacco già consegnato o rimandato in precendenza", QMessageBox.Ok)
            self.close()
        
    def submit_chiusura(self):
        self.close()