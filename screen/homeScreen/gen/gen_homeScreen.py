from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UIHomeScreen(object):
    def setupUi(self, UIHomeScreen):
        UIHomeScreen.setObjectName("UIHomeScreen")
        UIHomeScreen.setEnabled(True)
        UIHomeScreen.resize(1016, 591)
        self.pill_channel_btn_4 = QtWidgets.QPushButton(UIHomeScreen)
        self.pill_channel_btn_4.setGeometry(QtCore.QRect(0, 400, 340, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pill_channel_btn_4.setFont(font)
        self.pill_channel_btn_4.setStyleSheet("background-color: #F8F37D")
        self.pill_channel_btn_4.setObjectName("pill_channel_btn_4")
        self.pill_channel_btn_5 = QtWidgets.QPushButton(UIHomeScreen)
        self.pill_channel_btn_5.setGeometry(QtCore.QRect(340, 400, 340, 200))
        self.pill_channel_btn_5.setStyleSheet("")
        self.pill_channel_btn_5.setText("")
        self.pill_channel_btn_5.setObjectName("pill_channel_btn_5")
        self.pill_channel_btn_2 = QtWidgets.QPushButton(UIHomeScreen)
        self.pill_channel_btn_2.setGeometry(QtCore.QRect(0, 200, 510, 200))
        self.pill_channel_btn_2.setStyleSheet("")
        self.pill_channel_btn_2.setText("")
        self.pill_channel_btn_2.setObjectName("pill_channel_btn_2")
        self.pill_channel_btn_6 = QtWidgets.QPushButton(UIHomeScreen)
        self.pill_channel_btn_6.setGeometry(QtCore.QRect(680, 400, 340, 200))
        self.pill_channel_btn_6.setStyleSheet("")
        self.pill_channel_btn_6.setText("")
        self.pill_channel_btn_6.setObjectName("pill_channel_btn_6")
        self.pill_channel_btn_1 = QtWidgets.QPushButton(UIHomeScreen)
        self.pill_channel_btn_1.setGeometry(QtCore.QRect(510, 0, 510, 200))
        self.pill_channel_btn_1.setStyleSheet("background-color: #F8F37D")
        self.pill_channel_btn_1.setText("")
        self.pill_channel_btn_1.setObjectName("pill_channel_btn_1")
        self.pill_channel_btn_3 = QtWidgets.QPushButton(UIHomeScreen)
        self.pill_channel_btn_3.setGeometry(QtCore.QRect(510, 200, 510, 200))
        self.pill_channel_btn_3.setStyleSheet("")
        self.pill_channel_btn_3.setText("")
        self.pill_channel_btn_3.setObjectName("pill_channel_btn_3")
        self.pill_channel_btn_0 = QtWidgets.QPushButton(UIHomeScreen)
        self.pill_channel_btn_0.setGeometry(QtCore.QRect(0, 0, 510, 200))
        self.pill_channel_btn_0.setStyleSheet("")
        self.pill_channel_btn_0.setText("")
        self.pill_channel_btn_0.setObjectName("pill_channel_btn_0")

        self.retranslateUi(UIHomeScreen)
        QtCore.QMetaObject.connectSlotsByName(UIHomeScreen)

    def retranslateUi(self, UIHomeScreen):
        _translate = QtCore.QCoreApplication.translate
        UIHomeScreen.setWindowTitle(_translate("UIHomeScreen", "Dialog"))
        self.pill_channel_btn_4.setText(_translate("UIHomeScreen", "ช่องที่ 5 \n"
" พาราเซตามอล"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UIHomeScreen = QtWidgets.QDialog()
    ui = Ui_UIHomeScreen()
    ui.setupUi(UIHomeScreen)
    UIHomeScreen.show()
    sys.exit(app.exec_())
