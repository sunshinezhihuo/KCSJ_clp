# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import SceneArcPaint
import GraphData
import MatrixText

class SceneArcPaintBFS(SceneArcPaint.SceneArcPaint):
    def giveNewMatrix(self, Oriented):
        self.Data = GraphData.GraphData()
        self.clear()
        self.paintEll()
        self.Text.initBFSText(self.textBrowser)
        if Oriented == True:
            self.Data.setOriented(True)
        self.Text.updateBFSDataText(self.dataBrowser, self.Data)

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
            self.Text.updateBFSDataText(self.dataBrowser, self.Data)

    def restartBfs(self):
        self.Data.restartDFS()
        self.Text.updateBFSDataText(self.dataBrowser, self.Data)

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

    def rePaint(self):
        self.clear()
        self.paintEll()
        self.paintLine()
        self.Text.updateBFSDataText(self.dataBrowser, self.Data)

    def BFS(self, process):
        if process[0] == 'start':
            self.Data.setTargetApex(process[1])
            self.Text.selectTextColBFS(0, self.textBrowser, u"将顶点"+process[1]+u"加入队列")
            self.Data.addStackdApex([0, process[1]])
            process[0] = 'check'
            return process
        elif process[0] == 'check':
            if self.Data.getStackApNumber() == 0:
                process[0] = 'stop'
                self.Text.selectTextColBFS(1, self.textBrowser, u"队列中已经没有顶点了")
                return process
            else:
                process[0] = 'print'
                self.Text.selectTextColBFS(1, self.textBrowser, u"队列中还有" + str(self.Data.getStackApNumber()) + u"个顶点" )
                return process
        elif process[0] == 'print':
            process[0] = 'find'
            process[1] = self.Data.fifoStack()[1]
            process[2] = 0
            self.Data.setTargetApex(process[1])
            self.Data.setVisited(process[1])
            self.Data.addVisitedApex(process[1])
            self.Text.selectTextColBFS(2, self.textBrowser, u"将队列中的第一个顶点" + process[1] + u"导出，并输出" )
            return process
        elif process[0] == 'find':
            if process[2] < self.Data.getSize():
                for i in range(process[2], self.Data.getSize()):
                    if self.Data.getArc(ord(process[1]) - ord('A'), i) == 1:
                        process[0] = 'ifvisit'
                        process[2] = i
                        self.Text.selectTextColBFS(4, self.textBrowser, u"结点" + process[1] + u"到结点" + chr(ord('A') +i) + u"存在弧")
                        return process
            process[0] = 'check'
            return process
        elif process[0] == 'ifvisit':
            if self.Data.getVisited(process[2]) == 1:
                self.Text.selectTextColBFS(6, self.textBrowser, u"结点" + chr(ord('A') +process[2]) + u"已被加入队列（访问）过")
                process[0] = 'find'
                process[2] = process[2] + 1
                return process
            else:
                self.Text.selectTextColBFS(6, self.textBrowser, u"结点" + chr(ord('A') +process[2]) + u"还未被加入队列（访问）过")
                process[0] = 'visit'
                return process
        elif process[0] == 'visit':
            self.Text.selectTextColBFS(6, self.textBrowser, u"将结点" + chr(ord('A') +process[2]) + u"的visited数组置为1，并将其加入队列")
            self.Data.setVisited(chr(ord('A') +process[2]))
            self.Data.addStackdApex([0, chr(ord('A') +process[2])])
            process[0] = 'find'
            process[2] = process[2] + 1
            return process
