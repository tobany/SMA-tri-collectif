import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QApplication, QHeaderView

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
        self.initUI()

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
        for rowNb, row in enumerate(self.grid.object_grid):
            for columnNb, column in enumerate(row):
                self.tableWidget.setColumnWidth(columnNb, 1)
                self.tableWidget.setItem(rowNb, columnNb, QTableWidgetItem())
                if column[0] == 'A':
                    self.tableWidget.item(rowNb, columnNb).setBackground(QColor(155, 0, 0))
                elif column[0] == 'B':
                    self.tableWidget.item(rowNb, columnNb).setBackground(QColor(200, 155, 0))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())