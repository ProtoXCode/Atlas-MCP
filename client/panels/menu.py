from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class MenuPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.button_mcp_client = QPushButton('MCP Client')
        layout.addWidget(self.button_mcp_client)
        self.button_mcp_server = QPushButton('MCP Server')
        layout.addWidget(self.button_mcp_server)
        self.button_settings = QPushButton('Settings')
        layout.addWidget(self.button_settings)
        self.button_status = QPushButton('Status')
        layout.addWidget(self.button_status)

        layout.addStretch()
        self.setLayout(layout)
