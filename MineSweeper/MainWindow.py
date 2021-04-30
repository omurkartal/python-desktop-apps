import sys
from PySide2 import QtCore
from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)

class Constants:
    LEVEL_EASY = "Easy"
    LEVEL_MEDIUM  = "Medium"
    LEVEL_HARD  = "Hard"

class DifficultyDialogBox(QDialog):
    selectedLevel = Constants.LEVEL_EASY

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(140,160)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        buttonEasy = QPushButton(Constants.LEVEL_EASY)
        buttonMedium = QPushButton(Constants.LEVEL_MEDIUM)
        buttonHard = QPushButton(Constants.LEVEL_HARD)
        buttonEasy.clicked.connect(self.pbClicked)
        buttonMedium.clicked.connect(self.pbClicked)
        buttonHard.clicked.connect(self.pbClicked)
        
        label = QLabel("Select Difficulty Level")
        label.setAlignment(QtCore.Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(buttonEasy)
        layout.addWidget(buttonMedium)
        layout.addWidget(buttonHard)
        self.setLayout(layout)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(200, 200, 200))
        self.setPalette(palette)
        #self.setAutoFillBackground(True)

    def pbClicked(self):
        self.selectedLevel = self.sender().text()
        self.close()
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mine Sweeper")
        self.setFixedSize(400,400)
        button = QPushButton("Change Difficulty")
        button.clicked.connect(self.openDialogBox)
        self.setCentralWidget(button)

    def openDialogBox(self):
        # If you pass self, the dialog will be centered over the main window as before.
        dialog = DifficultyDialogBox(self)
        dialog.exec_()
        print("self.selectedLevel:"+dialog.selectedLevel)
        if dialog.selectedLevel == Constants.LEVEL_HARD:
            cellNumber = 9
        elif dialog.selectedLevel == Constants.LEVEL_MEDIUM:
            cellNumber = 7
        else:
            cellNumber = 5
        self.createButtonsForNewGame(cellNumber)
    
    def createButtonsForNewGame(self, cellNumber):
        for i in range(0, cellNumber):
            for j in range(0, cellNumber):
                newBtn = QPushButton(str(i), self)
                newBtn.setFixedSize(22,22)
                newBtn.move(i*22, j*22)
                newBtn.clicked.connect(self.pbNewBtn)
                newBtn.show()
    
    def pbNewBtn(self):
        self.sender().setDisabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.openDialogBox()
    app.exec_()