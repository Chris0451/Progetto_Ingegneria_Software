class GestoreBackup():
    def __init__(self, gestoreConsegna, gestoreRitiro):
        self.gestoreConsegna = gestoreConsegna
        self.gestoreRitiro = gestoreRitiro
    
    def backup_consegne_standard_positive(self):
        with open("Dati/BackupConsegneStandardPositive.txt", "w") as f:
            i = 1
            for consegna_standard in self.gestoreConsegna.listaConsegnePositive:
                f.write(f"Consegna standard positiva n. {i}:\n{consegna_standard.getInfoPaccoConsegna()}\n************\n")
                i+=1
        f.close()
    
    def backup_consegne_standard_negative(self):
        with open("Dati/BackupConsegneStandardNegative.txt", "w") as f:
            i = 1
            for consegna_standard in self.gestoreConsegna.listaConsegneNegative:
                f.write(f"Consegna standard negativa n. {i}:\n{consegna_standard.getInfoPaccoConsegna()}\n************\n")
                i+=1
        f.close()

    def backup_consegne_colli_positivi(self):
        with open("Dati/BackupConsegneColliPositivi.txt", "w") as f:
            i = 1
            for collo in self.gestoreConsegna.listaColliPositivi:
                f.write(f"Consegna di collo positiva n.{i}:\n{collo.getInfoColloConsegna()}\n************\n")
                i+=1
        f.close()
    
    def backup_consegne_colli_negativi(self):
        with open("Dati/BackupConsegneColliNegativi.txt", "w") as f:
            i = 1
            for collo in self.gestoreConsegna.listaColliNegativi:
                f.write(f"Consegna di collo negativo n.{i}:\n{collo.getInfoColloConsegna()}\n************\n")
                i+=1
        f.close()

    #####################################################

    def backup_ritiri_standard_positivi(self):
        with open("Dati/BackupRitiriStandardPositivi.txt", "w") as f:
            i = 1
            for ritiri_standard in self.gestoreRitiro.listaRitiriPositivi:
                f.write(f"Ritiro standard positivo n. {i}:\n{ritiri_standard.getInfoPaccoRitiro()}\n************\n")
                i+=1
        f.close()
    
    def backup_ritiri_standard_negativi(self):
        with open("Dati/BackupRitiriStandardNegativi.txt", "w") as f:
            i = 1
            for ritiri_standard in self.gestoreRitiro.listaRitiriNegativi:
                f.write(f"Ritiro standard negativo n. {i}:\n{ritiri_standard.getInfoPaccoRitiro()}\n************\n")
                i+=1
        f.close()

    def backup_ritiri_colli_positivi(self):
        with open("Dati/BackupRitiriColliPositivi.txt", "w") as f:
            i = 1
            for collo in self.gestoreRitiro.listaColliPositivi:
                f.write(f"Ritiro di collo positivo n.{i}:\n{collo.getInfoColloRitiro()}\n************\n")
                i+=1
        f.close()
    
    def backup_ritiri_colli_negativi(self):
        with open("Dati/BackupRitiriColliNegativi.txt", "w") as f:
            i = 1
            for collo in self.gestoreRitiro.listaColliNegativi:
                f.write(f"Ritiro di collo negativo n.{i}:\n{collo.getInfoColloRitiro()}\n************\n")
                i+=1
        f.close()