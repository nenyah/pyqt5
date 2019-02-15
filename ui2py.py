# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo003.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 100, 54, 12))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menusub_menu = QtWidgets.QMenu(self.menu)
        self.menusub_menu.setObjectName("menusub_menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew_file = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("File.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionnew_file.setIcon(icon)
        self.actionnew_file.setObjectName("actionnew_file")
        self.actionquit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionquit.setIcon(icon1)
        self.actionquit.setObjectName("actionquit")
        self.actionitem1 = QtWidgets.QAction(MainWindow)
        self.actionitem1.setObjectName("actionitem1")
        self.actionitem2 = QtWidgets.QAction(MainWindow)
        self.actionitem2.setObjectName("actionitem2")
        self.menusub_menu.addAction(self.actionitem1)
        self.menusub_menu.addAction(self.actionitem2)
        self.menu.addAction(self.actionnew_file)
        self.menu.addAction(self.actionquit)
        self.menu.addAction(self.menusub_menu.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.actionquit.triggered.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.edit_label)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def edit_label(self):
        self.label.setText('Nenyah')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python GUI 学习"))
        MainWindow.setStatusTip(_translate("MainWindow", "这里是状态栏文本"))
        self.label.setText(_translate("MainWindow", "我在这里"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menusub_menu.setTitle(_translate("MainWindow", "子菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "修改"))
        self.actionnew_file.setText(_translate("MainWindow", "新文件"))
        self.actionnew_file.setStatusTip(_translate("MainWindow", "创建新文件"))
        self.actionquit.setText(_translate("MainWindow", "退出"))
        self.actionquit.setStatusTip(_translate("MainWindow", "点击退出应用程序"))
        self.actionquit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionitem1.setText(_translate("MainWindow", "项目1"))
        self.actionitem2.setText(_translate("MainWindow", "项目2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())