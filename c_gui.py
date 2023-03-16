import gui_compiled_template, sys
from PyQt5.QtCore import QDateTime, Qt, QTimer, pyqtSlot
from PyQt5 import QtWidgets

from c_etudiant import etudiant


class Ui(QtWidgets.QMainWindow, gui_compiled_template.Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super(Ui, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Etudiant")

    @pyqtSlot()
    def on_pushButtonAdd_clicked(self):
        prenom = self.lineEditPrenom.text()
        nom = self.lineEdit_Nom.text()
        id = self.lineEdit_ID.text()
        vip = self.checkBoxVIP.isChecked()
        danger = self.checkBoxDanger.isChecked()

        if not all([prenom, nom, id]):
            return

        etudiant_c = etudiant(prenom, nom, id, vip, danger)

        self.plainTextEdit.appendPlainText(str(etudiant_c))

