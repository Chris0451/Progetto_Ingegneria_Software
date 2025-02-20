from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QTimeEdit, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import QTime
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo

class VistaModificaOrarioRitiro(QWidget):
    def __init__(self, gestoreRitiro, ritiro_selezionato):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.ritiro_selezionato = ritiro_selezionato
        self.setWindowTitle("Modifica orario ritiro")
        self.setFixedSize(400, 150)

        self.label = QLabel("Seleziona un nuovo orario compatibile: ")
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

        self.conferma.clicked.connect(lambda: self.submit_modifica_orario(self.gestoreRitiro, self.ritiro_selezionato))
        self.indietro.clicked.connect(self.submit_chiusura)

    def verifica_orario(self):
        """ Assicura che l'orario selezionato sia multiplo di 30 minuti """
        orario_selezionato = self.imposta_orario.time()
        minuti = orario_selezionato.minute()
        
        if minuti != 0 and minuti != 30:
            if minuti < 30:
                nuovo_orario = QTime(orario_selezionato.hour(), 0)
            else:
                nuovo_orario = QTime(orario_selezionato.hour(), 30)
            self.imposta_orario.setTime(nuovo_orario)

    def submit_modifica_orario(self, gestoreRitiro, ritiro_selezionato):
        """ Modifica l'orario di ritiro controllando le disponibilità """
        orario_selezionato = self.imposta_orario.time()
        orario_str = orario_selezionato.toString("HH:mm")  # Converte in stringa

        if ritiro_selezionato.datiRitiro.statoRitiro == "Consegnato":
            QMessageBox.warning(self, "Errore", "Il pacco è già stato ritirato!", QMessageBox.Ok)
            return

        # Controllo per Pacco
        if isinstance(ritiro_selezionato, Pacco):
            trovato = False
            orario_minimo = QTime.fromString("08:00", "HH:mm")
            orario_massimo = QTime.fromString("19:00", "HH:mm")

            for ritiro in self.gestoreRitiro.listaRitiriLettura:
                if ritiro == ritiro_selezionato:
                    continue
                if ritiro.datiRitiro.oraRitiro == orario_str:  # Confronto con stringa
                    trovato = True
                    break

            if not trovato:
                if orario_minimo <= orario_selezionato <= orario_massimo:
                    if gestoreRitiro.modificaOrarioRitiro(ritiro_selezionato, orario_str):
                        QMessageBox.information(self, "Successo", "Orario modificato con successo!", QMessageBox.Ok)
                        self.close()
                else:
                    QMessageBox.warning(self, "Errore", "Orario non valido!", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Errore", "Orario già impostato per un altro ritiro!", QMessageBox.Ok)

        # Controllo per Collo
        elif isinstance(ritiro_selezionato, Collo):
            trovato = False
            orario_minimo = QTime.fromString(ritiro_selezionato.aziendaMittente.orarioApertura, "HH:mm")
            orario_massimo = QTime.fromString(ritiro_selezionato.aziendaMittente.orarioChiusura, "HH:mm")

            for ritiro in self.gestoreRitiro.listaColliRitiriLettura:
                if ritiro.datiRitiro.oraRitiro == orario_str:
                    trovato = True
                    break

            if not trovato:
                if orario_minimo <= orario_selezionato <= orario_massimo:
                    if gestoreRitiro.modificaOrarioRitiro(ritiro_selezionato, orario_str):
                        QMessageBox.information(self, "Successo", "Orario modificato con successo!", QMessageBox.Ok)
                        self.close()
                else:
                    QMessageBox.warning(self, "Errore", "Orario non valido!", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Errore", "Orario già impostato per un altro ritiro!", QMessageBox.Ok)

    def submit_chiusura(self):
        self.close()