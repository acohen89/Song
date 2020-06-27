import requests
import json

def main():
   readAndSave()
   #r = requests.get("https://www.rocknrollamerica.net/Top1000.html")
   #li =  list(r.text)
   listOfSongs = []
   """for i in range(len(li)): #Gathers list of songs
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
        listOfSongs.append(tempStr) """
   testList = ["Stairway to Heaven"]
   for i in testList: #Check if song has already been used
       if not(i in usedSongs):
           #create query url
           sUrl = getSearchURL(i)[0]
           songName = getSearchURL(i)[1]
           q = requests.get(sUrl)
           f = open("textDump.txt", "w")
           f.write(str(q.text.split()))
           f.close
           lURL = ""
           done = False
           if not done:
               for k in q.text.split():
                   if songName in k:
                       for l in range(len(k)):
                           if len(k) >= l+8:
                               if k[l] == "h" and k[l+1] == "t"  and k[l+2] == "t" and k[l+3] == "p":
                                   finished = False
                                   while not finished and not done:
                                       if (len(k) - 4) < 0: #Making sure next call does not throw index out of bounds exception
                                           print("error")
                                           finished = True
                                       else:
                                           if k[l-1] == "l" and k[l-2] == "m" and k[l-3] == "t" and k[l-4] == "h":
                                               finished = True
                                               done = True
                                           else:
                                               lURL += k[l]
                                               l += 1

           print(lURL)
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
def getSearchURL(song):
    qUrl = "https://search.azlyrics.com/search.php?q="
    tempWP = ""
    temp = ""
    li = list(song.split())
    for i in range(len(li)):
        temp += li[i]
        if i == (len(li) - 1):
            tempWP += li[i]
        else:
            tempWP += li[i] + "+"
    return [qUrl+tempWP, temp.lower()]
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