from Attivita.Pacco import Pacco
from Attivita.Consegna import Consegna
from Utenti.Cliente import Cliente
from Utenti.Posizione import Posizione

class LettoreFile:
    def __init__(self):
        pass
    def read_consegne(self):
        pacchi = []
        try:
            with open("Dati/listaConsegne.txt", "r") as file:
                for numero_riga, linea in enumerate(file, start=1):
                    # Rimuovi spazi e caratteri di nuova linea
                    linea = linea.strip()
                    if not linea:
                        print(f"Riga {numero_riga} vuota, ignorata.")
                        continue  # Salta le righe vuote
                    try:
                        # Converti la stringa in lista
                        dati = eval(linea)  # Usa eval solo se il formato è affidabile
                        if len(dati) != 8:
                            raise ValueError(f"Riga {numero_riga} non ha 8 elementi.")

                        codicePacco = int(dati[0])
                        peso = float(dati[1])
                        volume = float(dati[2])
                        tipo = dati[3]
                        metodoPagamento = dati[4]

                        # Parsing del mittente
                        mittente_info = dati[5]
                        if len(mittente_info) != 6:
                            raise ValueError(f"Riga {numero_riga}: Dati del mittente non validi.")
                        
                        posizione_mittente_info = mittente_info[5]
                        if len(posizione_mittente_info) != 5:
                            raise ValueError(f"Riga {numero_riga}: Dati della posizione del mittente non validi.")
                        
                        posizione_mittente = Posizione(*posizione_mittente_info)
                        mittente = Cliente(mittente_info[0], mittente_info[1], mittente_info[2],
                                           mittente_info[3], mittente_info[4], mittente_info[5],
                                           posizione_mittente)

                        # Parsing del destinatario
                        destinatario_info = dati[6]
                        if len(destinatario_info) != 6:
                            raise ValueError(f"Riga {numero_riga}: Dati del destinatario non validi.")
                        
                        posizione_destinatario_info = destinatario_info[5]
                        if len(posizione_destinatario_info) != 5:
                            raise ValueError(f"Riga {numero_riga}: Dati della posizione del destinatario non validi.")
                        
                        posizione_destinatario = Posizione(*posizione_destinatario_info)
                        destinatario = Cliente(destinatario_info[0], destinatario_info[1], destinatario_info[2], 
                                               destinatario_info[3], destinatario_info[4], destinatario_info[5], 
                                               posizione_destinatario)
                        
                        dati_consegna_info = dati[7]
                        if len(dati_consegna_info) != 5:
                            raise ValueError(f"Riga {numero_riga}: Dati della consegna non validi.")
                        dati_consegna = Consegna(*dati_consegna_info)
                        
                        # Crea un oggetto Pacco
                        pacco = Pacco(codicePacco, peso, volume, tipo, metodoPagamento, mittente, destinatario, dati_consegna, None)
                        pacchi.append(pacco)
                    except SyntaxError as e:
                        print(f"Errore di sintassi nella riga {numero_riga}: {e}")
                    except Exception as e:
                        print(f"Errore nella riga {numero_riga}: {e}")

        except FileNotFoundError:
            print("Il file 'listaConsegne.txt' non è stato trovato.")
        except Exception as e:
            print(f"Si è verificato un errore: {e}")

        return pacchi


# Esempio di utilizzo
# lettore = LettoreFile()
# pacchi = lettore.read_file()

# for pacco in pacchi:
#     print(pacco)
    
    # def read_file(self):
    #     pacchi = []
    #     try:
    #         with open("listaConsegne.txt", "r") as file:
    #             for linea in file:
    #                 # Rimuovi spazi e caratteri di nuova linea
    #                 linea = linea.strip()
    #                 if linea:
    #                     # Converti la stringa in lista
    #                     dati = eval(linea)  # Usa eval solo se il formato è affidabile
    #                     codicePacco = int(dati[0])
    #                     peso = float(dati[1])
    #                     volume = float(dati[2])
    #                     tipo = dati[3]
    #                     metodoPagamento = dati[4]

    #                     # Parsing del mittente
    #                     mittente_info = dati[5]  # Lista con i dati del mittente
    #                     mittente = Utente(mittente_info[0], mittente_info[1], mittente_info[2],
    #                                       mittente_info[3], mittente_info[4])

    #                     # Parsing del destinatario
    #                     destinatario_info = dati[6]  # Lista con i dati del destinatario
    #                     destinatario = Utente(destinatario_info[0], destinatario_info[1], destinatario_info[2],
    #                                            destinatario_info[3], destinatario_info[4])

    #                     # Crea un oggetto Pacco
    #                     pacco = Pacco(codicePacco, peso, volume, tipo, metodoPagamento, mittente, destinatario)
    #                     pacchi.append(pacco)

    #     except FileNotFoundError:
    #         print("Il file 'listaPacchi.txt' non è stato trovato.")
    #     except Exception as e:
    #         print(f"Si è verificato un errore: {e}")

    #     return pacchi

# Esempio di utilizzo
# lettore = LettoreFile()
# pacchi = lettore.read_file()

#     def salva_pacchi_pickle():
   
#         pacco1 = Pacco(codicePacco="1", peso=5.0, volume=10.0, tipo="ndjns", metodoPagamento="jadnaò", destinatario="jdsnjfs", mittente="njsdncsoid")
#         pacco2 = Pacco(codicePacco="2", peso=2.5, volume=5.0, tipo="ofwsfwsio", metodoPagamento="sodfjnswfoj", destinatario="djnsof", mittente="csdvisodvnos")
#         pacco3 = Pacco(codicePacco="3", peso=1.2, volume=2.0, tipo="csjjdnasi", metodoPagamento="ncsidanio", destinatario="njcoaic", mittente="csnodicaso")
    
#         with open('pacchi.pickle', 'wb') as f:
#             pickle.dump([pacco1, pacco2, pacco3], f, pickle.HIGHEST_PROTOCOL)

#         print("Salvataggio ok")

#     def carica_pacchi_pickle():
#         with open('pacchi.pickle', 'rb') as f:
#             pacchi = pickle.load(f)

#         print("Caricamento nel file ok")
#         return pacchi

#     #salva_pacchi_pickle()
#     pacchi_caricati = carica_pacchi_pickle()


# #for pacco in pacchi_caricati:
# #    pacco.getInfoPacco()
