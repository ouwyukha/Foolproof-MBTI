
from PyQt5 import QtCore, QtGui, QtWidgets

def iconFromBase64(base64):
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(base64))
    icon = QtGui.QIcon(pixmap)
    return icon

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.wantWidth = self.screen.width()/2
        self.wantHeight = self.screen.height()/2
        main.setGeometry(self.wantWidth-self.wantWidth/2, self.wantHeight/2, self.wantWidth, self.wantHeight)  
        main.setWindowIcon(iconFromBase64(ico))
        main.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        main.setStyleSheet("QWidget {background-color : #000000}")
        
        main.setWindowTitle("Foolproof Myers-Briggs Type Indicator")
        self.index = 0
        
        self.mbtiDict = {'E':'Extraversion','S':'Sensing','T':'Thinking','J':'Judgment','I':'Introversion', 'N':'Intuition', 'F':'Feeling', 'P':'Perception', 'None':'None'}
        self.leftLabel =['E','S','T','J','None']
        self.rightLabel =['I','N','F','P','None']
        self.result = []

        self.buttonFont = QtGui.QFont("Consolas", 20, QtGui.QFont.Normal) 
        
        self.leftBtn = QtWidgets.QPushButton(main)
        self.leftBtn.setGeometry(QtCore.QRect(75, self.wantHeight/2, self.wantWidth/3, self.wantWidth/4))
        self.leftBtn.setObjectName("leftBtn")
        self.leftBtn.setFont(self.buttonFont)
        self.leftBtn.setStyleSheet("QPushButton {background-color : rgb(104,33,122);color : #FFFFFF;}QPushButton::hover{background-color : rgb(30,30,30);color : #FFFFFF;}")
        
        self.rightBtn = QtWidgets.QPushButton(main)
        self.rightBtn.setGeometry(QtCore.QRect(self.wantWidth-self.wantWidth/3-75, self.wantHeight/2, self.wantWidth/3, self.wantWidth/4))
        self.rightBtn.setObjectName("rightBtn")
        self.rightBtn.setFont(self.buttonFont)
        self.rightBtn.setStyleSheet("QPushButton {background-color : rgb(104,33,122);color : #FFFFFF;}QPushButton::hover{background-color : rgb(30,30,30);color : #FFFFFF;}")
        
        self.questionLabel = QtWidgets.QLabel(main)
        self.questionLabel.setGeometry(QtCore.QRect(0, self.wantHeight/8, self.wantWidth, 100))
        self.questionLabel.setObjectName("questionLabel")
        self.LabelFont = QtGui.QFont("Consolas", 30, QtGui.QFont.Normal) 
        self.questionLabel.setFont(self.LabelFont)
        self.questionLabel.setStyleSheet("QLabel {color : #FFFFFF;background-color:None}")
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        
        self.retranslateUi([self.mbtiDict[self.leftLabel[self.index]],self.mbtiDict[self.rightLabel[self.index]]])
        QtCore.QMetaObject.connectSlotsByName(main)

        self.leftBtn.clicked.connect(self.leftBtnClicked)
        self.rightBtn.clicked.connect(self.rightBtnClicked)

    def leftBtnClicked(self):
        self.result.append(self.leftLabel[self.index])
        if self.index < 3:
            self.retranslateUi([self.mbtiDict[self.leftLabel[self.index+1]],self.mbtiDict[self.rightLabel[self.index+1]]])
            self.index=self.index+1
        else:
            self.showResult()

    def rightBtnClicked(self):      
        self.result.append(self.rightLabel[self.index])
        if self.index < 3:
            self.retranslateUi([self.mbtiDict[self.leftLabel[self.index+1]],self.mbtiDict[self.rightLabel[self.index+1]]])
            self.index=self.index+1  
        else:
            self.showResult()

    def showResult(self):
        print(self.result)
        self.leftBtn.hide()
        self.rightBtn.hide()
        self.questionLabel.setText("Your Personality is : ")
        
        self.resultLabel = QtWidgets.QLabel(main)
        self.resultLabel.setGeometry(QtCore.QRect(0, 0, self.wantWidth, self.wantHeight))
        self.resultLabel.setObjectName("resultLabel")
        self.subLabelButtonFont = QtGui.QFont("Consolas", 60, QtGui.QFont.Normal) 
        self.resultLabel.setFont(self.subLabelButtonFont)
        self.resultLabel.setStyleSheet("QLabel {color : #FFFFFF;background-color:None}")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.resultLabel.setText(self.result[0]+self.result[1]+self.result[2]+self.result[3])
        self.resultLabel.show()
        

    def retranslateUi(self, code):
        _translate = QtCore.QCoreApplication.translate
        self.leftBtn.setText(_translate("main", code[0]))
        self.questionLabel.setText(_translate("main", code[0]+" OR "+code[1]))
        self.rightBtn.setText(_translate("main", code[1]))


ico=b"iVBORw0KGgoAAAANSUhEUgAAAKAAAACgCAYAAACLz2ctAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsIAAA7CARUoSoAAAAM9SURBVHhe7d2xbSVVGIZhQxekVLEpIT0sNVALARVAD4Sk28ImpETUAFgaCcn6ZQ2au/POnPs8kuWJrVdH99MZ2199+Panv18g8vX2HRICJCVAUgIkJUBSAiQlQFICJCVAUk93E/Lpjx+3p96/P/vt6Xk5AUkJkJQASQmQ1NIjZBocn37/c3t6jA/ffbM9/eeX73/dnt73w28ft6f3rTxWnICkBEhKgKQESGqZEbL3huNKI2QyDRMjBL4QAZISICkBkrrlCDnjhmOvR4+Qyco3Jk5AUgIkJUBSAiR1qRFS3WYcMY2QyaOHyeSOtyhOQFICJCVAUgIkdfkRMn14nz5sP9swWeV2xAlISoCkBEhKgKSyEbJ3cEz2fgC/4zB5NCME3iFAUgIkJUBStxwhk6vfjlSm8XOlYeIEJCVAUgIkJUBSAiQlQFICJCVAUgIkdcpNyBm3HhM3IbMr3Y44AUkJkJQASQmQ1OVHiMHxeEYIbARISoCkBEgqGyFHGByzI7/8boTwlARISoCkBEjq4SNkGhxGw+PtHRxHbpzOGCZOQFICJCVAUgIkJcCFvA6Ot19XJ0BSAiQlQFICJCVAUgIkJUBSAiQlQFKHXsfy6lVneh3r0TcfP3/+a3v6cpyApARISoCkBEhq6REyfVBfZSSdMULO+D0RJyApAZISICkBklpmhBz5y1B7XX1gTY4MEyOE5QmQlABJCZDULUfIkcGx90P5Hf8/yRlDzAhhKQIkJUBSAiS1zAg54y9BPds/Tpx+zkYISxEgKQGSEiApAf4Pr0Pn7RfHCJCUAEkJkJQASS0T4Ostxdsvrs8JSEqApARISoCkDr2ONVn5Fa29w+aOr2Od8erVxAlISoCkBEhKgKSWHiF7TWPF4DiHE5CUAEkJkJQAST18hExW+VO+dxwcEyMENgIkJUBSAiR1ygiZTMNkssoH/8mRQXRENTgmTkBSAiQlQFICJJWNkL2udItyxN7Bsff3WPa+LnalwTFxApISICkBkhIgqcuPkMkdb1GmEXJkcFx9XOzlBCQlQFICJCVAUrccIXvtHStXt8rgmDgBSQmQlABJCZDU0iOE63MCkhIgKQGSEiChl5d/AG2mJMp4S80KAAAAAElFTkSuQmCC"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QDialog()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())