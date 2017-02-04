# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lj.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import ScenePaint

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

class AdjacencyMatrixInsert(QtGui.QWidget):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(796, 569)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 731, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gautami"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("#label{border: 1px solid;}"))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(272)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 70, 401, 401))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.graphicsView = QtGui.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 401, 381))
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.prompt = QtGui.QLabel(self.tab)
        self.prompt.setGeometry(QtCore.QRect(10, 20, 220, 21))
        self.prompt.setText(_fromUtf8(""))
        self.prompt.setObjectName(_fromUtf8("prompt"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tabWidget_2 = QtGui.QTabWidget(Form)
        self.tabWidget_2.setGeometry(QtCore.QRect(430, 70, 361, 401))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 361, 381))
        self.textBrowser.setBaseSize(QtCore.QSize(10, 0))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabWidget_2.addTab(self.tab_2, _fromUtf8(""))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 480, 761, 71))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox.setStyleSheet(_fromUtf8("#groupBox{border: 1px solid;}"))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.InsertButton = QtGui.QPushButton(self.groupBox)
        self.InsertButton.setGeometry(QtCore.QRect(240, 20, 71, 31))
        self.InsertButton.setBaseSize(QtCore.QSize(0, 0))
        self.InsertButton.setObjectName(_fromUtf8("InsertButton"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Andalus"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Ap1 = QtGui.QTextEdit(self.groupBox)
        self.Ap1.setGeometry(QtCore.QRect(440, 20, 41, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setBold(True)
        font.setWeight(75)
        self.Ap1.setFont(font)
        self.Ap1.setObjectName(_fromUtf8("Ap1"))
        self.NewsButton = QtGui.QPushButton(self.groupBox)
        self.NewsButton.setGeometry(QtCore.QRect(150, 20, 71, 31))
        self.NewsButton.setStyleSheet(_fromUtf8(""))
        self.NewsButton.setObjectName(_fromUtf8("NewsButton"))
        self.ReturnButton = QtGui.QPushButton(self.groupBox)
        self.ReturnButton.setGeometry(QtCore.QRect(660, 20, 71, 31))
        self.ReturnButton.setStyleSheet(_fromUtf8(""))
        self.ReturnButton.setObjectName(_fromUtf8("ReturnButton"))
        self.Ap2 = QtGui.QTextEdit(self.groupBox)
        self.Ap2.setGeometry(QtCore.QRect(520, 20, 41, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setBold(True)
        font.setWeight(75)
        self.Ap2.setFont(font)
        self.Ap2.setObjectName(_fromUtf8("Ap2"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(490, 20, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Andalus"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(60, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft New Tai Lue"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.scene = ScenePaint.ScenePaint()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()
        self.scene.setSceneRect(0, 0, 400, 380)
        self.scene.giveNewMatrix(Oriented=False, textBrowser=self.textBrowser)
        self.prompt.setText(u"在动画演示窗口双击可以生成新的顶点")

        self.InsertButton.clicked.connect(self.InsertArc)
        self.NewsButton.clicked.connect(self.NewGraph)
        self.connect(self.scene, QtCore.SIGNAL("updateText"), self.updateText)
        self.connect(self.scene, QtCore.SIGNAL("tooManyApex"), self.tooManyApex)

    @QtCore.pyqtSlot()
    def tooManyApex(self):
        message = QtGui.QMessageBox.warning(self, "Warning", u"已经有足够多的顶点了……", QtGui.QMessageBox.Yes, 0)

    @QtCore.pyqtSlot()
    def updateText(self):
        self.scene.updateText(self.textBrowser)

    def NewGraph(self):
        if self.checkBox.isChecked() == True:
            self.scene.giveNewMatrix(Oriented=True, textBrowser=self.textBrowser)
        else:
            self.scene.giveNewMatrix(Oriented=False, textBrowser=self.textBrowser)

    def InsertArc(self):
        Ap1 = self.Ap1.toPlainText()
        Ap2 = self.Ap2.toPlainText()
        if len(Ap1) != 1 or len(Ap2) != 1:
            message = QtGui.QMessageBox.warning(self, "Warning", u"请输入正确长度的顶点！", QtGui.QMessageBox.Yes, 0)
        else:
            Ap1 = Ap1.at(0).toAscii()
            Ap2 = Ap2.at(0).toAscii()
            if (ord(Ap1) >= ord('A') and ord(Ap1) < ord('A')+ self.scene.getDataSize() and
                        ord(Ap2) >= ord('A') and ord(Ap2) < ord('A')+ self.scene.getDataSize()):
                self.scene.addNewArc(Ap1, Ap2, self.textBrowser)
                self.Ap1.setText("")
                self.Ap2.setText("")
            else:
                message = QtGui.QMessageBox.warning(self, "Warning", u"请输入图中存在的顶点！", QtGui.QMessageBox.Yes, 0)




    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "邻接矩阵的插入", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "动画演示窗口", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form", "邻接矩阵窗口", None))
        self.groupBox.setTitle(_translate("Form", "控制面板", None))
        self.InsertButton.setText(_translate("Form", "插入弧", None))
        self.label_2.setText(_translate("Form", "输入弧的顶点", None))
        self.NewsButton.setText(_translate("Form", "新建图", None))
        self.ReturnButton.setText(_translate("Form", "返回", None))
        self.label_4.setText(_translate("Form", "→", None))
        self.checkBox.setText(_translate("Form", "有向图", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = AdjacencyMatrixInsert()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

