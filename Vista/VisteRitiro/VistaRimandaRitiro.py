from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from datetime import datetime, timedelta
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo


class VistaRimandaRitiro(QWidget):
    def __init__(self, gestoreRitiro, ritiro_selezionato):
        super().__init__()
        self.gestoreRitiro = gestoreRitiro
        self.ritiro_selezionato = ritiro_selezionato
        print(type(self.ritiro_selezionato))
        self.setWindowTitle("Rimanda ritiro")
        self.setFixedSize(400,100)
        self.messaggio = QLabel("Vuoi rimandare il seguente ritiro al giorno successivo?")
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
        self.conferma.clicked.connect(lambda : self.rimanda_ritiro(self.gestoreRitiro, self.ritiro_selezionato, datetime.today()))
        self.indietro.clicked.connect(self.submit_chiusura)
        
    def rimanda_ritiro(self, gestoreRitiro, ritiro_selezionato, giorno_ritiro):
        # indice_ritiro = giorno_ritiro.weekday()
        
        if self.ritiro_selezionato.datiRitiro.statoRitiro != "Ritirato":
            if isinstance(ritiro_selezionato, Pacco):
                if ritiro_selezionato.datiRitiro.statoRitiro != "Ritiro rimandato":
                    data_ritiro_selezionato = datetime.strptime(ritiro_selezionato.datiRitiro.dataRitiro, "%d/%m/%Y")
                    nuova_data = data_ritiro_selezionato + timedelta(days=1)
                    if gestoreRitiro.rimandaRitiro(ritiro_selezionato, nuova_data):
                        self.ritiro_rimandato()
                else:
                     QMessageBox.critical(self, "Errore", "Ritiro già rimandato", QMessageBox.Ok, QMessageBox.Ok)
            elif isinstance(ritiro_selezionato, Collo):
                giorni_disponibili = ritiro_selezionato.aziendaMittente.giorniApertura
                giorno_consegna = datetime.strptime(ritiro_selezionato.datiRitiro.dataRitiro, "%d/%m/%Y")
                nuova_data = self.nuovo_giorno_disponibile(giorno_ritiro, giorni_disponibili)
                if nuova_data!=None:
                    if gestoreRitiro.rimandaRitiro(ritiro_selezionato,nuova_data):
                        self.consegna_rimandata()
                else:
                    QMessageBox.critical(self, "Errore", "Data non validata", QMessageBox.Ok, QMessageBox.Ok)
        else:
             QMessageBox.critical(self, "Errore", "Ritiro già effettuato\nImpossibile rimandare", QMessageBox.Ok, QMessageBox.Ok)
     
    
    def nuovo_giorno_disponibile(self, giorno_ritiro, giorni_disponibili):
        
        # Ottieni l'indice del giorno della settimana (0 = lunedì, 6 = domenica)
        indice_ritiro = giorno_ritiro.weekday()
        
        # Converti la lista dei giorni della settimana con la prima lettera maiuscola per confrontare
        giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
    
        # A partire dal giorno di consegna, cerca il primo giorno disponibile
        for i in range(7):
            # Calcola l'indice del giorno da verificare (usando il modulo per far girare la settimana)
            giorno_da_verificare = (indice_ritiro + i) % 7
            
            # Trova il nome del giorno corrispondente all'indice
            giorno_nome = giorni_settimana[giorno_da_verificare]
            
            # Verifica se il giorno calcolato è presente nella lista dei giorni disponibili
            if giorno_nome in giorni_disponibili:
                giorni_da_aggiungere = i  # Aggiungi il numero di giorni necessari per arrivare al giorno trovato
                giorno_disponibile_dt = giorno_ritiro + timedelta(days=giorni_da_aggiungere)
                
                return giorno_disponibile_dt.strftime("%d/%m/%Y")  # Ritorna il primo giorno disponibile
        
        return None

    def ritiro_rimandato(self):
        reply = QMessageBox.question(self, "Conferma", "Operazione riuscita! Ritiro Rimandato", QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            self.close()
            
    def submit_chiusura(self):
        self.close()

