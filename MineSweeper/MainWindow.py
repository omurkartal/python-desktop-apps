import sys
import numpy as np
import random
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QDialog, QLabel, QMessageBox, QVBoxLayout, QWidget, QPushButton,QHBoxLayout, QGridLayout, QApplication

class Constants:
    LEVEL_EASY = "Easy"
    LEVEL_MEDIUM  = "Medium"
    LEVEL_HARD  = "Hard"
    MINE_INDICATOR = "X"
    NEW_GAME = "new-game"

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
        #palette.setColor(QPalette.Window, QColor(20, 200, 200))
        palette.setColor(QPalette.Window, QtCore.Qt.yellow)
        self.setPalette(palette)

    def pbClicked(self):
        self.selectedLevel = self.sender().text()
        self.close()

class GameResultDialogBox(QDialog):
    responseText = ""

    def __init__(self, totalGameCount, wonGameCount):
        super().__init__()
        self.setFixedSize(120,140)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        buttonNewGame = QPushButton("New Game")
        buttonNewGame.clicked.connect(self.pbClicked)
        
        labelTotalGameCount = QLabel("Game Count:" + str(totalGameCount))
        labelTotalGameCount.setAlignment(QtCore.Qt.AlignCenter)

        labelWonGameCount = QLabel("Won Count:" + str(wonGameCount))
        labelWonGameCount.setAlignment(QtCore.Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(labelTotalGameCount)
        layout.addWidget(labelWonGameCount)
        layout.addWidget(buttonNewGame)
        self.setLayout(layout)
        
        palette = self.palette()
        #palette.setColor(QPalette.Window, QColor(20, 200, 200))
        palette.setColor(QPalette.Window, QtCore.Qt.yellow)
        self.setPalette(palette)

    def pbClicked(self):
        self.responseText = Constants.NEW_GAME
        self.close()

class MineQPushButton(QPushButton,object):
    hiddenValue = ""
    def __init__(self, text, hiddenText, parent = None):
        super(MineQPushButton, self).__init__()
        self.hiddenValue=hiddenText
        self.setText(text)

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.cellNumber = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mine Sweeper")
        self.setFixedSize(400,400)
        button = QPushButton("Change Difficulty")
        button.clicked.connect(self.openDialogBox)
        self.layout = QGridLayout()
        self.layout.addWidget(button, 0, 0)
        self.setLayout(self.layout)
        self.mineSweeper = MineSweeper(self.cellNumber)
        self.show()
        self.openDialogBox()

    def openDialogBox(self):
        # If you pass self, the dialog will be centered over the main window as before.
        dialog = DifficultyDialogBox(self)
        dialog.exec_()
        print("self.selectedLevel: " + dialog.selectedLevel)
        if dialog.selectedLevel == Constants.LEVEL_HARD:
            self.cellNumber = 9
        elif dialog.selectedLevel == Constants.LEVEL_MEDIUM:
            self.cellNumber = 7
        else:
            self.cellNumber = 3
        self.startNewGame()

    def startNewGame(self):
        self.remainingButton = (self.cellNumber * self.cellNumber) - self.cellNumber
        print("self.remainingButton:"+str(self.remainingButton))
        self.mineSweeper.startNewGame(self.cellNumber)

        self.layout.itemAt(0).widget().deleteLater()
        for i in range(0, self.cellNumber):
            for j in range(0, self.cellNumber):
                self.button = MineQPushButton("", self.mineSweeper.matrix[i][j])
                self.button.clicked.connect(self.mineButtonClicked)
                self.layout.addWidget(self.button, i, j+1)

    def mineButtonClicked(self):
        self.remainingButton -= 1
        self.sender().setDisabled(True)
        self.sender().setText(self.sender().hiddenValue)
        if Constants.MINE_INDICATOR in self.sender().hiddenValue:
            self.endTheGame(False)
        elif self.remainingButton==0:
            self.endTheGame(True)

    def endTheGame(self, isSucceeded):
        if isSucceeded:
            print("Succeeded :)")
            self.mineSweeper.wonGameCount += 1
        else:
            print("Failed :(")

        for i in range(0, self.cellNumber):
            for j in range(0, self.cellNumber):
                button=self.layout.itemAt(i*self.cellNumber+j).widget()
                button.setText(button.hiddenValue)
                button.deleteLater()

        dialog = GameResultDialogBox(self.mineSweeper.totalGameCount, self.mineSweeper.wonGameCount)
        dialog.exec_()
        print("dialog.responseText:"+dialog.responseText)
        if dialog.responseText == Constants.NEW_GAME:
            self.openDialogBox()

class MineSweeper(np.int8):
    totalGameCount = 0
    wonGameCount = 0
    cellNumber = 0
    matrix = np.zeros((1, 1))

    def __init__(self, cellNumber):
        super().__init__()

    def startNewGame(self, cellNumber):
        self.cellNumber=cellNumber
        self.totalGameCount += 1
        self.matrix = np.full((self.cellNumber, self.cellNumber), "0", dtype=np.str0)
        #print(self.matrix)
        mines = random.sample(range(self.cellNumber * self.cellNumber), self.cellNumber)
        for i in range(0, len(mines)):
            division = mines[i] // self.cellNumber
            remainder = mines[i] % self.cellNumber
            self.matrix[division][remainder] = Constants.MINE_INDICATOR
        #print(self.matrix)
        self.markMineFields()
        print(self.matrix)

    def markMineFields(self):
        for i in range(0, self.cellNumber):
            for j in range(0, self.cellNumber):
                if self.matrix[i][j] == Constants.MINE_INDICATOR:
                    for x in (i-1, i, i+1):
                        for y in (j-1, j, j+1):
                            if (x >= 0) and (x < self.cellNumber) and (y >= 0) and (y < self.cellNumber) and ((x!=i) or (y!=j)):
                                #print("["+str(i)+", "+str(j)+"] --> ["+str(a)+", "+str(b)+"]:"+self.matrix[a][b])
                                if self.matrix[x][y] != Constants.MINE_INDICATOR:
                                    self.matrix[x][y] = str(int(self.matrix[x][y])+1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())