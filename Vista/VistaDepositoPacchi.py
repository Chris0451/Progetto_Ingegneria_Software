from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMessageBox, QTableWidget, QHeaderView,QTableWidgetItem
from PyQt5.QtCore import Qt

class VistaDepositoPacchi(QWidget):
    def __init__(self, gestoreConsegna, gestoreRitiro):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.gestoreRitiro = gestoreRitiro

        self.setWindowTitle("Deposito Pacchi")
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
        for pacco in self.gestoreRitiro.listaRitiriPositivi:
            self.aggiungi_riga_pacco(pacco)
        for collo in self.gestoreRitiro.listaColliPositivi:
            self.aggiungi_riga_collo(collo)

    def aggiungi_riga_pacco(self, pacco):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        self.table_widget.setItem(row_position, 0, QTableWidgetItem(pacco.codicePacco))
        self.table_widget.setItem(row_position, 1, QTableWidgetItem(str(pacco.peso))) #conversione in stringa
        self.table_widget.setItem(row_position, 2, QTableWidgetItem(str(pacco.volume))) #conversione in stringa
        self.table_widget.setItem(row_position, 3, QTableWidgetItem(pacco.tipo))
        self.table_widget.setItem(row_position, 4, QTableWidgetItem(pacco.metodoPagamento))
        self.table_widget.setItem(row_position, 5, QTableWidgetItem(pacco.mittente.nome + " " + pacco.mittente.cognome)) #nome e cognome del mittente
        self.table_widget.setItem(row_position, 6, QTableWidgetItem(pacco.destinatario.nome + " " + pacco.destinatario.cognome)) #nome e cognome del destinatario
        self.table_widget.setItem(row_position, 7, QTableWidgetItem(pacco.datiRitiro.statoRitiro))

    def aggiungi_riga_collo(self, collo):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        self.table_widget.setItem(row_position, 0, QTableWidgetItem(collo.codiceCollo))
        self.table_widget.setItem(row_position, 1, QTableWidgetItem(str(collo.peso))) #conversione in stringa
        self.table_widget.setItem(row_position, 2, QTableWidgetItem(str(collo.volume))) #conversione in stringa
        self.table_widget.setItem(row_position, 3, QTableWidgetItem(collo.naturaCollo))
        self.table_widget.setItem(row_position, 4, QTableWidgetItem("N/A")) #metodo pagamento non presente per i colli
        self.table_widget.setItem(row_position, 5, QTableWidgetItem(collo.aziendaMittente.nomeAzienda)) #nome azienda mittente
        self.table_widget.setItem(row_position, 6, QTableWidgetItem(collo.aziendaDestinatario.nomeAzienda)) #nome azienda destinatario
        self.table_widget.setItem(row_position, 7, QTableWidgetItem(collo.datiRitiro.statoRitiro))


    def conferma_deposito(self):
        reply = QMessageBox.question(self, "Conferma Deposito", "Sei sicuro di voler confermare il deposito?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.gestoreRitiro.depositaRitiriPositivi()
            QMessageBox.information(self, "Deposito Confermato", "Deposito Pacchi Confermato")
            self.close()