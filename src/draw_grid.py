from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QTreeView


class DrawGrid(QFrame):

    def __init__(self):
        super().__init__()
        self.tree = None
        self.model = None
        self.draw_box()

    def draw_box(self):

        self.model = QFileSystemModel()
        self.model.setRootPath("")

        self.tree = QTreeView()
        self.tree.setIndentation(10)
        self.tree.setModel(self.model)

        frame = QVBoxLayout()
        frame.addWidget(self.tree)
        self.setLayout(frame)