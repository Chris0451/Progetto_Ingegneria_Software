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
    def getInfoPaccoConsegna(self):
        return f"Codice Pacco: {self.codicePacco}\nPeso: {self.peso}\nVolume: {self.volume}\nTipo: {self.tipo}\nMetodo Pagamento: {self.metodoPagamento}\n\nConsegna:\n" + self.datiConsegna.getInfoConsegna() + "\nDestinatario:\n" + self.destinatario.getInfoCliente() + "\nMittente:\n" + self.mittente.getInfoCliente() + "\n"
    def getInfoPaccoRitiro(self):
        return f"Codice Pacco: {self.codicePacco}\nPeso: {self.peso}\nVolume: {self.volume}\nTipo: {self.tipo}\nMetodo Pagamento: {self.metodoPagamento}\n\nRitiro:\n" + self.datiRitiro.getInfoRitiro() + "\nDestinatario:\n" + self.destinatario.getInfoCliente() + "\nMittente:\n" + self.mittente.getInfoCliente() + "\n"
           
       
