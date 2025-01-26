import sys

from PyQt5.QtWidgets import QApplication

from Vista.VistaAccessoCorriere import VistaAccessoCorriere

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_corriere = VistaAccessoCorriere()
    vista_corriere.show()
    sys.exit(app.exec())