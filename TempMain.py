# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TempMain.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import AdjacencyMatrixInsert,DFS,BFS

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.Form = QtGui.QWidget()
        self.Form_2 = QtGui.QWidget()
        self.Form_3 = QtGui.QWidget()
        self.sonUI = AdjacencyMatrixInsert.AdjacencyMatrixInsert()
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(794, 540)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        MainWindow.connect(self.action, QtCore.SIGNAL("triggered()"), self.openAM)
        MainWindow.connect(self.action_2, QtCore.SIGNAL("triggered()"), self.openDFS)
        MainWindow.connect(self.action_3, QtCore.SIGNAL("triggered()"), self.openBFS)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    @QtCore.pyqtSlot()
    def openAM(self):
        self.sonUI = AdjacencyMatrixInsert.AdjacencyMatrixInsert()
        self.sonUI.setupUi(self.Form)
        self.Form.show()

    @QtCore.pyqtSlot()
    def openDFS(self):
        self.sonUI = DFS.Ui_Form()
        self.sonUI.setupUi(self.Form_2)
        self.Form_2.show()

    @QtCore.pyqtSlot()
    def openBFS(self):
        self.sonUI = BFS.Ui_Form()
        self.sonUI.setupUi(self.Form_3)
        self.Form_3.show()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "临时主窗口", None))
        self.menu.setTitle(_translate("MainWindow", "图的算法", None))
        self.action.setText(_translate("MainWindow", "邻接矩阵", None))
        self.action_2.setText(_translate("MainWindow", "图的深度优先遍历", None))
        self.action_3.setText(_translate("MainWindow", "图的广度优先遍历", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

