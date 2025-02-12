from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFormLayout, QVBoxLayout, QHBoxLayout, QMessageBox
from datetime import datetime, timedelta
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo


class VistaRimandaConsegna(QWidget):
    def __init__(self, gestoreConsegna, consegna_selezionata):
        super().__init__()
        self.gestoreConsegna = gestoreConsegna
        self.consegna_selezionata = consegna_selezionata
        self.setWindowTitle("Rimanda consegna")
        self.setFixedSize(400,100)
        self.messaggio = QLabel("Vuoi rimandare la seguente consegna al giorno successivo?")
        self.conferma = QPushButton("Sì")
        self.indietro = QPushButton("No, torna indietro")
        self.initUI()
    
    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.messaggio.setStyleSheet("font-size: 15px; font-family: Arial; font-weight: bold;")
        self.conferma.setStyleSheet("font-size: 15px; font-family: Arial;")
        self.indietro.setStyleSheet("font-size: 15px; font-family: Arial;")
        vlayout.addWidget(self.messaggio)
        hlayout.addWidget(self.indietro)
        hlayout.addWidget(self.conferma)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
        self.conferma.clicked.connect(lambda : self.rimanda_consegna(self.gestoreConsegna, self.consegna_selezionata))
        self.indietro.clicked.connect(self.submit_chiusura)
    
    def nuovo_giorno_disponibile(self, giorno_consegna, giorni_disponibili):
        
        # Ottieni l'indice del giorno della settimana (0 = lunedì, 6 = domenica)
        indice_consegna = giorno_consegna.weekday()
        
        # Converti la lista dei giorni della settimana con la prima lettera maiuscola per confrontare
        giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
    
        # A partire dal giorno di consegna, cerca il primo giorno disponibile
        for i in range(7):
            # Calcola l'indice del giorno da verificare (usando il modulo per far girare la settimana)
            giorno_da_verificare = (indice_consegna + i) % 7
            
            # Trova il nome del giorno corrispondente all'indice
            giorno_nome = giorni_settimana[giorno_da_verificare]
            
            # Verifica se il giorno calcolato è presente nella lista dei giorni disponibili
            if giorno_nome in giorni_disponibili:
                giorni_da_aggiungere = i  # Aggiungi il numero di giorni necessari per arrivare al giorno trovato
                giorno_disponibile_dt = giorno_consegna + timedelta(days=giorni_da_aggiungere)
                
                return giorno_disponibile_dt.strftime("%d/%m/%Y")  # Ritorna il primo giorno disponibile
        
        return None
    
    def rimanda_consegna(self, gestoreConsegna, consegna_selezionata):
        if consegna_selezionata.datiConsegna.statoConsegna != "Consegnato":
            if isinstance(consegna_selezionata, Pacco):
                if consegna_selezionata.datiConsegna.statoConsegna != "Consegna rimandata":
                    data_consegna_selezionata = datetime.strptime(consegna_selezionata.datiConsegna.dataConsegna, "%d/%m/%Y")
                    nuova_data = data_consegna_selezionata + timedelta(days=1)
                    if gestoreConsegna.rimandaConsegna(consegna_selezionata, nuova_data):
                        self.consegna_rimandata()
                else:
                    QMessageBox.critical(self, "Errore", "Consegna già rimandata", QMessageBox.Ok, QMessageBox.Ok)
            elif isinstance(consegna_selezionata, Collo):
                giorni_disponibili = consegna_selezionata.aziendaDestinatario.giorniApertura
                giorno_consegna = datetime.strptime(consegna_selezionata.datiConsegna.dataConsegna, "%d/%m/%Y")
                nuova_data = self.nuovo_giorno_disponibile(giorno_consegna, giorni_disponibili)
                if nuova_data!=None:
                    if gestoreConsegna.rimandaConsegna(consegna_selezionata,nuova_data):
                        self.consegna_rimandata()
                else:
                    QMessageBox.critical(self, "Errore", "Data non validata", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Errore", "Consegna già effettuata\nImpossibile rimandare", QMessageBox.Ok, QMessageBox.Ok)
    
    def consegna_rimandata(self):
        reply = QMessageBox.question(self, "Conferma", "Operazione riuscita! Consegna Rimandata", QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            self.close()
            
    def submit_chiusura(self):
        self.close()