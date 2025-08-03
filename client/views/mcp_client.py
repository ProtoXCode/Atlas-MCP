from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class MCPClient(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('MCP Client'))
        self.setLayout(layout)
