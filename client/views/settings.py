from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Settings(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Settings'))
        self.setLayout(layout)
