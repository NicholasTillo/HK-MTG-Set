import os
import json


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
                
                
                
                
createJsonFromDraftmancerFile("allCardsClone.txt", "justJSON.json")
ExtractNames("justJSON.json", "JustNamesInOrder.txt")
with open("JustNamesInOrder.txt", "r") as nameFile:
    curr_first = "A"
    counter = 0
    targetFile = "Section"+str(counter)+".txt"
    writeTo = open(targetFile, "w")
    for i in nameFile.readlines():
        if curr_first < i[0]: 
            counter+= 1
            targetFile = "Section"+str(counter)+".txt"
            writeTo.close()
            writeTo = open(targetFile, "w")
        writeTo.write(i)

        

