#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4 import QtCore

class GraphData():
    def __init__(self):
        self.Apex = []
        self.Arc = []
        self.coordinates = []
        self.visited = []
        self.resetVisited()
        self.oriented = False
        self.hadVisited = []
        self.stack = []
        self.targetApex = 'X'

    def setTargetApex(self, Apex):
        self.targetApex = Apex

    def getTargetApex(self):
        return self.targetApex

    def addnewApex(self, x, y):
        if self.getSize() == 0:
            self.Apex.append('A')
            self.coordinates.append([x, y])
            self.Arc.append([0])
        else:
            self.Apex.append(chr(ord(self.Apex[-1])+1))
            self.coordinates.append([x, y])
            Temp = []
            for i in range(0, len(self.Arc)):
                self.Arc[i].append(0)
                Temp.append(0)
            Temp.append(0)
            self.Arc.append(Temp)
        self.resetVisited()

    def setnewArc(self, Ap1, Ap2):
        num1 = ord(Ap1) - ord('A')
        num2 = ord(Ap2) - ord('A')
        self.Arc[num1][num2] = 1

    def setOriented(self, oriented):
        self.oriented = oriented

    def getSize(self):
        return len(self.Apex)

    def getApex(self, i):
        return self.Apex[i]

    def getArc(self, Ap1, Ap2):
        return self.Arc[Ap1][Ap2]

    def getCoordinates(self, i):
        return self.coordinates[i]

    def getOriented(self):
        return self.oriented

    def resetVisited(self):
        self.visited = []
        for i in range(0, self.getSize()):
            self.visited.append(0)

    def setVisited(self, Apex):
        self.visited[ord(Apex) - ord('A')] = 1

    def getVisited(self, Apex):
        return self.visited[Apex]

    def checkApex(self, x, y, lenth):
        Line = QtCore.QLineF()
        Line.setP1(QtCore.QPointF(x, y))
        for i in range(0, self.getSize()):
            Line.setP2(QtCore.QPointF(self.getCoordinates(i)[0], self.getCoordinates(i)[1]))
            if Line.length() <= lenth:
                return self.getApex(i)
        return 'X'

    def addVisitedApex(self, Apex):
        self.hadVisited.append(Apex)

    def gethadVisitedApex(self, x):
        return self.hadVisited[x]

    def getVisitedApNumber(self):
        return len(self.hadVisited)

    def addStackdApex(self, Apex):
        self.stack.append(Apex)

    def getStackApex(self, x):
        return self.stack[x][1]

    def getStackApNumber(self):
        return len(self.stack)

    def popStack(self):
        return self.stack.pop(-1)

    def fifoStack(self):
        return self.stack.pop(0)

    def restartDFS(self):
        self.resetVisited()
        self.hadVisited = []
        self.stack = []

    def testprint(self):
        print self.Apex
        print self.Arc
        print self.coordinates

if __name__ == "__main__":
    test1 = GraphData()
    test1.addStackdApex([0 , 1 ,'asd'])
    test1.addStackdApex([0 , 2 ,'asd'])
    test1.addStackdApex([0 , 3 ,'asd'])
    print test1.getStackApNumber()
    print test1.popStack()
    print test1.getStackApNumber()