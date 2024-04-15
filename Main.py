from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow
import os

class HTMLViewer(QMainWindow):
    def __init__(self, html_file):
        super().__init__()
        self.setWindowTitle("HTML Viewer")
        self.setGeometry(100, 100, 1300, 750)

        self.web_view = QWebEngineView(self)
        self.setCentralWidget(self.web_view)

        url = QUrl.fromLocalFile(os.path.abspath(html_file))
        self.web_view.load(url)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    html_file = "main.html"  # Замініть це на шлях до вашого HTML-файлу
    window = HTMLViewer(html_file)
    window.show()
    sys.exit(app.exec_())
