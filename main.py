import sys
from PyQt5 import QtWidgets

from c_etudiant import etudiant
from c_gui import Ui



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = Ui()
    form.show()
    app.exec()
