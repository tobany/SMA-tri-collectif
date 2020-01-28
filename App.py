import sys
import threading

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QApplication

from Agent import Agent
from Grid import Grid


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Tri collectif multi-agents'
        self.left = 0
        self.top = 0
        self.width = 2000
        self.height = 1000
        self.grid = Grid(50, 200, 200)
        self.populateGrid(self.grid)
        self.initUI()

    def populateGrid(self, grid):
        agents = list()
        for i in range(20):
            a = Agent(10, 0.1, 0.3, 1, grid)
            grid.place_agent(a)
            agents.append(a)
        for k in range(500):
            if k % 100 == 0:
                self.createTable()
            for a in agents:
                a.act()
            print(grid.object_grid)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.show()

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.grid.size)
        self.tableWidget.setColumnCount(self.grid.size)
        print(self.grid.object_grid)
        for rowNb, row in enumerate(self.grid.object_grid):
            for columnNb, column in enumerate(row):
                self.tableWidget.setColumnWidth(columnNb, 1)
                self.tableWidget.setItem(rowNb, columnNb, QTableWidgetItem())
                if column[0] == 'A':
                    self.tableWidget.item(rowNb, columnNb).setBackground(QColor(155, 0, 0))
                elif column[0] == 'B':
                    self.tableWidget.item(rowNb, columnNb).setBackground(QColor(200, 155, 0))
                if column[1] == 'agent':
                    self.tableWidget.setItem(rowNb, columnNb, QTableWidgetItem('A'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())