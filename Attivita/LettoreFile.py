from Attivita.Pacco import Pacco
from Utenti.Cliente import Cliente
from Utenti.Posizione import Posizione
from Attivita.Consegna import Consegna
from Attivita.Ritiro import Ritiro
from Utenti.Azienda import Azienda
from Attivita.Collo import Collo
import ast

class LettoreFile:
    def __init__(self):
        pass

    def parse_posizione(self, data):
        """Converte una lista di dati in un oggetto Posizione."""
        return Posizione(data[0], data[1], data[2], data[3], data[4])

    def parse_cliente(self, data):
        """Converte una lista di dati in un oggetto Cliente."""
        nome, cognome, email, telefono, codiceFiscale, codiceCliente, posizione_data = data
        posizione = self.parse_posizione(posizione_data)
        return Cliente(nome, cognome, email, telefono, codiceFiscale, codiceCliente, posizione)

    def parse_consegna(self, data):
        """Converte una lista di dati in un oggetto Consegna."""
        codiceConsegna, dataConsegna, oraConsegna, statoConsegna, valoreContrassegno = data
        return Consegna(codiceConsegna, dataConsegna, oraConsegna, statoConsegna, valoreContrassegno)
    
    def parse_ritiro(self, data):
        """Converte una lista di dati in un oggetto Ritiro."""
        codiceRitiro, dataRitiro, oraRitiro, statoRitiro = data
        return Ritiro(codiceRitiro, dataRitiro, oraRitiro, statoRitiro)

    def parse_pacco_consegna(self, data):
        """Converte una lista di dati in un oggetto Pacco per una consegna."""
        codicePacco = data[0]
        peso = data[1]
        volume = data[2]
        tipo = data[3]
        metodoPagamento = data[4]
        mittente_data = data[5]
        destinatario_data = data[6]
        consegna_data = data[7:12]

        mittente = self.parse_cliente(mittente_data)
        destinatario = self.parse_cliente(destinatario_data)
        consegna = self.parse_consegna(consegna_data)

        return Pacco(codicePacco, peso, volume, tipo, metodoPagamento, mittente, destinatario, consegna, None)
    
    def parse_pacco_ritiro(self, data):
        """Converte una lista di dati in un oggetto Pacco per un ritiro."""
        codicePacco = data[0]
        peso = data[1]
        volume = data[2]
        tipo = data[3]
        metodoPagamento = data[4]
        mittente_data = data[5]
        destinatario_data = data[6]
        ritiro_data = data[7:11]

        mittente = self.parse_cliente(mittente_data)
        destinatario = self.parse_cliente(destinatario_data)
        ritiro = self.parse_ritiro(ritiro_data)
        
        return Pacco(codicePacco, peso, volume, tipo, metodoPagamento, mittente, destinatario, None, ritiro)

    def leggi_consegne(self):
        """Legge il file listaConsegne.txt e restituisce una lista di oggetti Pacco per le consegne."""
        pacchi = []
        try:
            with open("Dati/listaConsegne.txt", "r") as file:
                content = file.read()
                records = content.split("***********")  # Corretto separatore
                for record in records:
                    record = record.strip()
                    if record:  # Salta record vuoti
                        try:
                            data = ast.literal_eval(record)  # Parsing sicuro della stringa in lista Python
                            pacco = self.parse_pacco_consegna(data)
                            pacchi.append(pacco)
                        except (SyntaxError, ValueError) as e:
                            print(f"Errore nel parsing del record: {record} - {e}")
        except FileNotFoundError:
            print("Errore: Il file listaConsegne.txt non è stato trovato.")
        
        return pacchi

    def leggi_ritiri(self):
        """Legge il file listaRitiri.txt e restituisce una lista di oggetti Pacco per i ritiri."""
        pacchi = []
        try:
            with open("Dati/listaRitiri.txt", "r") as file:
                content = file.read()
                records = content.split("***********")  # Corretto separatore
                for record in records:
                    record = record.strip()
                    if record:  # Salta record vuoti
                        try:
                            data = ast.literal_eval(record)  # Parsing sicuro della stringa in lista Python
                            pacco = self.parse_pacco_ritiro(data)
                            pacchi.append(pacco)
                        except (SyntaxError, ValueError) as e:
                            print(f"Errore nel parsing del record: {record} - {e}")
        except FileNotFoundError:
            print("Errore: Il file listaRitiri.txt non è stato trovato.")
        
        return pacchi
    
    def crea_azienda(self, dati):
        responsabile_raw, codice_fornitore, nome_azienda, orario_apertura, orario_chiusura, giorni_apertura = dati
        responsabile = self.crea_cliente(responsabile_raw)
        return Azienda(responsabile, responsabile.posizione, nome_azienda, orario_apertura, orario_chiusura, giorni_apertura)
    
    def crea_cliente(self, dati):
        nome, cognome, codice_fiscale, telefono, email, codice_cliente, posizione_raw = dati
        posizione = self.crea_posizione(posizione_raw)
        return Cliente(nome, cognome, email, telefono, codice_fiscale, codice_cliente, posizione)
    
    def crea_posizione(self, dati):
        via, civico, comune, provincia, CAP = dati
        return Posizione(via, civico, comune, provincia, CAP)
    
    def crea_ritiro(self, dati):
        codice_ritiro, data_ritiro, ora_ritiro, stato_ritiro = dati
        return Ritiro(codice_ritiro, data_ritiro, ora_ritiro, stato_ritiro)

    
    def leggi_lista_colli(self):
        with open("Dati/listaColliRitiri.txt", "r") as file:
            contenuto = file.read()
        
        # Separiamo le istanze di Collo usando "***********"
        colli_raw = contenuto.split("***********")
        colli = []
        
        for collo_raw in colli_raw:
            collo_raw = collo_raw.strip()
            if not collo_raw:
                continue
            
            try:
                # Convertiamo la stringa in una struttura dati Python
                collo_dati = ast.literal_eval(collo_raw)
                
                codice_collo, natura_collo, peso, volume, azienda_mittente_raw, azienda_destinatario_raw, ritiro_raw = collo_dati
                
                # Creazione degli oggetti
                azienda_mittente = self.crea_azienda(azienda_mittente_raw)
                azienda_destinatario = self.crea_azienda(azienda_destinatario_raw)
                ritiro = self.crea_ritiro(ritiro_raw)
                
                collo = Collo(codice_collo, natura_collo, peso, volume, azienda_mittente, azienda_destinatario, ritiro, None)
                colli.append(collo)
            except Exception as e:
                print(f"Errore nel parsing del collo: {e}")
                continue
                
        return colli
    
    def crea_azienda(self, dati):
        responsabile_raw, codice_fornitore, nome_azienda, orario_apertura, orario_chiusura, giorni_apertura = dati
        responsabile = self.crea_cliente(responsabile_raw)
        return Azienda(responsabile, responsabile.posizione, nome_azienda, orario_apertura, orario_chiusura, giorni_apertura)
    
    def crea_cliente(self, dati):
        nome, cognome, codice_fiscale, telefono, email, codice_cliente, posizione_raw = dati
        posizione = self.crea_posizione(posizione_raw)
        return Cliente(nome, cognome, email, telefono, codice_fiscale, codice_cliente, posizione)
    
    def crea_posizione(self, dati):
        via, civico, comune, provincia, CAP = dati
        return Posizione(via, civico, comune, provincia, CAP)
    
    def crea_ritiro(self, dati):
        codice_ritiro, data_ritiro, ora_ritiro, stato_ritiro = dati
        return Ritiro(codice_ritiro, data_ritiro, ora_ritiro, stato_ritiro)
    
 


    def leggi_lista_colli_consegne(self):
        def crea_posizione(dati):
            via, civico, comune, provincia, CAP = dati
            return Posizione(via, civico, comune, provincia, CAP)
        
        def crea_consegna(dati):
            codice_consegna, data_consegna, ora_consegna, stato_consegna = dati
            return Consegna(codice_consegna, data_consegna, ora_consegna, stato_consegna, None)
        
        def crea_azienda(dati):
            responsabile_raw, codice_fornitore, nome_azienda, orario_apertura, orario_chiusura, giorni_apertura = dati
            responsabile = crea_cliente(responsabile_raw)
            return Azienda(responsabile, crea_posizione(responsabile_raw[-1]), nome_azienda, orario_apertura, orario_chiusura, giorni_apertura)
        
        def crea_cliente(dati):
            nome, cognome, codice_fiscale, telefono, email, codice_cliente, posizione_raw = dati
            posizione = crea_posizione(posizione_raw)
            return Cliente(nome, cognome, email, telefono, codice_fiscale, codice_cliente, posizione)
        
        
        with open("Dati/listaColliConsegnare.txt", "r") as file:
            contenuto = file.read()
        
        # Separiamo le istanze di Collo usando "***********"
        colli_raw = contenuto.split("***********")
        colli = []
        
        for collo_raw in colli_raw:
            collo_raw = collo_raw.strip()
            if not collo_raw:
                continue
            
            try:
                # Convertiamo la stringa in una struttura dati Python
                collo_dati = ast.literal_eval(collo_raw)
                
                codice_collo, natura_collo, peso, volume, azienda_mittente_raw, azienda_destinatario_raw, consegna_raw = collo_dati
                
                # Creazione degli oggetti
                azienda_mittente = crea_azienda(azienda_mittente_raw)
                azienda_destinatario = crea_azienda(azienda_destinatario_raw)
                consegna = crea_consegna(consegna_raw)
                
                collo = Collo(codice_collo, natura_collo, peso, volume, azienda_mittente, azienda_destinatario, None, consegna)
                colli.append(collo)
            except Exception as e:
                print(f"Errore nel parsing del collo: {e}")
                continue
                
        return colli
    
    