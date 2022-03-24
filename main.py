from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class webBrowser(QMainWindow):
    def __init__(self):
        self.window = QWidget()
        self.window.setWindowTitle("Chibib And Chiboo Browser - Slow Internet Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit("Type URL")
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.for_btn = QPushButton(">")
        self.for_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.search_bar = QTextEdit("Search")
        self.search_bar.setMaximumHeight(30)

        self.search_btn = QPushButton("Search")
        self.search_btn.setMinimumHeight(30)

        self.home = QPushButton("🏠")
        self.home.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.for_btn)
        self.horizontal.addWidget(self.search_bar)
        self.horizontal.addWidget(self.search_btn)
        self.horizontal.addWidget(self.home)

        self.browser = QWebEngineView()

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://shedeurcoder.github.io/chibibandchiboo/"))

        self.window.setLayout(self.layout)
        self.window.show()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))

        self.back_btn.clicked.connect(self.browser.back)

        self.for_btn.clicked.connect(self.browser.forward)

        self.search_btn.clicked.connect(lambda: self.search(self.search_bar.toPlainText()))

        self.home.clicked.connect(lambda: self.goHome())

    def search(self, search):
        url = "https://duckduckgo.com/?q=" + search.replace(" ", "+")
        self.browser.setUrl(QUrl(url))

    def navigate(self, url):
        if not url.startswith("http"):
            url = "https://" + url.strip()
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url.strip()))

    def goHome(self):
        self.browser.setUrl(QUrl("https://shedeurcoder.github.io/chibibandchiboo"))

app = QApplication([])
window = webBrowser()
app.exec_()