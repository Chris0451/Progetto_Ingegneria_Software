from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QTimeEdit, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import QTime
from datetime import datetime
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo

class VistaModificaOrarioRitiro(QWidget):
    def __init__(self, gestoreRitiro, ritiro_selezionato):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.ritiro_selezionato = ritiro_selezionato

        if ritiro_selezionato.datiRitiro.statoRitiro != "Ritiro rimandato" and ritiro_selezionato.datiRitiro.statoRitiro != "Ritirato":
            self.setWindowTitle("Modifica orario ritiro")
            self.setFixedSize(500, 150)
            self.label = QLabel("Seleziona un nuovo orario compatibile:")
            
            if isinstance(ritiro_selezionato, Collo):
                self.orario_apertura = QLabel(
                    f"Orario aziendale: {ritiro_selezionato.aziendaMittente.orarioApertura} - "
                    f"{ritiro_selezionato.aziendaMittente.orarioChiusura}\n"
                    f"Orario attuale: {ritiro_selezionato.datiRitiro.oraRitiro}"
                )
            else:
                self.orario_apertura = QLabel("Intervallo valido: 08:00 - 19:00\n"
                                            f"Orario attuale: {ritiro_selezionato.datiRitiro.oraRitiro}")
            
            self.imposta_orario = QTimeEdit(self)
            self.imposta_orario.setDisplayFormat("HH:mm")
            self.imposta_orario.editingFinished.connect(self.verifica_orario)
            self.conferma = QPushButton("Conferma")
            self.indietro = QPushButton("Indietro")
            self.imposta_orario.setTime(QTime.currentTime())
            self.initUI()
        else:
            vlayout = QVBoxLayout()
            self.setWindowTitle("Modifica orario ritiro")
            self.setFixedSize(400, 80)
            self.label = QLabel("Impossibile modificare l'orario: ritiro non disponibile")
            self.indietro = QPushButton("Indietro")
            self.indietro.clicked.connect(self.close)
            vlayout.addWidget(self.label)
            vlayout.addWidget(self.indietro)
            self.setLayout(vlayout)

    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.orario_apertura)
        vlayout.addWidget(self.imposta_orario)
        hlayout.addWidget(self.conferma)
        hlayout.addWidget(self.indietro)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
        self.conferma.clicked.connect(lambda: self.submit_modifica_orario(self.ritiro_selezionato))
        self.indietro.clicked.connect(self.close)

    def verifica_orario(self):
        orario_selezionato = self.imposta_orario.time()
        minuti = orario_selezionato.minute()
        if minuti not in [0, 30]:
            nuovo_orario = QTime(orario_selezionato.hour(), 0 if minuti < 30 else 30)
            self.imposta_orario.setTime(nuovo_orario)

    def submit_modifica_orario(self, ritiro_selezionato):
        orario_selezionato = self.imposta_orario.time()
        orario_ritiro = datetime.strptime(ritiro_selezionato.datiRitiro.oraRitiro, "%H:%M").time()
        if isinstance(ritiro_selezionato, Pacco):
            trovato=False
            orario_minimo = datetime.strptime("08:00", "%H:%M").time()
            orario_massimo = datetime.strptime("19:00", "%H:%M").time()
            for ritiro in self.gestoreRitiro.listaRitiriLettura:
                if ritiro == ritiro_selezionato:
                    continue
                if ritiro.datiRitiro.oraRitiro == ritiro_selezionato.datiRitiro.oraRitiro:
                    trovato=True
            if trovato==False:
                if orario_minimo <= orario_selezionato <= orario_massimo and orario_selezionato >= orario_ritiro:
                    if self.gestoreRitiro.modificaOrarioRitiro(ritiro_selezionato, orario_selezionato.toString("HH:mm")):
                        QMessageBox.information(self, "Successo", "Orario modificato con successo", QMessageBox.Ok)
                        self.close()
                else:
                        QMessageBox.warning(self, "Avviso", "Orario non valido",QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Avviso", "Orario già impostato per un altro ritiro", QMessageBox.Ok) 
        elif isinstance(ritiro_selezionato, Collo):
            trovato=False
            orario_minimo = datetime.strptime(ritiro_selezionato.aziendaMittente.orarioApertura, "%H:%M").time()
            orario_massimo = datetime.strptime(ritiro_selezionato.aziendaMittente.orarioChiusura, "%H:%M").time()
            for ritiro in self.gestoreRitiro.listaColliRitiriLettura:
                if ritiro == ritiro_selezionato:
                    continue
                if ritiro.datiRitiro.oraRitiro == ritiro_selezionato.datiRitiro.oraRitiro:
                    trovato=True
            if trovato==False:
                if orario_minimo <= orario_selezionato <= orario_massimo and orario_selezionato >= orario_ritiro:
                    if self.gestoreRitiro.modificaOrarioRitiro(ritiro_selezionato, orario_selezionato.toString("HH:mm")):
                        QMessageBox.information(self, "Successo", "Orario modificato con successo", QMessageBox.Ok)
                        self.close()
                else:
                    QMessageBox.warning(self, "Avviso", "Orario non valido",QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Avviso", "Orario già impostato per un altro  ritiro", QMessageBox.Ok)     
        