#did a pip install PyQt6

import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

from bs4 import *
import requests

from tkinter import *
win = Tk()
w = round((win.winfo_screenmmwidth()))
h = round((win.winfo_screenheight())) #To determine the size of the user's screen automatically to center the program

firstIteration=[] 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Apple Music Stuff")
        self.setGeometry(int(h/2), int(w/2), 525, 250) #The parameters of this one is (x, y, width, height)
        self.initUI()
        
    def initUI(self):
        lLabel = QLabel(self,text="URL")
        lLabel.setGeometry(20,50,50,25)
        
        fLabel = QLabel(self,text="Filepath")
        fLabel.setGeometry(20,75,50,25)
        
        global lyric
        lyric = QLineEdit(self, placeholderText="Enter URL here...")
        lyric.setGeometry(70,50,350,25)
        
        global fLine
        fLine = QLineEdit(self, placeholderText="(Optional) Enter filepath...")
        fLine.setGeometry(70,75,350,25)
        
        lButton = QPushButton(self,text="Transfer")
        lButton.setGeometry(425,50,75,25)
        lButton.clicked.connect(self.convert)
    
    def convert(self, url):
        try:
            url = lyric.text()
            name = url.split("https://genius.com/")
            finalName = name[1]
            
            fPath = fLine.text()
            
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            
            for a in soup.find("div", attrs={"id":"lyrics-root"}):       
                firstIteration.append(a.get_text("\n"))

            firstIteration.pop(-1)
            firstIteration.pop(-1)
            firstIteration.pop(0)
            firstIteration.pop(1)
            firstIteration.pop(3)
            firstIteration.pop(3)
            
            finalName += ".txt"
            
            if len(fPath) == 0:
                f = open(finalName,"a", encoding="utf-8")
                for b in firstIteration:
                    f.write(b)
            else:
                fnPath = fPath + "\\" + finalName
                f = open(fnPath, "a", encoding="utf-8")
                for b in firstIteration:
                    f.write(b)
        except:
            errorBox = QMessageBox()
            errorBox.setIcon(QMessageBox.warning)
            errorBox.setWindowTitle("Warning")
            errorBox.setText("An error occurred....")
            errorBox.setStandardButtons(QMessageBox.Ok)
            retval = errorBox.exec()
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()