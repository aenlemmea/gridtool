import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QLineEdit, \
    QGridLayout

WIDTH = 800
HEIGHT = 600


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        toolbar = QHBoxLayout()

        toolbar.addWidget(QPushButton('Infinite Grid'))
        toolbar.addWidget(QPushButton('Give Dimensions'))

        self.user_text_box = [[] for _ in range(5)]
        positions = [(i + 1, j + 1) for i in range(5) for j in range(5)]

        for i, position in enumerate(positions):
            self.user_text_box[position[0] - 1].append(QLineEdit())
            layout.addWidget(self.user_text_box[position[0] - 1][position[1] - 1], *position)

        dummy_widget = QWidget()
        dummy_widget.setLayout(layout)
        self.setCentralWidget(dummy_widget)
        self.initialize()

    def initialize(self):
        self.setGeometry(0, 0, WIDTH, HEIGHT)
        self.setWindowTitle("Grid Tool")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
