import os
import json

#This file is used to replace the names of the images in the set to the corresponding names. 
#However I failed to realize that the names were already correct, and just needed a replacement. 
#So this code is mostly useless, 
#Might get picked back up if the names of the images dont match up in the future. 

def createJsonFromDraftmancerFile(paramInput, paramOutput):
    with open(paramInput, "r") as file:
        with open(paramOutput, "w") as jsonFile:
            flag = False
            jsonFile.write("{ \"AllEntities\" : [  \n")

            for i in file.readlines():
                i = i[:-1]
                if i == "#FLAG":
                    flag = not flag
                elif flag:
                    jsonFile.write(i +"\n")

            jsonFile.write("] \n} \n")


def ExtractNames(paramJSON, outputTXT):
    with open(paramJSON, "r") as jsonFile:
        Jser = json.load(jsonFile)
        with open(outputTXT, "w") as nameFile:
            for i in Jser["AllEntities"]:
                nameFile.write(i["name"] + "\n")
                
#Segment the names into files, becuase the list is in alphabetical order.
#  We can just scan for a reset in alphabetical order, and segment it there.           
def alphaSegmentFile(paramInput):
    with open(paramInput, "r") as nameFile:
        curr_first = "A"
        counter = 0
        targetFile = "Section"+str(counter)+".txt"
        writeTo = open(targetFile, "w")
        for i in nameFile.readlines():
            if curr_first > i[0]: 
                counter+= 1
                targetFile = "Section"+str(counter)+".txt"
                writeTo.close()
                writeTo = open(targetFile, "w")
            writeTo.write(i)
            curr_first = i[0]   


def makeSegments():
    createJsonFromDraftmancerFile("allCardsClone.txt", "justJSON.json")
    ExtractNames("justJSON.json", "JustNamesInOrder.txt")
    alphaSegmentFile("JustNamesInOrder.txt")


def getPath(section):
   
    if section == "white":
        return "C:/Users/Nicholas/Desktop/www.planesculptors.net-1727540147531/White"
    if section == "blue":
        return "C:/Users/Nicholas/Desktop/www.planesculptors.net-1727540147531/Blue"
    if section == "black":
        return "C:/Users/Nicholas/Desktop/www.planesculptors.net-1727540147531/Black"
    if section == "red":
        return "C:/Users/Nicholas/Desktop/www.planesculptors.net-1727540147531/Red"
    if section == "green":
        return "C:/Users/Nicholas/Desktop/www.planesculptors.net-1727540147531/Green"
    if section == "colourless":
        return "C:/Users/Nicholas/Desktop/www.planesculptors.net-1727540147531/Colourless"
    if section == "multi":
        return "C:/Users/Nicholas/Desktop/www.planesculptors.net-1727540147531/MultiColoured"

    
#This is the real thing that works. 
#Just replace the "%20" with a space, and itll work....
#Sigh.
def replaceWierdThing(path):
    dirlist = os.listdir(path)
    print(dirlist)
    for i in dirlist:
        temp = i.replace("%20", " ")
        os.rename(path+"/"+i, path+"/"+temp)

pathBlack = getPath("white")
replaceWierdThing(pathBlack)
pathBlack = getPath("blue")
replaceWierdThing(pathBlack)
pathBlack = getPath("black")
replaceWierdThing(pathBlack)
pathBlack = getPath("red")
replaceWierdThing(pathBlack)
pathBlack = getPath("green")
replaceWierdThing(pathBlack)
pathBlack = getPath("colourless")
replaceWierdThing(pathBlack)
pathBlack = getPath("multi")
replaceWierdThing(pathBlack)





        

