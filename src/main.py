import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class ShiroBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shiro Browser")
        self.resize(1024, 768) 
        
        self.view = QWebEngineView()

        # Barra de endereços
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Digite a URL e pressione Enter...")
        self.url_bar.returnPressed.connect(self.load_url)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(self.view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        
    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("https"):
            url = "https://" + url
        self.view.setUrl(QUrl(url))

app = QApplication(sys.argv)
window = ShiroBrowser()
window.show()
sys.exit(app.exec())
