import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QApplication, QMainWindow, QTabWidget

from Agent import Agent
from Grid import Grid


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Tri collectif multi-agents'
        self.left = 0
        self.top = 0
        self.width = 2000
        self.height = 1000
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tableWidget = MyTableWidget(self)
        self.setCentralWidget(self.tableWidget)
        self.show()



class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.grid = Grid(50, 200, 200)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(2000, 1000)

        self.tabs.addTab(self.tab1, "Initiale")
        self.tabs.addTab(self.tab2, "Intermédiaire")
        self.tabs.addTab(self.tab3, "Finale")

    #Generate first tab content
        self.tab1.layout = QVBoxLayout(self)
        self.initTable = QTableWidget()
        self.create_table(self.initTable)
        self.tab1.layout.addWidget(self.initTable)
        self.tab1.setLayout(self.tab1.layout)

        self.populateGrid(self.grid)

    #Generate last tab content
        self.tab3.layout = QVBoxLayout(self)
        self.finaleTable = QTableWidget()
        self.create_table(self.finaleTable)
        self.tab3.layout.addWidget(self.finaleTable)
        self.tab3.setLayout(self.tab3.layout)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def createTab2(self):
        self.tab2.layout = QVBoxLayout(self)
        self.finaleTable = QTableWidget()
        self.create_table(self.finaleTable)
        self.tab2.layout.addWidget(self.finaleTable)
        self.tab2.setLayout(self.tab2.layout)

    def populateGrid(self, grid):
        agents = list()
        nbIteration = 1000000
        for i in range(20):
            a = Agent(10, 0.1, 0.3, 1, grid)
            grid.place_agent(a)
            agents.append(a)
        for k in range(nbIteration):
            if k == nbIteration/2:
                self.createTab2()
            for a in agents:
                a.act()

    def create_table(self, table):
        table.setRowCount(self.grid.size)
        table.setColumnCount(self.grid.size)
        for rowNb, row in enumerate(self.grid.object_grid):
            for columnNb, column in enumerate(row):
                table.setColumnWidth(columnNb, 1)
                table.setItem(rowNb, columnNb, QTableWidgetItem())
                if column[0] == 'A':
                    table.item(rowNb, columnNb).setBackground(QColor(155, 0, 0))
                elif column[0] == 'B':
                    table.item(rowNb, columnNb).setBackground(QColor(200, 155, 0))
                if column[1] == 'agent':
                    table.setItem(rowNb, columnNb, QTableWidgetItem('A'))
        # self.tableWidget = QTableWidget()
        # self.tableWidget.setRowCount(self.grid.size)
        # self.tableWidget.setColumnCount(self.grid.size)
        # for rowNb, row in enumerate(self.grid.object_grid):
        #     for columnNb, column in enumerate(row):
        #         self.tableWidget.setColumnWidth(columnNb, 1)
        #         self.tableWidget.setItem(rowNb, columnNb, QTableWidgetItem())
        #         if column[0] == 'A':
        #             self.tableWidget.item(rowNb, columnNb).setBackground(QColor(155, 0, 0))
        #         elif column[0] == 'B':
        #             self.tableWidget.item(rowNb, columnNb).setBackground(QColor(200, 155, 0))
        #         if column[1] == 'agent':
        #             self.tableWidget.setItem(rowNb, columnNb, QTableWidgetItem('A'))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())