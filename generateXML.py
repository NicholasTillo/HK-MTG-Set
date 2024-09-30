import json

def getJSONpath():
    return "justJSON.json"





def createCards(outputFile):
    with open(getJSONpath(), "r") as jsonFile:
        loadedJson = json.load(jsonFile)
        setcounter = 0
        for card in loadedJson["AllEntities"]:
            outputFile.write("<card>\n")
            outputFile.write("<name>"+card["name"]+"</name>\n")
            outputFile.write("<text> NA </text>\n")
            outputFile.write("<prop>\n")



            outputFile.write("<layout>normal</layout>\n")
            outputFile.write("<side>front</side>\n")

            if "subtypes" in card:
                subtypeStr = " ---"
                for subtype in card["subtypes"]:
                    subtypeStr += " " + subtype
            else:
                subtypeStr = ""


            outputFile.write("<type>"+card["type"] + subtypeStr +"</type>\n")
            outputFile.write("<maintype>"+card["type"].replace("Legendary ", "") +"</maintype>\n")
            
            cleanManaValue = card["mana_cost"].replace("{","").replace("}","")
            outputFile.write("<manacost>"+ cleanManaValue + "</manacost>\n")
        
            counter = 0
            colorIdentity = ""
            for char in cleanManaValue:
                if char.isdigit():
                    counter += int(char)
                else:
                    counter += 1
                    if char not in colorIdentity:
                        colorIdentity += char

            outputFile.write("<cmc>"+str(counter)+"</cmc>\n")

            
            outputFile.write("<colors>"+colorIdentity+"</colors>\n")
            outputFile.write("<coloridentity>"+colorIdentity+"</coloridentity>\n")

            outputFile.write("<pt> NA </pt>\n")
            outputFile.write("<loyalty> NA </loyalty>\n")

            outputFile.write("<format-standard>legal</format-standard>\n")
            outputFile.write("<format-commander>legal</format-commander>\n")
            outputFile.write("<format-modern>legal</format-modern>\n")
            outputFile.write("<format-pauper>legal</format-pauper>\n")


            setcounter += 1
            outputFile.write("</prop>\n")
            outputFile.write("<set rarity=\""+card["rarity"]+"\" num=\""+str(setcounter)+"\" picurl=\""+card["image"]+"\" >HOK</set>\n")
            #uuid and muid are both not here. 
            outputFile.write("</card>\n")

            
        

with open('Hallownest.xml', 'w') as xmlFile:
    xmlFile.writelines(['<?xml version="1.0" encoding="UTF-8"?> \n','<cockatrice_carddatabase version="4">\n','<sets>\n','<set>\n','<name>HOK</name>\n', '<longname>Hollow Knight Set</longname>\n','<settype>Custom</settype>\n','<releasedate>2022-11-25</releasedate>\n','</set>\n','</sets>\n','<cards>\n'])
    
    
    createCards(xmlFile)


    xmlFile.writelines(['</cards>\n','</cockatrice_carddatabase>'])