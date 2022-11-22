from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        title = "그림판"
        top = 200
        left = 200
        width = 1200
        height = 800

        icon = "img/web.png"

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 5
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("파일")
        brushSize = mainMenu.addMenu("팬 사이즈")
        brushColor = mainMenu.addMenu("색상")

        saveAction = QAction(QIcon("img/save.png"), "저장",self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)
        
        clearAction = QAction(QIcon("img/delete.png"), "초기화", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        fileMenu.addSeparator()
        
        exitAction = QAction(QIcon("img/exit.png"), "나가기", self)
        exitAction.setShortcut("Ctrl+Q")
        fileMenu.addAction(exitAction)
        exitAction.triggered.connect(quit)
        
    
        threepxAction = QAction("3px", self)
        brushSize.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePixel)

        fivepxAction = QAction("5px", self)
        brushSize.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePixel)

        sevenpxAction = QAction("7px", self)
        brushSize.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPixel)

        ninepxAction = QAction("10px", self)
        brushSize.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePixel)

        blackAction = QAction(QIcon("./img/black.png"), "검정색", self)
        blackAction.setShortcut("Ctrl+B")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)

        blueAction = QAction(QIcon("./img/blue.png"), "파란색", self)
        blueAction.setShortcut("Ctrl+U")
        brushColor.addAction(blueAction)
        blueAction.triggered.connect(self.blueColor)

        whitekAction = QAction(QIcon("./img/white.png"), "하얀색", self)
        whitekAction.setShortcut("Ctrl+W")
        brushColor.addAction(whitekAction)
        whitekAction.triggered.connect(self.whiteColor)


        redAction = QAction(QIcon("./img/red.png"), "빨강색", self)
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        greenAction = QAction(QIcon("./img/green.png"), "초록색", self)
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        yellowAction = QAction(QIcon("./img/yellow.png"), "노란색", self)
        yellowAction.setShortcut("Ctrl+Y")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            #print(self.lastPoint)


    def mouseMoveEvent(self, event):
        if(event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.drawing = False


    def paintEvent(self, event):
        canvasPainter  = QPainter(self)
        canvasPainter.drawImage(self.rect(),self.image, self.image.rect() )

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def threePixel(self):
        self.brushSize = 3

    def fivePixel(self):
        self.brushSize = 5

    def sevenPixel(self):
        self.brushSize = 7

    def ninePixel(self):
        self.brushSize = 10

    def blackColor(self):
        self.brushColor = Qt.black
        
    def blueColor(self):
        self.brushColor = Qt.blue

    def whiteColor(self):
        self.brushColor = Qt.white

    def redColor(self):
        self.brushColor = Qt.red

    def greenColor(self):
        self.brushColor = Qt.green

    def yellowColor(self):
        self.brushColor = Qt.yellow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()