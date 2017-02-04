# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import GraphData
import MatrixText

class ScenePaint(QtGui.QGraphicsScene):
    def __init__(self):
        QtGui.QGraphicsScene.__init__(self)
        self.Data = GraphData.GraphData()
        self.Text = MatrixText.MatrixText()

    def giveNewMatrix(self, Oriented, textBrowser):
        self.Data = GraphData.GraphData()
        """初始四点"""
        self.Data.addnewApex(100, 100)
        self.Data.addnewApex(280, 100)
        self.Data.addnewApex(100, 280)
        self.Data.addnewApex(280, 280)
        self.clear()
        self.paintEll()
        self.Text.updateMatrixText(self.Data, textBrowser, 15, 15)
        if Oriented == True:
            self.Data.setOriented(True)

    def updateText(self, textBrowser):
        self.Text.updateMatrixText(self.Data, textBrowser, 15, 15)

    def getDataSize(self):
        return self.Data.getSize()

    def addNewArc(self, Ap1, Ap2, textBrowser):
        if (self.Data.getOriented() == False):
            self.Data.setnewArc(Ap1, Ap2)
            self.Data.setnewArc(Ap2, Ap1)
            self.clear()
            self.paintEll()
            self.paintLine()
            self.Text.updateMatrixText(self.Data, textBrowser, ord(Ap1)-ord('A'), ord(Ap2)-ord('A'))
        else:
            self.Data.setnewArc(Ap1, Ap2)
            self.clear()
            self.paintEll()
            self.paintLine()
            self.Text.updateMatrixText(self.Data, textBrowser, ord(Ap1)-ord('A'), ord(Ap2)-ord('A'))

    def mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent):
        print QGraphicsSceneMouseEvent.lastScenePos().x()
        print QGraphicsSceneMouseEvent.lastScenePos().y()
        if self.Data.getSize() >= 14:
            self.emit(QtCore.SIGNAL("tooManyApex"))
        else:
            self.Data.addnewApex(QGraphicsSceneMouseEvent.lastScenePos().x(), QGraphicsSceneMouseEvent.lastScenePos().y())
            self.clear()
            self.paintEll()
            self.paintLine()
            self.emit(QtCore.SIGNAL("updateText"))


    def paintEll(self):
        for i in range(0, self.Data.getSize()):
            self.addEllipse(self.Data.getCoordinates(i)[0]-10, self.Data.getCoordinates(i)[1]-10, 20, 20)
            Text = self.addText(self.Data.getApex(i))
            Text.setPos(self.Data.getCoordinates(i)[0]-6, self.Data.getCoordinates(i)[1]-11)

    def undirectionLine(self, x1, y1, x2, y2):
        Line = QtCore.QLineF(x1, y1, x2, y2)
        Line.setLength(10)
        F1 = Line.p2()
        Line = QtCore.QLineF(x2, y2, x1, y1)
        Line.setLength(10)
        F2 = Line.p2()
        Line = QtCore.QLineF(F1, F2)
        self.addLine(Line)

    def makeArrow(self, x1, y1, x2, y2):
        Line = QtCore.QLineF(x2, y2, x1, y1)
        Line.setLength(16)
        F1 = Line.p2()
        Line.setLength(10)
        F2 = Line.p2()
        Line = QtCore.QLineF(F1, F2)
        Line = Line.normalVector()
        Line.setLength(3)
        F1 =Line.p2()
        F3 =Line.p1()
        Line = QtCore.QLineF(F1, F3)
        Line.setLength(6)
        F3 =Line.p2()
        Polygon = QtGui.QPolygonF()
        Polygon.append(F1)
        Polygon.append(F2)
        Polygon.append(F3)
        self.addPolygon(Polygon, brush=QtGui.QBrush(QtGui.QColor(0, 0, 0)))

    def paintLine(self):
        """无向图的场合"""
        if(self.Data.getOriented() == False):
            for i in range(0, self.Data.getSize()):
                for j in range(i+1, self.Data.getSize()):
                    if(self.Data.getArc(i, j) == 1):
                        self.undirectionLine(self.Data.getCoordinates(i)[0], self.Data.getCoordinates(i)[1]
                                             , self.Data.getCoordinates(j)[0], self.Data.getCoordinates(j)[1])
        else:
            """有向图的场合"""
            for i in range(0, self.Data.getSize()):
                for j in range(0, self.Data.getSize()):
                    if(i != j and self.Data.getArc(i, j) == 1):
                        self.undirectionLine(self.Data.getCoordinates(i)[0], self.Data.getCoordinates(i)[1]
                                             , self.Data.getCoordinates(j)[0], self.Data.getCoordinates(j)[1])
                        self.makeArrow(self.Data.getCoordinates(i)[0], self.Data.getCoordinates(i)[1]
                                             , self.Data.getCoordinates(j)[0], self.Data.getCoordinates(j)[1])
