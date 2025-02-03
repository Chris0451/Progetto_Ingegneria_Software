from Attivita.Pacco import Pacco
from Utenti.Cliente import Cliente
from Utenti.Posizione import Posizione
from Attivita.Consegna import Consegna
import ast
class LettoreFile:
    def _init_ (self):
        pass
    
    def parse_posizione(self, data):
        return Posizione(data[0], data[1], data[2], data[3], data[4])

    def parse_cliente(self, data):
        nome, cognome, email, telefono, codiceFiscale, codiceCliente, posizione_data = data
        posizione = self.parse_posizione(posizione_data)
        return Cliente(nome, cognome, email, telefono, codiceFiscale, codiceCliente, posizione)

    def parse_consegna(self, data):
        codiceConsegna, dataConsegna, oraConsegna, statoConsegna, valoreContrassegno = data
        return Consegna(codiceConsegna, dataConsegna, oraConsegna, statoConsegna, valoreContrassegno)

    def parse_pacco(self, data):
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
    def read_consegne(self):
        pacchi = []
        with open("Dati/listaConsegne.txt", "r") as file:
            content = file.read()
            records = content.split("*")  # Split by delimiter
            for record in records:
                record = record.strip()
                if record:  # Skip empty records
                    data = ast.literal_eval(record)  # Safely parse the string as a Python literal
                    pacco = self.parse_pacco(data)
                    pacchi.append(pacco)
        return pacchi
