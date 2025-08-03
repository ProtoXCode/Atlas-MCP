from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Status(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Status'))
        self.setLayout(layout)
