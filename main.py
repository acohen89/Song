import requests
import urllib
from urllib import request
import json

def main():
   readAndSave()
   r = requests.get("https://www.rocknrollamerica.net/Top1000.html")
   #test = ' 1px; padding-right: 1px; padding-top: 1px u1:str="Another Brick In The Wall "> Like A Rolling Stone</td> '
   li =  list(r.text)
   #print(li)
   listOfSongs = []
   for i in range(len(li)): #Gathers list of songs
       tempStr = ""
       if li[i] == "s":
           if li[i+1] == "t":
               if li[i+2] == "r":
                   if li[i+3] == "=":
                       done = False
                       iter = 5
                       while not done:
                            if li[i + iter] == '"':
                                done = True
                            else:
                               tempStr += li[i + iter]
                               #print(li[iter])
                               iter += 1
       if len(tempStr) >= 2:
        listOfSongs.append(tempStr)
   testList = ["I'm on a boat"]
   for i in testList: #Check if song has already been used
       if not(i in usedSongs):
           #create query url
           qUrl = "https://www.google.com/search?safe=strict&rlz=1C1CHBF_enUS887US887&sxsrf=ALeKk03cyazYe4mCJVoCXP-_HwOMs9ETyw%3A1593109458102&ei=0uv0Xo3cBYz--gTpq5fQBg&q="
           midUrl = ""
           endUrl = "&gs_lcp=CgZwc3ktYWIQAxgAMggIABAHEAoQHjIICAAQCBAHEB4yCAgAEAgQBxAeOgcIABCxAxBDOgQIABBDOgYIABAHEB46AggAOgQIABAKOgYIABAIEB5Q6RlYqTFgpDhoAHAAeACAAW2IAfcGkgEDOC4ymAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab"
           li = i.split()
           for i in li:
                midUrl += i + "+"
           midUrl += "lyrics"
           midUrl += "&oq" + midUrl
           qUrl += midUrl + endUrl
           f = open("testString.txt", "w")
           f.write(qUrl)
           f.close()
           #print(qUrl)

            #usedSongs.append(i)

    #pushInfo():

   """
   1. Get List of rock songs
   2. Check if  Song has already been used
   3. Get Lyrics of each song 
   4. Add averages to variables
   5. Add song to used songs 
   
   
   """
def pushInfo():
    f = open("usedSongs.json", "w")
    f.write({"UsedSongs": usedSongs})
    f.close()
    f = open("data.json", "w")
    f.write({"Averages": {"Lines":  AVGLines, "Stanzas":  AVGStanzas, "WordsPerLine":  AVGWordsPerLine}})
    f.close()


def readAndSave():
    # Read JSON File and compile all into variables
    with open('data.json', 'r') as openfile:
        json_object = json.load(openfile)
    global AVGLines
    global AVGStanzas
    global AVGWordsPerLine
    AVGLines = json_object["Averages"]["Lines"]
    AVGStanzas = json_object["Averages"]["Stanzas"]
    AVGWordsPerLine = json_object["Averages"]["WordsPerLine"]
    with open('usedSongs.json', 'r') as openfile:
        json_object = json.load(openfile)
    global usedSongs
    usedSongs = json_object["UsedSongs"]

main()