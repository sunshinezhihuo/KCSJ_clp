# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BianLi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import SceneArcPaintBFS

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

class Ui_Form(QtGui.QWidget):
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
        self.label.setIndent(255)
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
        self.prompt.setGeometry(QtCore.QRect(10, 5, 220, 21))
        self.prompt.setText(_fromUtf8(""))
        self.prompt.setObjectName(_fromUtf8("prompt"))
        self.prompt.setText(u"在动画演示窗口双击可以生成新的顶点")
        self.prompt2 = QtGui.QLabel(self.tab)
        self.prompt2.setGeometry(QtCore.QRect(10, 20, 335, 21))
        self.prompt2.setText(_fromUtf8(""))
        self.prompt2.setObjectName(_fromUtf8("prompt"))
        self.prompt2.setText(u"鼠标点住一个顶点，然后移动到另一个顶点再放开就可以生成边")
        self.prompt3 = QtGui.QLabel(self.tab)
        self.prompt3.setGeometry(QtCore.QRect(10, 35, 300, 21))
        self.prompt3.setText(_fromUtf8(""))
        self.prompt3.setObjectName(_fromUtf8("prompt"))
        self.prompt3.setText(u"正在遍历的点背景是绿色的，已加入队列的点的边是红色的")
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tabWidget_2 = QtGui.QTabWidget(Form)
        self.tabWidget_2.setGeometry(QtCore.QRect(430, 70, 361, 231))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 361, 211))
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
        self.StartButton = QtGui.QPushButton(self.groupBox)
        self.StartButton.setGeometry(QtCore.QRect(240, 20, 71, 31))
        self.StartButton.setBaseSize(QtCore.QSize(0, 0))
        self.StartButton.setObjectName(_fromUtf8("StartButton"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Andalus"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.TextData = QtGui.QTextEdit(self.groupBox)
        self.TextData.setGeometry(QtCore.QRect(510, 20, 41, 31))
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(60, 20, 81, 31))
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setBold(True)
        font.setWeight(75)
        self.TextData.setFont(font)
        self.TextData.setObjectName(_fromUtf8("TextData"))
        self.NewsButton = QtGui.QPushButton(self.groupBox)
        self.NewsButton.setGeometry(QtCore.QRect(150, 20, 71, 31))
        self.NewsButton.setStyleSheet(_fromUtf8(""))
        self.NewsButton.setObjectName(_fromUtf8("NewsButton"))
        self.ReturnButton = QtGui.QPushButton(self.groupBox)
        self.ReturnButton.setGeometry(QtCore.QRect(660, 20, 71, 31))
        self.ReturnButton.setStyleSheet(_fromUtf8(""))
        self.ReturnButton.setObjectName(_fromUtf8("ReturnButton"))
        self.tabWidget_3 = QtGui.QTabWidget(Form)
        self.tabWidget_3.setGeometry(QtCore.QRect(430, 320, 361, 151))
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab_3)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 361, 131))
        self.textBrowser_2.setBaseSize(QtCore.QSize(10, 0))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.tabWidget_3.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.scene = SceneArcPaintBFS.SceneArcPaintBFS()
        self.scene.setTextBrowser(self.textBrowser)
        self.scene.setDataBrowser(self.textBrowser_2)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()
        self.scene.setSceneRect(0, 0, 400, 380)
        self.scene.giveNewMatrix(Oriented=False)

        self.timeController = QtCore.QTimeLine(150000)
        self.timeController.setFrameRange(0, 100)
        self.timeController.setCurveShape(QtCore.QTimeLine.LinearCurve)
        self.timeController.frameChanged.connect(self.BFSProcess)

        self.NewsButton.clicked.connect(self.NewGraph)
        self.StartButton.clicked.connect(self.startBFS)

    def startBFS(self):
        Apex = self.TextData.toPlainText()
        self.scene.restartBfs()
        if len(Apex) != 1 :
            message = QtGui.QMessageBox.warning(self, "Warning", u"请输入正确的数据！", QtGui.QMessageBox.Yes, 0)
        else:
            Apex = Apex.at(0).toAscii()
            if ord(Apex) >= ord('A') and ord(Apex) < ord('A')+ self.scene.getDataSize():
                self.process = ['start', 'X', 0]
                self.process[1] = Apex
                """动画效果的准备和启动"""
                self.timeController.start()
            else:
                message = QtGui.QMessageBox.warning(self, "Warning", u"请输入图中存在的顶点！", QtGui.QMessageBox.Yes, 0)

    def NewGraph(self):
        if self.checkBox.isChecked() == True:
            self.scene.giveNewMatrix(Oriented=True)
        else:
            self.scene.giveNewMatrix(Oriented=False)

    def BFSProcess(self):
        self.process = self.scene.BFS(self.process)
        self.scene.rePaint()
        if self.process[0] == 'stop':
            self.timeController.stop()
            message = QtGui.QMessageBox.warning(self, u"完成", u"广度优先遍历完成！", QtGui.QMessageBox.Yes, 0)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "图的广度优先遍历", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "动画演示窗口", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form", "算法演示窗口", None))
        self.groupBox.setTitle(_translate("Form", "控制面板", None))
        self.StartButton.setText(_translate("Form", "开始遍历", None))
        self.label_2.setText(_translate("Form", "输入遍历开始的结点", None))
        self.NewsButton.setText(_translate("Form", "新建图", None))
        self.ReturnButton.setText(_translate("Form", "返回", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("Form", "数据演示窗口", None))
        self.checkBox.setText(_translate("Form", "有向图", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())