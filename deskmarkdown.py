# github.com/lastkarrde

import sys

import markdown2

from PySide.QtCore import QUrl
from PySide.QtGui import QApplication, QGridLayout, QLineEdit, QPushButton, QWidget, QTextEdit, QMainWindow, QMenu, QMenuBar, QAction, QFileDialog, QHBoxLayout, QSplitter
from PySide.QtWebKit import QWebView


class App(QMainWindow):

    def __init__(self, parent=None):
        """Create Qt widgets, connect event handlers."""

        super(App, self).__init__(parent)
        
        self.windowTitle = 'DMD | '
        self.fileName = ''
        
        self.setWindowTitle(self.windowTitle + 'Unsaved File')
        
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        
        openAction = QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open Markdown File')
        openAction.triggered.connect(self.openFile)
        
        newAction = QAction('New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New Markdown File')
        newAction.triggered.connect(self.newFile)

        saveAction = QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save File')
        saveAction.triggered.connect(self.saveFile)
        
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 1024, 768)
        
        self.show()

        self.txtInput = QTextEdit()
        self.txtInput.setTabStopWidth(20)
        self.webPreview = QWebView()
        self.webPreview.setHtml('Start typing...', baseUrl=QUrl('preview'))
        
        self.txtInput.textChanged.connect(self.loadPreview)
        
        splitter = QSplitter()
        splitter.addWidget(self.txtInput)
        splitter.addWidget(self.webPreview)


        self.setCentralWidget(splitter)
        

    def loadPreview(self):
        """Set the QWebView to the value of the parsed document."""
    
        html = markdown2.markdown(self.txtInput.toPlainText())
        self.webPreview.setHtml(html, baseUrl=QUrl('preview'))
        

    def openFile(self):
        """Handles opening a file, just like any other text editor."""
    
        self.fileName = QFileDialog.getOpenFileName()[0]
    
        fh = open(self.fileName, 'r')
        
        contents = fh.read()
        
        fh.close()
    
        self.txtInput.setText(contents)
        self.setWindowTitle(self.windowTitle + self.fileName)
       

    def newFile(self):
        """Creates a new file, just like any other text editor."""
           
        self.fileName = ''
        self.setWindowTitle(self.windowTitle + 'Unsaved File')
        self.txtInput.setText('')
        
        
    def saveFile(self):
        """Saves the file, just like any other text editor."""
    
        if not self.fileName == '':
            fh = open(self.fileName, 'w')
            fh.write(self.txtInput.toPlainText())
            fh.close()
            self.setWindowTitle(self.windowTitle + self.fileName)
            
        else:
            self.fileName = QFileDialog.getSaveFileName()[0]
            self.saveFile()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    basic = App()
    basic.show()
    
    sys.exit(app.exec_())
