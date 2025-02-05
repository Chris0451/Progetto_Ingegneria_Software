from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QApplication
import sys

class FinestraRitiri(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selezione Liste")
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Visualizzazione Lista Ritiri", self)
        layout.addWidget(self.label)
        
        self.lista_ritiri_standard = QPushButton("Lista Ritiri Standard", self)
        self.ritiri_positivi = QPushButton("Ritiri Positivi", self)
        self.ritiri_rimandati = QPushButton("Ritiri Rimandati", self)
        self.lista_colli = QPushButton("Lista Colli", self)
        self.colli_ritirati = QPushButton("Colli Ritirati", self)
        self.colli_rimandati = QPushButton("Colli Rimandati", self)
        
        for button in [self.lista_ritiri_standard, self.ritiri_positivi, self.ritiri_rimandati,
                       self.lista_colli, self.colli_ritirati, self.colli_rimandati]:
            layout.addWidget(button)
        
        self.setLayout(layout)

class VistaRitiri(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finestra Corriere")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Premi per visualizzare i ritiri", self)
        layout.addWidget(self.label)
        
        self.btn_visualizza = QPushButton("Visualizza Lista Ritiri", self)
        self.btn_visualizza.clicked.connect(self.apri_finestra_ritiri)
        layout.addWidget(self.btn_visualizza)
        
        self.setLayout(layout)
    
    def apri_finestra_ritiri(self):
        self.finestra_ritiri = FinestraRitiri()
        self.finestra_ritiri.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    finestra = VistaRitiri()
    finestra.show()
    sys.exit(app.exec_())
