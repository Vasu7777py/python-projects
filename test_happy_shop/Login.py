# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(516, 440)
        login.setAutoFillBackground(True)
        self.frame = QtWidgets.QFrame(login)
        self.frame.setGeometry(QtCore.QRect(90, 50, 361, 311))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.frame.setFont(font)
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Login = QtWidgets.QPushButton(self.frame)
        self.Login.setGeometry(QtCore.QRect(130, 160, 101, 31))
        self.Login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Login.setObjectName("Login")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(70, 30, 231, 111))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.username_labe = QtWidgets.QLabel(self.widget)
        self.username_labe.setObjectName("username_labe")
        self.gridLayout.addWidget(self.username_labe, 0, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.password_lable = QtWidgets.QLabel(self.widget)
        self.password_lable.setObjectName("password_lable")
        self.gridLayout.addWidget(self.password_lable, 1, 0, 1, 1)
        self.User_Name = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.User_Name.sizePolicy().hasHeightForWidth())
        self.User_Name.setSizePolicy(sizePolicy)
        self.User_Name.setObjectName("User_Name")
        self.gridLayout.addWidget(self.User_Name, 0, 1, 1, 1)
        self.login_lable = QtWidgets.QLabel(login)
        self.login_lable.setGeometry(QtCore.QRect(200, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_lable.setFont(font)
        self.login_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.login_lable.setWordWrap(False)
        self.login_lable.setObjectName("login_lable")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.Login.setText(_translate("login", "LOGIN"))
        self.username_labe.setText(_translate("login", "User Name"))
        self.password_lable.setText(_translate("login", "Password"))
        self.login_lable.setText(_translate("login", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
