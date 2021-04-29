import sys
import platform
from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from Calculator import Calculator, Constants
from ui_calculator import Ui_Calculator

class Window(QMainWindow):
    def __init__(self):
        print('System/Version: ' + platform.system() + '/' +platform.release())
        super().__init__()
        #self.setWindowIcon(QIcon('calculator.png'))
        self.calculator = Calculator()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.setWindowTitle('** Calculator **')
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        #self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)
        self.show()

    def keyPressEvent(self, event):
        #print('Key: ' + str(event.key()) + ' | Text Press: ' + event.text())
        if event.text() in ['0','1','2','3','4','5','6','7','8','9']:
            formula = self.calculator.addNumber(event.text())
            self.ui.label.setText(formula)
        elif self.calculator.isOperator(event.text()):
            formula = self.calculator.addOperator(event.text())
            self.ui.label.setText(formula)
        elif event.text() in ['.',',']:
            formula = self.calculator.addDecimalSeparator(Constants.DECIMAL_SEPARATOR)
            self.ui.label.setText(formula)
        elif event.key() == 16777223 or event.key() == 16777219:
            self.pbDeleteClicked()
        elif event.key() == 16777221:
            self.pbExecuteClicked()
        elif event.key() == 16777216:
            self.pbClearClicked()

    def pbNumberClicked(self):
        formula = self.calculator.addNumber(self.sender().text())
        self.ui.label.setText(formula)

    def pbOperationClicked(self):
        formula = self.calculator.addOperator(self.sender().text())
        self.ui.label.setText(formula)

    def pbDecimalSeparatorClicked(self):
        formula = self.calculator.addDecimalSeparator(self.sender().text())
        self.ui.label.setText(formula)

    def pbDeleteClicked(self):
        formula = self.calculator.removeItem()
        self.ui.label.setText(formula)

    def pbExecuteClicked(self):
        result = self.calculator.executeFormula()
        self.ui.label.setText(str(result))

    def pbClearClicked(self):
        self.calculator.initInstanceVariables()
        self.ui.label.setText('')
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(window.size())
    sys.exit(app.exec_())