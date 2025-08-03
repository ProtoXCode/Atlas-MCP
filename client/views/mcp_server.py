from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class MCPServer(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('MCP Server'))
        self.setLayout(layout)
