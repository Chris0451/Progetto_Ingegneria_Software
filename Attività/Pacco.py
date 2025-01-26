class Pacco:
    def __init__(self, codicePacco, peso, volume, tipo, metodoPagamento, destinatario, mittente):
        self.codicePacco = codicePacco
        self.peso = peso
        self.volume = volume
        self.tipo = tipo
        self.metodoPagamento = metodoPagamento
        self.mittente = mittente
        self.destinatario = destinatario
    def getInfoPacco(self, codicePacco, peso, volume, tipo, metodoPagamento, destinatario, mittente):
           print(f"Destinatario: {self.destinatario}\n")
           print(f"Mittente: {self.mittente}\n")
           print(f"Codice Pacco: {self.codicePacco}\n")
           print(f"Peso: {self.peso}\n")
           print(f"Volume: {self.volume}\n")  
           print(f"Tipo: {self.tipo}\n")
           print(f"Metodo Pagamento: {self.metodoPagamento}\n")
    
           
       