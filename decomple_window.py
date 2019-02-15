import nullwindow
from PyQt5 import QtCore, QtWidgets, QtGui


def set_table_item(item1='数据1', item2='数据2', item3='数据3'):
    ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(item1))
    ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(item2))
    ui.tableWidget.setItem(2, 2, QtWidgets.QTableWidgetItem(item3))


def button_clicked():
    ui.pushButton.setText("按钮被点击")
    set_table_item(item2='数据2被改变')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = nullwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)

    # 调用函数
    set_table_item()
    ui.pushButton.clicked.connect(button_clicked)
    MainWindow.show()
    sys.exit(app.exec_())
