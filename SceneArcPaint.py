# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import ScenePaint
import GraphData
import MatrixText

class SceneArcPaint(ScenePaint.ScenePaint):
    def __init__(self):
        ScenePaint.ScenePaint.__init__(self)
        self.textBrowser = QtGui.QTextBrowser()
        self.dataBrowser = QtGui.QTextBrowser()
        self.Ap1 = 'X'
        self.Ap2 = 'X'

    def setTextBrowser(self, textBrowser):
        self.textBrowser = textBrowser

    def setDataBrowser(self, dataBrowser):
        self.dataBrowser = dataBrowser

    def restartDfs(self):
        self.Data.restartDFS()
        self.Text.updateDFSDataText(self.dataBrowser, self.Data)


    def paintEll(self):
        for i in range(0, self.Data.getSize()):
            ellipse = self.addEllipse(self.Data.getCoordinates(i)[0]-10, self.Data.getCoordinates(i)[1]-10, 20, 20)
            Text = self.addText(self.Data.getApex(i))
            Text.setPos(self.Data.getCoordinates(i)[0]-6, self.Data.getCoordinates(i)[1]-11)
            if self.Data.getVisited(i) == 1:
                ellipse.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0, 240)))
                Text.setDefaultTextColor(QtGui.QColor(255, 0, 0, 240))
            if self.Data.getApex(i) == self.Data.getTargetApex():
                ellipse.setBrush(QtGui.QBrush(QtGui.QColor(0, 255, 50, 240)))

    def giveNewMatrix(self, Oriented):
        self.Data = GraphData.GraphData()
        self.clear()
        self.paintEll()
        self.Text.initDFSText(self.textBrowser)
        if Oriented == True:
            self.Data.setOriented(True)
        self.Text.updateDFSDataText(self.dataBrowser, self.Data)

    def mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent):
        print QGraphicsSceneMouseEvent.lastScenePos().x()
        print QGraphicsSceneMouseEvent.lastScenePos().y()
        if self.Data.getSize() >= 14:
            self.emit(QtCore.SIGNAL("tooManyApex"))
        elif self.Data.checkApex(QGraphicsSceneMouseEvent.lastScenePos().x(), QGraphicsSceneMouseEvent.lastScenePos().y(), 25) != 'X':
            print self.Data.checkApex(QGraphicsSceneMouseEvent.lastScenePos().x(), QGraphicsSceneMouseEvent.lastScenePos().y(), 25)
        else:
            self.Data.addnewApex(QGraphicsSceneMouseEvent.lastScenePos().x(), QGraphicsSceneMouseEvent.lastScenePos().y())
            self.clear()
            self.paintEll()
            self.paintLine()
            self.Text.updateDFSDataText(self.dataBrowser, self.Data)

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        self.Ap1 = self.Data.checkApex(QGraphicsSceneMouseEvent.lastScenePos().x(),
                                  QGraphicsSceneMouseEvent.lastScenePos().y(), 10)

    def mouseReleaseEvent(self, QGraphicsSceneMouseEvent):
        self.Ap2 = self.Data.checkApex(QGraphicsSceneMouseEvent.lastScenePos().x(),
                                  QGraphicsSceneMouseEvent.lastScenePos().y(), 10)
        if self.Ap1 != 'X' and self.Ap2 != 'X' and self.Ap1 != self.Ap2:
            if self.Data.getOriented() == False:
                self.Data.setnewArc(self.Ap1, self.Ap2)
                self.Data.setnewArc(self.Ap2, self.Ap1)
            else:
                self.Data.setnewArc(Ap1=self.Ap1, Ap2=self.Ap2)
            self.clear()
            self.paintEll()
            self.paintLine()
        self.Ap1 = 'X'
        self.Ap2 = 'X'

    def rePaint(self):
        self.clear()
        self.paintEll()
        self.paintLine()
        self.Text.updateDFSDataText(self.dataBrowser, self.Data)

    def DFS(self, process):
        if process[0] == 'start':
            self.Data.setTargetApex(process[1])
            self.Text.selectTextCol(0, self.textBrowser, u"从顶点"+process[1]+u"进行深度优先遍历")
            process[0] = 'visit'
            self.rePaint()
            return process
        elif process[0] == 'visit':
            self.Text.selectTextCol(2, self.textBrowser, u"将顶点"+process[1]+u"的访问数组置为1")
            self.Data.setVisited(process[1])
            process[0] = 'cout'
            self.rePaint()
            return process
        elif process[0] == 'cout':
            self.Text.selectTextCol(3, self.textBrowser, u"已访问结点"+process[1])
            self.Data.addVisitedApex(process[1])
            process[0] = 'check'
            self.rePaint()
            return process
        elif process[0] == 'check':
            if process[2] < self.Data.getSize():
                for i in range(process[2], self.Data.getSize()):
                    if self.Data.getArc(ord(process[1]) - ord('A'), i) == 1:
                        self.Text.selectTextCol(4, self.textBrowser, u"结点" + process[1] + u"到结点" + chr(ord('A') +i) + u"存在弧")
                        process[0] = 'if'
                        process[2] = i
                        self.rePaint()
                        return process
        elif process[0] == 'if':
            if self.Data.getVisited(process[2]) == 1:
                self.Text.selectTextCol(5, self.textBrowser, u"结点" + chr(ord('A') + process[2]) + u"已经被访问过了")
                process[0] = 'check'
                process[2] = process[2] + 1
                self.rePaint()
                return process
            else:
                self.Text.selectTextCol(5, self.textBrowser, u"结点" + chr(ord('A') + process[2]) + u"还未被访问过")
                process[0] = 'dfs'
                self.rePaint()
                return process
        elif process[0] == 'dfs':
            self.Text.selectTextCol(7, self.textBrowser, u"递归（相当于将结点" + process[1] +
                                    u"入栈）,对结点" + chr(ord('A') + process[2]) + u"进行深度优先遍历")
            print process
            self.Data.addStackdApex([process[0], process[1], process[2]])
            process[0] = 'start'
            process[1] = chr(ord('A') + process[2])
            process[2] = 0
            print self.Data.getStackApex(0)
            self.rePaint()
            return process
        if self.Data.getStackApNumber() != 0:
            process = self.Data.popStack()
            self.Text.selectTextCol(4, self.textBrowser, u"该结点已没有未被访问的邻接点，返回上一层递归（出栈）,继续对结点" +
                                    process[1] + u"的邻接点进行检查")
            process[0] = 'check'
            process[2] = process[2] + 1
            self.Data.setTargetApex(process[1])
            self.rePaint()
            return process
        else:
            self.Text.selectTextCol(8, self.textBrowser, u"已完成深度优先遍历")
            self.Data.setTargetApex('X')
            process[0] = 'stop'
            self.rePaint()
            return process