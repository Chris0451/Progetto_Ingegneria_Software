import sys

# from PyQt5.QtWidgets import QApplication

# from Vista.VistaAccessoCorriere import VistaAccessoCorriere
# from Vista.VistaVisualizzaListaRitiri import VistaVisualizzaListaRitiri

from Attivita.LettoreFile import LettoreFile

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # vista_corriere = VistaAccessoCorriere()
    # vista_corriere.show()
    # sys.exit(app.exec())
    
    lettore = LettoreFile()
    pacchiConsegne = lettore.read_consegne()
    print (pacchiConsegne[0].consegna.codiceConsegna)
    pacchiRitiri = lettore.read_ritiri()
    print (pacchiRitiri[0].ritiro.codiceRitiro)
    colliRitiri = lettore.leggi_lista_colli()
    print (colliRitiri[0].aziendaMittente.orarioApertura)
    print(colliRitiri[0].ritiro.codiceRitiro)
    colliConsegne = lettore.leggi_lista_colli_consegne()
    print(colliConsegne[0].consegna.codiceConsegna)
    