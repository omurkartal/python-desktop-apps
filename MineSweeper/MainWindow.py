import sys
import numpy as np
import random
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPalette, QTextFrame
from PyQt5.QtWidgets import QDialog, QFrame, QGroupBox, QLabel, QMainWindow, QMessageBox, QVBoxLayout, QWidget, QPushButton,QHBoxLayout, QGridLayout, QApplication

class Constants:
    NEW_GAME = "new-game"
    LEVEL_EASY = "Easy"
    LEVEL_EASY_COUNT = 4
    LEVEL_MEDIUM  = "Medium"
    LEVEL_MEDIUM_COUNT  = 15
    LEVEL_HARD  = "Hard"
    LEVEL_HARD_COUNT  = 30
    MINE_INDICATOR = "X"
    MINE_SUSPICION = "?"
    NO_MINE_TEXT = ""

class DifficultyDialogBox(QDialog):
    selectedLevel = ""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(130,120)
        self.setWindowTitle("Select Difficulty Level")
        self.setWindowFlag(QtCore.Qt.SubWindow)
        
        buttonEasy = QPushButton(Constants.LEVEL_EASY)
        buttonMedium = QPushButton(Constants.LEVEL_MEDIUM)
        buttonHard = QPushButton(Constants.LEVEL_HARD)
        buttonEasy.clicked.connect(self.pbClicked)
        buttonMedium.clicked.connect(self.pbClicked)
        buttonHard.clicked.connect(self.pbClicked)

        layout = QVBoxLayout()
        layout.addWidget(buttonEasy)
        layout.addWidget(buttonMedium)
        layout.addWidget(buttonHard)
        self.setLayout(layout)
        
        palette = self.palette()
        #palette.setColor(QPalette.Window, QColor(20, 200, 200))
        palette.setColor(QPalette.Window, QtCore.Qt.lightGray)
        self.setPalette(palette)

    def pbClicked(self):
        self.selectedLevel = self.sender().text()
        self.close()

class GameResultDialogBox(QDialog):
    responseText = ""

    def __init__(self, totalGameCount, gamesWonCount):
        super().__init__()
        self.setFixedSize(128,100)
        
        self.setWindowTitle("Statistics")
        self.setWindowFlag(QtCore.Qt.SubWindow)
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        buttonNewGame = QPushButton("New Game")
        buttonNewGame.clicked.connect(self.pbClicked)
        
        labelTotalGameCount = QLabel("Games played:" + str(totalGameCount))
        labelTotalGameCount.setAlignment(QtCore.Qt.AlignCenter)

        labelWonGameCount = QLabel("Games won:" + str(gamesWonCount))
        labelWonGameCount.setAlignment(QtCore.Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(buttonNewGame)
        layout.addWidget(labelTotalGameCount)
        layout.addWidget(labelWonGameCount)
        self.setLayout(layout)
        
        palette = self.palette()
        #palette.setColor(QPalette.Window, QColor(20, 200, 200))
        palette.setColor(QPalette.Window, QtCore.Qt.lightGray)
        self.setPalette(palette)

    def pbClicked(self):
        self.responseText = Constants.NEW_GAME
        self.close()

class MineQPushButton(QPushButton):
    hiddenValue = Constants.NO_MINE_TEXT
    posX = 0
    posY = 0
    isActive = True
    rightClicked = QtCore.pyqtSignal()

    def __init__(self, text, hiddenText, positionX, positionY, parent = None):
        super(MineQPushButton, self).__init__()
        if hiddenText=="0":
            self.hiddenValue=Constants.NO_MINE_TEXT
        else:
            self.hiddenValue=hiddenText
        self.posX = positionX
        self.posY = positionY
        self.isActive = True
        self.setFixedSize(24,24)
        self.setText(text)
        self.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red; "
                             "}"
                             "QPushButton::disabled"
                             "{"
                              "background-color: white; color: #0000FF; border-style: outset; padding: 2px;"
                             "}"
                            )

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        # To set the signal for the right click
        if event.button()==QtCore.Qt.RightButton:
            self.rightClicked.emit()

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.cellNumber = 0
        self.minesFound = 0
        self.mineSweeper = MineSweeper()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mine Sweeper")
        self.setFixedSize(800, 800)
        self.layout = QGridLayout()
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)
        self.show()
        self.openDifficultyDialogBox()

    def openDifficultyDialogBox(self):
        if self.layout.itemAt(0) != None:
            self.layout.itemAt(0).widget().deleteLater()
        # If you pass self, the dialog will be centered over the main window as before.
        dialog = DifficultyDialogBox(self)
        dialog.exec_()
        print("self.selectedLevel: " + dialog.selectedLevel)
        if dialog.selectedLevel == Constants.LEVEL_EASY:
            self.cellNumber = Constants.LEVEL_EASY_COUNT
        elif dialog.selectedLevel == Constants.LEVEL_MEDIUM:
            self.cellNumber = Constants.LEVEL_MEDIUM_COUNT
        elif dialog.selectedLevel == Constants.LEVEL_HARD:
            self.cellNumber = Constants.LEVEL_HARD_COUNT
        else:
            self.cellNumber = 0
            self.addNewGameButton()

        if self.cellNumber > 0:
            self.startNewGame()

    def addNewGameButton(self):
        self.clearButtonsFromLayout()
        button = QPushButton("Change Difficulty")
        button.clicked.connect(self.openDifficultyDialogBox)
        self.layout.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.layout.addWidget(button, 0, 0)

    def startNewGame(self):
        self.minesFound = 0
        self.mineSweeper.startNewGame(self.cellNumber)
        self.clearButtonsFromLayout()
        self.layout.setSpacing(1)
        self.layout.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        for i in range(0, self.cellNumber):
            for j in range(0, self.cellNumber):
                button = MineQPushButton(Constants.NO_MINE_TEXT, self.mineSweeper.matrix[i][j], i, j)
                button.clicked.connect(self.mineButtonClicked)
                button.rightClicked.connect(self.mineRightButtonClicked)
                self.layout.addWidget(button, i, j)

    def mineButtonClicked(self):
        if self.sender().text() == Constants.MINE_SUSPICION:
            return
        self.sender().setDisabled(True)
        if Constants.MINE_INDICATOR in self.sender().hiddenValue:
            self.endTheGame(False)
        elif self.sender().hiddenValue == Constants.NO_MINE_TEXT:
            self.cleanCellsHaveNoMineNeighbor(self.sender().posX, self.sender().posY)
        else:
            self.sender().setText(self.sender().hiddenValue)

    def mineRightButtonClicked(self):
        button = self.sender()
        if button.text() == Constants.NO_MINE_TEXT:
            button.setText(Constants.MINE_SUSPICION)
            if button.hiddenValue == Constants.MINE_INDICATOR:
                self.minesFound += 1
        else:
            button.setText(Constants.NO_MINE_TEXT)
            if button.hiddenValue == Constants.MINE_INDICATOR:
                self.minesFound -= 1
        print("self.minesFound:" + str(self.minesFound))
        if self.minesFound == self.cellNumber:
            self.endTheGame(True)

    def cleanCellsHaveNoMineNeighbor(self,i,j):
        neighborList = []
        for x in (i-1, i, i+1):
            for y in (j-1, j, j+1):
                if (x >= 0) and (x < self.cellNumber) and (y >= 0) and (y < self.cellNumber) and ((x!=i) or (y!=j)):
                    #print("["+str(i)+", "+str(j)+"] --> ["+str(x)+", "+str(y)+"]:")
                    button=self.layout.itemAt(x*self.cellNumber+y).widget()
                    if (button.hiddenValue == Constants.NO_MINE_TEXT) and (button.isActive):
                        neighborList.append([x, y])
                    button.setText(button.hiddenValue)
                    button.setDisabled(True)
                    button.isActive=False
        for item in neighborList:
            self.cleanCellsHaveNoMineNeighbor(item[0],item[1])

    def endTheGame(self, isSucceeded):
        if isSucceeded:
            print("Succeeded :)")
            self.mineSweeper.gamesWonCount += 1
        else:
            print("Failed :(")
        for i in range(0, self.cellNumber):
            for j in range(0, self.cellNumber):
                button=self.layout.itemAt(i*self.cellNumber+j).widget()
                if(button.hiddenValue==Constants.MINE_INDICATOR):
                    button.setDisabled(True)
                    button.setText(button.hiddenValue)
        dialog = GameResultDialogBox(self.mineSweeper.gamesPlayedCount, self.mineSweeper.gamesWonCount)
        dialog.exec_()
        print("dialog.responseText:"+dialog.responseText)
        if dialog.responseText == Constants.NEW_GAME:
            self.openDifficultyDialogBox()
        else:
            self.addNewGameButton()

    def clearButtonsFromLayout(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)

class MineSweeper:
    gamesPlayedCount = 0
    gamesWonCount = 0
    cellNumber = 0
    matrix = np.zeros((1, 1))

    def __init__(self):
        super().__init__()

    def startNewGame(self, cellNumber):
        self.cellNumber=cellNumber
        self.gamesPlayedCount += 1
        self.matrix = np.full((self.cellNumber, self.cellNumber), "0", dtype=np.str0)
        mines = random.sample(range(self.cellNumber * self.cellNumber), self.cellNumber)
        for i in range(0, len(mines)):
            division = mines[i] // self.cellNumber
            remainder = mines[i] % self.cellNumber
            self.matrix[division][remainder] = Constants.MINE_INDICATOR
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