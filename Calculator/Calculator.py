class Calculator():
    itemList = []
    isLastItemOperator = False

    def __init__(self) -> None:
        pass

    def initInstanceVariables(self):
        self.itemList = []
        self.isLastItemOperator = False

    def printInstanceVariables(self):
        print("isLastItemOperator:" + str(self.isLastItemOperator) + "-->" + str(self.itemList))

    def printMyList(self):
        #method-1
        #outputText = ""
        #for i in range(0, len(self.itemList)):
        #    outputText = outputText + self.itemList[i]
        #return outputText
        #method-2
        return ''.join(map(str, self.itemList))

    def executeFormula(self):
        if len(self.itemList) > 0:
            formulaText = self.printMyList()
            result = eval(formulaText)
            result = round(result, 5)
            self.initInstanceVariables()
            return (formulaText + " = " + str(result))
        else:
            return "0"

    def addNumber(self, item):
        self.itemList.append(item)
        self.isLastItemOperator=False
        return self.printMyList()

    def addOperator(self, item):
        if not self.isOperator(item):
            print('Input parameter is not valid! Only operator can be passed to method. Item:' + item)
            return self.printMyList()
        if len(self.itemList) < 1:
            print('First item cannot be operator!')
        else:
            if self.isLastItemOperator:
                print('Operators are passed in a row. Last one is used!')
                self.itemList[-1]=item
            else:
                self.itemList.append(item)
        self.isLastItemOperator=True
        self.printInstanceVariables()
        return self.printMyList()

    def addDecimalSeparator(self, item):
        if item != Constants.DECIMAL_SEPARATOR: 
            print('Input parameter is not valid! Only decimal separator can be passed to method. Item:' + item)
            return self.printMyList()
        if len(self.itemList) < 1:
            print('First item cannot be decimal separator!')
        else:
            result = self.getLastNumber().find(Constants.DECIMAL_SEPARATOR)
            if result < 0:
                self.itemList.append(item)
            else:
                print("There is a decimal separator in the last number. New decimal separator will not be added!")
        self.isLastItemOperator=False
        self.printInstanceVariables()
        return self.printMyList()

    def removeItem(self):
        if len(self.itemList) < 1: return ""
        del self.itemList[-1]
        if len(self.itemList) < 1: return ""

        if self.isOperator(self.itemList[-1]):
            self.isLastItemOperator=True
        else:
            self.isLastItemOperator=False

        self.printInstanceVariables()
        return self.printMyList()

    def getLastNumber(self):
        i = len(self.itemList) - 1
        while i >= 0:
            if self.isOperator(self.itemList[i]): break
            i = i-1
        new_list = self.itemList[(i+1):]
        lastNumberText = ''.join(map(str, new_list))
        print("lastNumberText: " + lastNumberText)
        return lastNumberText

    def isOperator(self, input):
        if input in ['/', '*', '-', '+']:
            return True
        return False

class Constants:
    DECIMAL_SEPARATOR = "."
    DELETE_OPERATION  = "Del"
