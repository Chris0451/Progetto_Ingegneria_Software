from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QFormLayout
from Attivita.LettoreFile import LettoreFile
from Vista.VistaConsegnaAggiunta import VistaConsegnaAggiunta
from Vista.VistaConsegnaNonAggiunta import VistaConsegnaNonAggiunta
from Gestore.GestoreConsegna import GestoreConsegna

class VistaPresaInCarico(QWidget) :
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,150)
        self.setWindowTitle("Conferma consegna")
        self.titolo = QLabel("Inserisci codice consegna: ")
        self.inserimento_codice = QLineEdit(self)
        self.conferma = QPushButton("Conferma", self)
        self.indietro = QPushButton("Indietro", self)
        self.initUI()
        
        
    def initUI(self):
        layout1 = QFormLayout()
        layout1.addRow(self.titolo, self.inserimento_codice)
        layout1.addRow(self.conferma)
        layout1.addRow(self.indietro)
        self.setLayout(layout1)
        self.titolo.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.inserimento_codice.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.conferma.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.indietro.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.conferma.clicked.connect(self.submit_lettura)
        self.indietro.clicked.connect(self.submit_chiusura)
        
    def submit_lettura(self):
        lettore = LettoreFile()
        pacchi = lettore.read_consegne()
        codice = self.inserimento_codice.text()
        trovato = False
        for pacco in pacchi:
            if codice == pacco.consegna.codiceConsegna:
                print(f"Codice confermato: {codice}")
                pacco.consegna.setStatoConsegna("In transito")
                print("Nuovo stato: "+pacco.consegna.statoConsegna)
                self.consegna_aggiunta = VistaConsegnaAggiunta()
                self.consegna_aggiunta.show()
                trovato = True
        if not trovato:
            self.consegna_nonAggiunta = VistaConsegnaNonAggiunta()
            self.consegna_nonAggiunta.show()
        self.inserimento_codice.setText("")
    
    def submit_chiusura(self):
        self.close()
        
        
        