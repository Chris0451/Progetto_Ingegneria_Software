from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMessageBox, QTableWidget, QHeaderView,QTableWidgetItem
from PyQt5.QtCore import Qt
from Gestione.GestoreBackup import GestoreBackup
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo

class VistaDepositoPacchi(QWidget):
    def __init__(self, gestoreConsegna, gestoreRitiro):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.gestoreRitiro = gestoreRitiro
        self.gestoreBackup = GestoreBackup(self.gestoreConsegna, self.gestoreRitiro)

        self.setWindowTitle("Deposito Pacchi")
        self.resize(700,550)
        self.layout = QVBoxLayout()

        # Tabella per visualizzare i pacchi
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(8)  # Numero di colonne (adattato)
        self.table_widget.setHorizontalHeaderLabels(["Codice", "Peso", "Volume", "Tipo", "Metodo Pagamento", "Mittente", "Destinatario", "Stato"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table_widget)

        # Popola la tabella
        self.popola_tabella()

        # Pulsanti
        button_layout = QHBoxLayout()
        conferma_button = QPushButton("Conferma Deposito")
        conferma_button.clicked.connect(self.conferma_deposito)
        button_layout.addWidget(conferma_button)

        indietro_button = QPushButton("Indietro")
        indietro_button.clicked.connect(self.close)
        button_layout.addWidget(indietro_button)

        self.layout.addLayout(button_layout)
        self.setLayout(self.layout)

    def popola_tabella(self):
        for ritiro_standard in self.gestoreRitiro.listaRitiriPositivi:
            self.aggiungi_riga(ritiro_standard,"Ritiro")
        for ritiro_collo in self.gestoreRitiro.listaColliPositivi:
            self.aggiungi_riga(ritiro_collo,"Ritiro")
        for consegna_standard in self.gestoreConsegna.listaConsegneNegative:
            self.aggiungi_riga(consegna_standard,"Consegna")
        for consegna_colli in self.gestoreConsegna.listaColliNegativi:
            self.aggiungi_riga(consegna_colli,"Consegna")
        

    def aggiungi_riga(self, argument,type):
        if isinstance(argument, Pacco) and type=="Ritiro":
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QTableWidgetItem(argument.datiRitiro.codiceRitiro))
            self.table_widget.setItem(row_position, 1, QTableWidgetItem(str(argument.peso))) #conversione in stringa
            self.table_widget.setItem(row_position, 2, QTableWidgetItem(str(argument.volume))) #conversione in stringa
            self.table_widget.setItem(row_position, 3, QTableWidgetItem(argument.tipo))
            self.table_widget.setItem(row_position, 4, QTableWidgetItem("N/A"))
            self.table_widget.setItem(row_position, 5, QTableWidgetItem(argument.mittente.nome + " " + argument.mittente.cognome)) #nome e cognome del mittente
            self.table_widget.setItem(row_position, 6, QTableWidgetItem(argument.destinatario.nome + " " + argument.destinatario.cognome)) #nome e cognome del destinatario
            self.table_widget.setItem(row_position, 7, QTableWidgetItem(argument.datiRitiro.statoRitiro))
        elif isinstance(argument, Collo) and type=="Ritiro":
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QTableWidgetItem(argument.datiRitiro.codiceRitiro))
            self.table_widget.setItem(row_position, 1, QTableWidgetItem(str(argument.peso))) #conversione in stringa
            self.table_widget.setItem(row_position, 2, QTableWidgetItem(str(argument.volume))) #conversione in stringa
            self.table_widget.setItem(row_position, 3, QTableWidgetItem(argument.naturaCollo))
            self.table_widget.setItem(row_position, 4, QTableWidgetItem("N/A")) #metodo pagamento non presente per i colli
            self.table_widget.setItem(row_position, 5, QTableWidgetItem(argument.aziendaMittente.nomeAzienda)) #nome azienda mittente
            self.table_widget.setItem(row_position, 6, QTableWidgetItem(argument.aziendaDestinatario.nomeAzienda)) #nome azienda destinatario
            self.table_widget.setItem(row_position, 7, QTableWidgetItem(argument.datiRitiro.statoRitiro))
        elif isinstance(argument, Pacco) and type=="Consegna":
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QTableWidgetItem(argument.datiConsegna.codiceConsegna))
            self.table_widget.setItem(row_position, 1, QTableWidgetItem(str(argument.peso))) #conversione in stringa
            self.table_widget.setItem(row_position, 2, QTableWidgetItem(str(argument.volume))) #conversione in stringa
            self.table_widget.setItem(row_position, 3, QTableWidgetItem(argument.tipo))
            self.table_widget.setItem(row_position, 4, QTableWidgetItem(argument.metodoPagamento))
            self.table_widget.setItem(row_position, 5, QTableWidgetItem(argument.mittente.nome + " " + argument.mittente.cognome)) #nome e cognome del mittente
            self.table_widget.setItem(row_position, 6, QTableWidgetItem(argument.destinatario.nome + " " + argument.destinatario.cognome)) #nome e cognome del destinatario
            self.table_widget.setItem(row_position, 7, QTableWidgetItem(argument.datiConsegna.statoConsegna))
        elif isinstance(argument, Collo) and type=="Consegna":
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QTableWidgetItem(argument.datiConsegna.codiceConsegna))
            self.table_widget.setItem(row_position, 1, QTableWidgetItem(str(argument.peso))) #conversione in stringa
            self.table_widget.setItem(row_position, 2, QTableWidgetItem(str(argument.volume))) #conversione in stringa
            self.table_widget.setItem(row_position, 3, QTableWidgetItem(argument.naturaCollo))
            self.table_widget.setItem(row_position, 4, QTableWidgetItem("N/A")) #metodo pagamento non presente per i colli
            self.table_widget.setItem(row_position, 5, QTableWidgetItem(argument.aziendaMittente.nomeAzienda)) #nome azienda mittente
            self.table_widget.setItem(row_position, 6, QTableWidgetItem(argument.aziendaDestinatario.nomeAzienda)) #nome azienda destinatario
            self.table_widget.setItem(row_position, 7, QTableWidgetItem(argument.datiConsegna.statoConsegna))


    def conferma_deposito(self):
        reply = QMessageBox.question(self, "Conferma Deposito", "Sei sicuro di voler confermare il deposito?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.gestoreBackup.effettua_backup()
            self.gestoreConsegna.depositaConsegneNegative()
            self.gestoreRitiro.depositaRitiriPositivi()
            QMessageBox.information(self, "Deposito Confermato", "Deposito Pacchi Confermato")
            self.close()