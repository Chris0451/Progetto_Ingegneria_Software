import sys

from PyQt5.QtWidgets import QApplication

from Vista.VistaAccessoCorriere import VistaAccessoCorriere
from Gestione.GestoreConsegna import GestoreConsegna
from Gestione.GestoreRitiro import GestoreRitiro
from Utenti.Corriere import Corriere

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestoreConsegna = GestoreConsegna()
    gestoreRitiro = GestoreRitiro()
    corriere = Corriere("Cristian", "Di Cintio", "CF", "32432432", "corriere@email.com", "CDM1","80100")
    vista_corriere = VistaAccessoCorriere(gestoreConsegna, gestoreRitiro, corriere)
    vista_corriere.show()
    sys.exit(app.exec())