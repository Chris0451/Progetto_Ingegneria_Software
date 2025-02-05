import sys

from PyQt5.QtWidgets import QApplication

from Vista.VistaAccessoCorriere import VistaAccessoCorriere
from Gestione.GestoreConsegna import GestoreConsegna
from Gestione.GestoreRitiro import GestoreRitiro

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_corriere = VistaAccessoCorriere(GestoreConsegna(), GestoreRitiro())
    vista_corriere.show()
    sys.exit(app.exec())