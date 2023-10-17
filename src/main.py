import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from src.draw_grid import DrawGrid


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gridframe = DrawGrid()
        self.initialize()

    def initialize(self):
        self.setGeometry(200, 800, 700, 500)
        self.setWindowTitle("Grid Tool")
        self.setCentralWidget(self.gridframe)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
