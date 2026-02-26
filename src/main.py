
import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLineEdit, QPushButton, QToolBar
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


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

        self.tabs = QTabWidget() 
        self.tabs.setTabsClosable(True)
        self.tabs.setDocumentMode(True)
        self.tabs.tabCloseRequested.connect(self.fechar_aba)

        self.url = QLineEdit()
        self.url.setPlaceholderText("digita algo aí…")
        self.url.returnPressed.connect(self.navigate)

        back = QPushButton("←")
        forward = QPushButton("→")
        refresh = QPushButton("⟳")
        new_tab = QPushButton("+")
        home_btn = QPushButton("🏠")

        back.clicked.connect(self.browser.back)
        forward.clicked.connect(self.browser.forward)
        refresh.clicked.connect(self.browser.reload)
        
        new_tab.clicked.connect(lambda: self.adicionar_aba())
        home_btn.clicked.connect(self.go_home)

        bar = QToolBar()
        bar.setMovable(False)
        self.addToolBar(bar)

        bar.addWidget(back)
        bar.addWidget(forward)
        bar.addWidget(refresh)
        bar.addWidget(home_btn)
        bar.addWidget(self.url)
        bar.addWidget(new_tab)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.adicionar_aba()

        self.browser.urlChanged.connect(
            lambda u: self.url.setText(u.toDisplayString())
        )

        directory = os.path.dirname(os.path.abspath(__file__))
        home = os.path.join(directory, "ui", "home.html")

        url_inicial = QUrl.fromLocalFile(home)


        self.browser.setUrl(url_inicial)



    def adicionar_aba(self, url=None):

        if url is None or not isinstance(url, QUrl):
            directory = os.path.dirname(os.path.abspath(__file__))
            home_path = os.path.join(directory, "ui", "home.html")
            
            if os.path.exists(home_path):
                url = QUrl.fromLocalFile(home_path)
            else:
                url = QUrl("https://www.google.com")

        browser = QWebEngineView()
        browser.setUrl(url)

    
        i = self.tabs.addTab(browser, "Carregando...")
        
        
        self.tabs.setCurrentIndex(i)

        
        browser.urlChanged.connect(lambda u, b=browser: self.atualizar_url_interface(u, b))
        
        # Quando o título do site carregar, atualiza o nome da aba
        browser.titleChanged.connect(lambda t, b=browser: self.atualizar_titulo_aba(t, b))

        self.adicionar_aba()

    def go_home(self):
        # Localiza o arquivo home.html
        directory = os.path.dirname(os.path.abspath(__file__))
        home_path = os.path.join(directory, "ui", "home.html")
        
        if os.path.exists(home_path):
            url = QUrl.fromLocalFile(home_path)
        else:
            url = QUrl("https://www.google.com")
            
        # Pega a aba atual e carrega a URL
        self.tabs.currentWidget().setUrl(url)

    def adicionar_aba(self, url=None):
        if url is None:
            directory = os.path.dirname(os.path.abspath(__file__))
            home = os.path.join(directory, "ui", "home.html")
            url = QUrl.fromLocalFile(home) if os.path.exists(home) else QUrl("https://www.google.com")

        browser = QWebEngineView()
        browser.setUrl(url)

        i = self.tabs.addTab(browser, "Carregando...")
        self.tabs.setCurrentIndex(i)

        # Atualização automática de URL e Título
        browser.urlChanged.connect(lambda u, b=browser: self.atualizar_url_interface(u, b))
        browser.titleChanged.connect(lambda t, b=browser: self.atualizar_titulo_aba(t, b))

    def fechar_aba(self, i):
        if self.tabs.count() > 1:
            self.tabs.removeTab(i)
        else:
            self.close()

    def aba_alterada(self, i):
        # Atualiza a barra de endereço ao trocar de aba
        if self.tabs.currentWidget():
            qurl = self.tabs.currentWidget().url()
            self.url.setText(qurl.toDisplayString())

    def atualizar_url_interface(self, u, browser):
        if browser == self.tabs.currentWidget():
            self.url.setText(u.toDisplayString())

    def atualizar_titulo_aba(self, title, browser):
        i = self.tabs.indexOf(browser)
        if i != -1:
            display_title = (title[:15] + '..') if len(title) > 15 else title
            self.tabs.setTabText(i, display_title)

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
