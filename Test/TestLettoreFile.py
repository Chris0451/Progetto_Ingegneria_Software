import unittest
from unittest.mock import patch, mock_open
from Attivita.LettoreFile import LettoreFile  # Assicurati di importare correttamente la tua classe LettoreFile
from Attivita.Pacco import Pacco
from Attivita.Collo import Collo
from Attivita.Consegna import Consegna
from Attivita.Ritiro import Ritiro
from Utenti.Cliente import Cliente
from Utenti.Azienda import Azienda
from Utenti.Posizione import Posizione

class TestLettoreFile(unittest.TestCase):

    # Test per la lettura delle consegne (pacchi normali)
    @patch("builtins.open", new_callable=mock_open, read_data="['codicePacco', 10, 20, 'tipo', 'pago', ['Mittente', 'Cognome', 'email', '1234', 'CF', 'Cliente001', ['via', '1', 'Comune', 'Prov', '12345']], ['Destinatario', 'Cognome', 'email', '5678', 'CF', 'Cliente002', ['via', '2', 'Comune', 'Prov', '54321']], ['ConsegnaCod', '01/01/2025', '10:00', 'completato', 100]]***********")
    def test_leggi_consegne(self, mock_file):
        lettore_file = LettoreFile()
        pacchi = lettore_file.leggi_consegne()

        # Verifica che il file sia stato aperto correttamente
        mock_file.assert_called_with("Dati/listaConsegne.txt", "r")
        
        # Verifica che i dati siano stati correttamente letti e trasformati in oggetti Pacco
        self.assertEqual(len(pacchi), 1)  # Dovremmo avere un pacco
        pacco = pacchi[0]
        
        self.assertIsInstance(pacco, Pacco)
        self.assertEqual(pacco.codicePacco, 'codicePacco')
        self.assertEqual(pacco.mittente.nome, 'Mittente')
        self.assertEqual(pacco.destinatario.nome, 'Destinatario')
        self.assertIsInstance(pacco.consegna, Consegna)
        self.assertEqual(pacco.consegna.codiceConsegna, 'ConsegnaCod')

    # Test per la lettura dei ritiri
    @patch("builtins.open", new_callable=mock_open, read_data="['codicePacco', 15, 25, 'tipo', 'pago', ['Mittente', 'Cognome', 'email', '1234', 'CF', 'Cliente001', ['via', '1', 'Comune', 'Prov', '12345']], ['Destinatario', 'Cognome', 'email', '5678', 'CF', 'Cliente002', ['via', '2', 'Comune', 'Prov', '54321']], ['RitiroCod', '02/02/2025', '15:00', 'in attesa']]***********")
    def test_leggi_ritiri(self, mock_file):
        lettore_file = LettoreFile()
        pacchi = lettore_file.leggi_ritiri()

        # Verifica che il file sia stato aperto correttamente
        mock_file.assert_called_with("Dati/listaRitiri.txt", "r")
        
        # Verifica che i dati siano stati correttamente letti e trasformati in oggetti Pacco
        self.assertEqual(len(pacchi), 1)  # Dovremmo avere un pacco
        pacco = pacchi[0]
        
        self.assertIsInstance(pacco, Pacco)
        self.assertEqual(pacco.codicePacco, 'codicePacco')
        self.assertEqual(pacco.mittente.nome, 'Mittente')
        self.assertEqual(pacco.destinatario.nome, 'Destinatario')
        self.assertIsInstance(pacco.ritiro, Ritiro)
        self.assertEqual(pacco.ritiro.codiceRitiro, 'RitiroCod')

    # Test per la lettura dei colli
    @patch("builtins.open", new_callable=mock_open, read_data=""" 
    [
        ['1', 'Elettronica', 20.0, 30.0, 
        [
            ['Alberto', 'Festa', 'AF200803H', '3773821832', 'alberto.festa@example.com', 'CL0001', ['Via Michele Fazioli', 1, 'Ancona', 'AN', 66019]], 
            'F000', 'Festa Group', '8:30', '18:30', ['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi', 'Venerdi']
        ],
        [
            ['Cristian', 'Di Cintio', 'CD201103K', '3893821832', 'cristian.dc@example.com', 'CL0002', ['Via Bartolo', 1, 'Ancona', 'AN', 66019]], 
            'F001', 'DC Group', '12:30', '18:30', ['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi', 'Venerdi']
        ],
        ['C220', '07/02/2025', '14:00', 'in deposito']
    ]
    """)
    def test_leggi_colli(self, mock_file):
        lettore_file = LettoreFile()
        colli = lettore_file.leggi_lista_colli()

        # Verifica che il file sia stato aperto correttamente
        mock_file.assert_called_with("Dati/listaColliRitiri.txt", "r")
        
        # Verifica che i dati siano stati correttamente letti e trasformati in oggetti Collo
        self.assertEqual(len(colli), 1)  # Dovremmo avere un collo
        collo = colli[0]
        
        # Verifica attributi del collo
        self.assertIsInstance(collo, Collo)
        self.assertEqual(collo.codice_collo, '1')
        self.assertEqual(collo.natura_collo, 'Elettronica')
        self.assertEqual(collo.peso, 20.0)
        self.assertEqual(collo.volume, 30.0)
        
        # Verifica che i dati del mittente siano corretti
        self.assertIsInstance(collo.mittente, Cliente)
        self.assertEqual(collo.mittente.nome, 'Alberto')
        self.assertEqual(collo.mittente.posizione.via, 'Via Michele Fazioli')
        
        # Verifica che i dati del destinatario siano corretti
        self.assertIsInstance(collo.destinatario, Cliente)
        self.assertEqual(collo.destinatario.nome, 'Cristian')
        self.assertEqual(collo.destinatario.posizione.via, 'Via Bartolo')
        
        # Verifica che i dati dell'azienda mittente e destinatario siano corretti
        self.assertIsInstance(collo.mittente_azienda, Azienda)
        self.assertEqual(collo.mittente_azienda.nome_azienda, 'Festa Group')
        self.assertEqual(collo.mittente_azienda.orario_apertura, '8:30')
        
        self.assertIsInstance(collo.destinatario_azienda, Azienda)
        self.assertEqual(collo.destinatario_azienda.nome_azienda, 'DC Group')
        self.assertEqual(collo.destinatario_azienda.orario_chiusura, '18:30')
        
        # Verifica che il ritiro sia stato correttamente creato
        self.assertIsInstance(collo.ritiro, Ritiro)
        self.assertEqual(collo.ritiro.codice_ritiro, 'C220')
        self.assertEqual(collo.ritiro.data_ritiro, '07/02/2025')
        self.assertEqual(collo.ritiro.ora_ritiro, '14:00')
        self.assertEqual(collo.ritiro.stato_ritiro, 'in deposito')

if __name__ == "__main__":
    unittest.main()
