#Currently pulls the lyrics off of genius and outputs them onto a file

from bs4 import *
import requests

firstIteration=[]  

URL = input("Enter the url to the lyrics of the song: ")
r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

for a in soup.find("div", attrs={"id":"lyrics-root"}):       
    firstIteration.append(a.get_text("\n"))

try:    #removes unnecessary lines
    firstIteration.pop(-1)
    firstIteration.pop(-1)
    firstIteration.pop(0)
    firstIteration.pop(1)
    firstIteration.pop(3)
    firstIteration.pop(3)
except:
    print("Something went wrong....")
    
fName = input("What is the name of the txt file:")
fName += ".txt"
#print(fName)   #Test to see the output of the file name

f = open(fName,"a", encoding="utf-8")
for b in firstIteration:
    f.write(b)
    #print(b)   #used to check if the lyrics were outputting correctly