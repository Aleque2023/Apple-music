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
        
        oLabel = QLabel(self,text="(Optional)")
        oLabel.setGeometry(20,88,50,25)
        oLabel.setFont(QFont("Arial",7))
        
        global lyric
        lyric = QLineEdit(self, placeholderText="Enter URL here...")
        lyric.setGeometry(70,50,350,25)
        
        global fLine
        fLine = QLineEdit(self, placeholderText="EX: C:\\Users\\Alex\\Documents")
        fLine.setGeometry(70,75,350,25)
        
        lButton = QPushButton(self,text="Transfer")
        lButton.setGeometry(425,50,75,25)
        lButton.clicked.connect(self.convert)
    
    def convert(self, url):
        try:
            quantityI = len(firstIteration)
            if len(firstIteration) > 0:
                i=0
                for i in range(quantityI):
                    firstIteration.pop(0)
                    if len(firstIteration) == 0:
                        break
                    
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
            counter = 0
            for c in firstIteration:
                if "You might also like" == firstIteration[counter]:
                    firstIteration.pop(counter)
                if len(firstIteration[counter]) == 0:
                    firstIteration.pop(counter)
                if "Get tickets as low as" in firstIteration[counter]:
                    firstIteration.pop(counter)
                counter += 1
            
            secondIteration = " ".join(firstIteration)
            thirdIteration = secondIteration.replace("(\n", "\n(")
            fourthIteration = thirdIteration.replace("[\n", "\n[")
                        
            print(fourthIteration)
            
            finalName += ".txt"
            if len(fPath) == 0:
                f = open(finalName,"a", encoding="utf-8")
                f.write(fourthIteration)
            else:
                fnPath = fPath + "\\" + finalName
                f = open(fnPath, "a", encoding="utf-8")
                f.write(fourthIteration)
        except:
            pass
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()