# -*- coding: utf-8 -*-
from PyQt4 import QtGui

class MatrixText:
    def updateMatrixText(self, Data, textBrowser, x, y):
        textBrowser.clear()
        textBrowser.insertPlainText("    ")
        for k in range(0, Data.getSize()):
            textBrowser.insertPlainText(str(Data.getApex(k)) +"   ")
        textBrowser.insertPlainText("\n")
        for i in range(0, Data.getSize()):
            textBrowser.insertPlainText(str(Data.getApex(i)))
            for j in range(0, Data.getSize()):
                textBrowser.insertPlainText("   ")
                if (i == x and j == y) or (Data.getOriented() == False and i == y and j == x):
                    textBrowser.setTextColor(QtGui.QColor(255, 0, 0, 240))
                    textBrowser.insertPlainText(str(Data.getArc(i, j)))
                    textBrowser.setTextColor(QtGui.QColor(0, 0, 0, 255))
                else:
                    textBrowser.insertPlainText(str(Data.getArc(i, j)))
            textBrowser.insertPlainText(" \n")

    def initDFSText(self, textBrowser):
        textBrowser.setText(u"void DFS(MGraph G,int i)"+ u"\n" +
                            u"{//从图G的第i号顶点出发深度优先遍历图G"+ u"\n" +
                            u"  int j,w;"+ u"\n" +
                            u"  visited[i]=1;"+ u"\n" +
                            u"  cout<<setw(5)<<G.vertex[i]; //访问结点i"+ u"\n" +
                            u"  for(w=FirstadjVex(G,i);w>=0;w=NextAdjVex(G,i,w))"+ u"\n" +
                            u"      if(visited[w]==0)"+ u"\n" +
                            u"      {	cout<<\"->/\";"+ u"\n" +
                            u"          DFS(G,w);"+ u"\n" +
                            u"      }"+ u"\n" +
                            u"}")

    def selectTextCol(self, col, textBrowser, text):
        textBrowser.clear()
        for i in range(0, 8):
            if i == col:
                textBrowser.setTextBackgroundColor(QtGui.QColor(255, 0, 0, 240))
            if i == 0:
                textBrowser.insertPlainText(u"void DFS(MGraph G,int i)"+ u"\n" )
            elif i == 1:
                textBrowser.insertPlainText(u"  int j,w;"+u"\n")
            elif i == 2:
                textBrowser.insertPlainText(u"  visited[i]=1;"+ u"\n")
            elif i == 3:
                textBrowser.insertPlainText(u"  cout<<setw(5)<<G.vertex[i]; //访问结点i"+ u"\n")
            elif i == 4:
                textBrowser.insertPlainText(u"  for(w=FirstadjVex(G,i);w>=0;w=NextAdjVex(G,i,w))"+ u"\n")
            elif i == 5:
                textBrowser.insertPlainText(u"      if(visited[w]==0)"+ u"\n")
            elif i == 6:
                textBrowser.insertPlainText(u"      {	cout<<\"->/\";"+ u"\n")
            elif i == 7:
                textBrowser.insertPlainText(u"          DFS(G,w);"+ u"\n" )
            textBrowser.setTextBackgroundColor(QtGui.QColor(0, 0, 0, 0))
            if i == 0:
                textBrowser.insertPlainText(u"{//从图G的第i号顶点出发深度优先遍历图G"+ u"\n")
        textBrowser.insertPlainText(u"      }" + u"\n" +
                            u"}"+ u"\n"+ u"\n")
        textBrowser.insertPlainText(u""+text)

    def updateDFSDataText(self, textBrowser, Data):
        textBrowser.clear()
        textBrowser.insertPlainText(u"visited数组:"+u"\n")
        for i in range(0, Data.getSize()):
            textBrowser.insertPlainText(u"  "+Data.getApex(i))
        textBrowser.insertPlainText(u"\n")
        for i in range(0, Data.getSize()):
            textBrowser.insertPlainText(u"  "+str(Data.getVisited(i)))
        textBrowser.insertPlainText(u"\n")
        textBrowser.insertPlainText(u"已访问的结点:"+u"\n")
        for i in range(0, Data.getVisitedApNumber()):
            textBrowser.insertPlainText(u"  "+str(Data.gethadVisitedApex(i)))
        textBrowser.insertPlainText(u"\n")
        textBrowser.insertPlainText(u"进入栈的结点:"+u"\n")
        for i in range(0, Data.getStackApNumber()):
            textBrowser.insertPlainText(u"  "+str(Data.getStackApex(i)))

    def initBFSText(self, textBrowser):
        textBrowser.setText(u"void BFS(ALGraph G,int i)"+ u"\n" +
                            u"{//从图G的第i号顶点出发广度优先遍历图G"+ u"\n" +
                            u"  visited[i]=1;EnQueue(Q,i);"+ u"\n" +
                            u"  while(!QueueEmpty(Q))"+ u"\n" +
                            u"  { j=DeQueue(Q);cout<<setw(5)<<G.adjlist[j].vertex;"+ u"\n" +
                            u"      p=G.adjlist[j].firstedge;"+ u"\n" +
                            u"      while(p)"+ u"\n" +
                            u"      {   k=p->adjvex;"+ u"\n" +
                            u"          if(visited[k]==0)"+ u"\n" +
                            u"          {   visited[k]=1;EnQueue(Q,k);"+ u"\n" +
                            u"          p=p->nextedge;}  }"+ u"\n" +
                            u"}")

    def selectTextColBFS(self, col, textBrowser, text):
        textBrowser.clear()
        textBrowser.insertPlainText(u"void BFS(ALGraph G,int i)"+ u"\n"+
                            u"{//从图G的第i号顶点出发广度优先遍历图G")
        for i in range(0, 10):
            if i == col:
                textBrowser.setTextBackgroundColor(QtGui.QColor(255, 0, 0, 240))
            if i == 0:
                textBrowser.insertPlainText(u"  visited[i]=1;EnQueue(Q,i);"+ u"\n" )
            elif i == 1:
                textBrowser.insertPlainText(u"  while(!QueueEmpty(Q))"+ u"\n")
            elif i == 2:
                textBrowser.insertPlainText(u"  { j=DeQueue(Q);cout<<setw(5)<<G.adjlist[j].vertex;"+ u"\n")
            elif i == 3:
                textBrowser.insertPlainText(u"      p=G.adjlist[j].firstedge;"+ u"\n" )
            elif i == 4:
                textBrowser.insertPlainText(u"      while(p)"+ u"\n")
            elif i == 5:
                textBrowser.insertPlainText(u"      {   k=p->adjvex;"+ u"\n")
            elif i == 6:
                textBrowser.insertPlainText(u"          if(visited[k]==0)"+ u"\n")
            elif i == 7:
                textBrowser.insertPlainText(u"          {   visited[k]=1;EnQueue(Q,k);"+ u"\n")
            elif i == 9:
                textBrowser.insertPlainText(u"          p=p->nextedge;}  }"+ u"\n"  )
            textBrowser.setTextBackgroundColor(QtGui.QColor(0, 0, 0, 0))
        textBrowser.insertPlainText(u"}" + u"\n")
        textBrowser.insertPlainText(u""+text)

    def updateBFSDataText(self, textBrowser, Data):
        textBrowser.clear()
        textBrowser.insertPlainText(u"visited数组:"+u"\n")
        for i in range(0, Data.getSize()):
            textBrowser.insertPlainText(u"  "+Data.getApex(i))
        textBrowser.insertPlainText(u"\n")
        for i in range(0, Data.getSize()):
            textBrowser.insertPlainText(u"  "+str(Data.getVisited(i)))
        textBrowser.insertPlainText(u"\n")
        textBrowser.insertPlainText(u"已被访问的结点:"+u"\n")
        for i in range(0, Data.getVisitedApNumber()):
            textBrowser.insertPlainText(u"  "+str(Data.gethadVisitedApex(i)))
        textBrowser.insertPlainText(u"\n")
        textBrowser.insertPlainText(u"进入队列的结点:"+u"\n")
        for i in range(0, Data.getStackApNumber()):
            textBrowser.insertPlainText(u"  "+str(Data.getStackApex(i)))
