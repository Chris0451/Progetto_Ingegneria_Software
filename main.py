import sys

from PyQt5.QtWidgets import QApplication

from Vista.VistaAccessoCorriere import VistaAccessoCorriere
from Gestione.GestoreConsegna import GestoreConsegna
from Gestione.GestoreRitiro import GestoreRitiro

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestoreConsegna = GestoreConsegna()
    gestoreRitiro = GestoreRitiro()
    vista_corriere = VistaAccessoCorriere(gestoreConsegna, gestoreRitiro)
    vista_corriere.show()
    sys.exit(app.exec())