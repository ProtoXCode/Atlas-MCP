import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, \
    QStackedWidget
import qt_material

from panels.menu import MenuPanel
from views.mcp_client import MCPClient
from views.mcp_server import MCPServer
from views.settings import Settings
from views.status import Status

PROGRAM_NAME = 'Atlas-MCP'
WINDOW_WIDTH = 1800
WINDOW_HEIGHT = 1000
MENU_WIDTH = 300


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(PROGRAM_NAME)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        central = QWidget()
        self.setCentralWidget(central)

        grid = QGridLayout(central)
        grid.setSpacing(8)
        central.setLayout(grid)

        # Menu panel
        self.menu_panel = MenuPanel()
        self.menu_panel.setFixedWidth(MENU_WIDTH)
        grid.addWidget(self.menu_panel, 0, 0)

        # QTStackedWidget for main content area
        self.stack = QStackedWidget()
        grid.addWidget(self.stack, 0, 1)

        # Pages
        mcp_client = MCPClient()
        mcp_server = MCPServer()
        settings = Settings()
        status = Status()
        self.stack.addWidget(mcp_client)
        self.stack.addWidget(mcp_server)
        self.stack.addWidget(settings)
        self.stack.addWidget(status)

        # Buttons
        self.menu_panel.button_mcp_client.clicked.connect(
            lambda: self.stack.setCurrentWidget(mcp_client))
        self.menu_panel.button_mcp_server.clicked.connect(
            lambda: self.stack.setCurrentWidget(mcp_server))
        self.menu_panel.button_settings.clicked.connect(
            lambda: self.stack.setCurrentWidget(settings))
        self.menu_panel.button_status.clicked.connect(
            lambda: self.stack.setCurrentWidget(status))

        # Stretch settings
        grid.setRowStretch(0, 1)
        grid.setColumnStretch(1, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qt_material.apply_stylesheet(app, theme='dark_blue.xml')

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
