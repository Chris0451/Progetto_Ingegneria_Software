class Pacco:
    def __init__(self, codicePacco, peso, volume, tipo, metodoPagamento, destinatario, mittente, datiConsegna, datiRitiro):
        self.codicePacco = codicePacco
        self.peso = peso
        self.volume = volume
        self.tipo = tipo
        self.metodoPagamento = metodoPagamento
        self.mittente = mittente
        self.destinatario = destinatario
        self.datiConsegna = datiConsegna
        self.datiRitiro = datiRitiro
    def getInfoPacco(self):
        print(f"Codice Pacco: {self.codicePacco}\n")
        print(f"Peso: {self.peso}\n")
        print(f"Volume: {self.volume}\n")  
        print(f"Tipo: {self.tipo}\n")
        print(f"Metodo Pagamento: {self.metodoPagamento}\n")
        print("Consegna: " + self.datiConsegnaonsegna.getInfoConsegna() + "\n")
        print("Destinatario: " + self.destinatario.getInfoDestinatario() + "\n")
        print("Ritiro: " + self.datiRitiro.getInfoRitiro() + "\n")
        print("Mittente: " + self.mittente.getInfoMittente() + "\n")
    
           
       
