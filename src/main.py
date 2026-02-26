import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLineEdit, QPushButton, QToolBar
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl


class Shiro(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shiro")
        self.resize(1100, 700)

        self.setStyleSheet("""
            QMainWindow {
                background: #0f0f13;
            }

            QToolBar {
                background: #16161d;
                border: none;
                padding: 6px;
                spacing: 6px;
            }

            QLineEdit {
                background: #1f1f2a;
                border: 1px solid #2d2d3a;
                border-radius: 8px;
                padding: 6px 10px;
                color: #e4e4f0;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 1px solid #7c5cff;
                background: #262636;
            }

            QPushButton {
                background: #232330;
                border: none;
                border-radius: 6px;
                padding: 6px 10px;
                color: #e4e4f0;
                min-width: 32px;
            }

            QPushButton:hover {
                background: #2e2e40;
            }

            QPushButton:pressed {
                background: #1a1a24;
            }
        """)

        self.browser = QWebEngineView()

        self.url = QLineEdit()
        self.url.setPlaceholderText("digita algo aí…")
        self.url.returnPressed.connect(self.navigate)

        back = QPushButton("←")
        forward = QPushButton("→")
        refresh = QPushButton("⟳")

        back.clicked.connect(self.browser.back)
        forward.clicked.connect(self.browser.forward)
        refresh.clicked.connect(self.browser.reload)

        bar = QToolBar()
        bar.setMovable(False)
        self.addToolBar(bar)

        bar.addWidget(back)
        bar.addWidget(forward)
        bar.addWidget(refresh)
        bar.addWidget(self.url)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.browser.urlChanged.connect(
            lambda u: self.url.setText(u.toDisplayString())
        )

        self.browser.setUrl(QUrl("https://github.com"))

        directory = os.path.dirname(os.path.abspath(__file__))
        home = os.path.join(directory, "ui", "home.html")

        url_inicial = QUrl.fromLocalFile(home)


        self.browser.setUrl(url_inicial)
    
    def navigate(self):
        text = self.url.text().strip()

        if not text:
            return

        if " " in text:
            text = f"https://google.com/search?q={text.replace(' ', '+')}"
        elif not text.startswith("http"):
            text = "https://" + text

        self.browser.setUrl(QUrl(text))


app = QApplication(sys.argv)
window = Shiro()
window.show()
sys.exit(app.exec())
