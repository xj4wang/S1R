import os
import csv
raw_input=input
from sortedcontainers import SortedDict

def getCategories(mainDir):
    categories = []
    category1 = {}
    category2 = {}
    category3 = {}
    category4 = {}
    categories.append(category1)
    categories.append(category2)
    categories.append(category3)
    categories.append(category4)

    for i in range(4):
        categoryFile = open(mainDirectory + "/category"+str(i+1)+".txt", "r")
        for line in categoryFile:
            categories[i][line.replace('\n','')] = ["",""]
        categoryFile.close()

    return categories


def calculateBlock(blockDirectory, num, categoriesList, avg, bList):
    blockDirectoryFiles = os.listdir(blockDirectory)
    
    
    for i in range(len(blockDirectoryFiles)):
        if(blockDirectoryFiles[i].endswith('.TextGrid')):

            fileName = blockDirectoryFiles[i].split(".")
        
            fileDirectory = blockDirectory + "/" + blockDirectoryFiles[i]
            file = open(fileDirectory,"r")
            fileContents = file.read()
            fileContentsList = fileContents.split()
            print(blockDirectory)
            print(blockDirectoryFiles[i])
            fileContentsList = [k for k in fileContentsList if (k != '""' and k != '"' and k != '"-"'and k != '"`"')]
            VoT = float(fileContentsList[66]) - float(fileContentsList[53])
            avg[0] += VoT
            avg[1] += 11

            
            for dictIndex in range(4):
                if(fileName[0] in categoriesList[dictIndex]):
                    temp = categoriesList[dictIndex][fileName[0]]
                    temp[num] = VoT
                    categoriesList[dictIndex][fileName[0]] = temp
                    if(fileName[0] in bList):
                        bList[fileName[0]][num] = int(num+1)
                    else:
                        bList[fileName[0]] = ["",""]
                        bList[fileName[0]][num] = int(num+1)
                    break


            file.close()
    
    return categoriesList

def createRFormat(subjectID, categoriesList, avg, bList, groupNum):
    headerList = ["Subject", "Cond_race", "Cond_acce","Group", "Item", "Vot Score", "Block", "Category", "Extra", "Word duration"]
    fileName = subjectID + "_R.csv"

    vot2List = []
    
    if(avg[1] != 0):
        with open(fileName, 'w') as csvfile:
            csvFileWriter = csv.writer(csvfile, delimiter=',')
            csvFileWriter.writerow(headerList)

            categoriesList[0] = SortedDict(categoriesList[0])
            while(len(categoriesList[0]) > 0 ):
                rowList= []
                key = next(iter(categoriesList[0]))
                temp = categoriesList[0][key]
                #Vot1 List if(temp[0] != ""):

                rowList.append(subjectID)
                rowList.append("")
                rowList.append("")
                rowList.append(groupNum)
                rowList.append(key)
                rowList.append(temp[0])
                rowList.append("1")    
                rowList.append("1")
                rowList.append("")
                rowList.append("")
                csvFileWriter.writerow(rowList)

                #Vot2 List if(temp[1] != ""):
                vot2List.append(key)
                vot2List.append(temp[1])
                vot2List.append("2")  
                vot2List.append("1")
                categoriesList[0].pop(key, None)

                                           
            categoriesList[1] = SortedDict(categoriesList[1])
            tempRow = []
            tempVot2List = []
            while(len(categoriesList[1]) > 0):
                rowList= []
                key = next(iter(categoriesList[1]))
                temp = categoriesList[1][key]
                
                if(key != "TV"):
                    rowList.append(subjectID)
                    rowList.append("")
                    rowList.append("")
                    rowList.append(groupNum)
                    rowList.append(key)
                    rowList.append(temp[0])
                    rowList.append("1")  
                    rowList.append("2")
                    rowList.append("")
                    rowList.append("")
                    csvFileWriter.writerow(rowList)
                    
                    
                    vot2List.append(key)
                    vot2List.append(temp[1])
                    vot2List.append("2")  
                    vot2List.append("2")
                    categoriesList[1].pop(key, None)
                else:
                    tempRow.append(subjectID)
                    tempRow.append("")
                    tempRow.append("")
                    tempRow.append(groupNum)
                    tempRow.append(key)
                    tempRow.append(temp[0])
                    tempRow.append("1")  
                    tempRow.append("2")
                    tempRow.append("")
                    tempRow.append("")
                    

                    tempVot2List.append(key)
                    tempVot2List.append(temp[1])
                    tempVot2List.append("2")  
                    tempVot2List.append("2")
                    categoriesList[1].pop(key, None)

            if(len(tempRow) > 0):
                csvFileWriter.writerow(tempRow)
                for x in range(len(tempVot2List)):
                    vot2List.append(tempVot2List[x])



            categoriesList[2] = SortedDict(categoriesList[2])
            tempRow = []
            tempVot2List = []
            while(len(categoriesList[2]) > 0):
                rowList= []
                key = next(iter(categoriesList[2]))
                temp = categoriesList[2][key]

                if(key != "baby"):
                    rowList.append(subjectID)
                    rowList.append("")
                    rowList.append("")
                    rowList.append(groupNum)
                    rowList.append(key)
                    rowList.append(temp[0])
                    rowList.append("1")  
                    rowList.append("3")
                    rowList.append("")
                    rowList.append("")
                    csvFileWriter.writerow(rowList)
                
                
                    vot2List.append(key)
                    vot2List.append(temp[1])
                    vot2List.append("2")  
                    vot2List.append("3")
                    categoriesList[2].pop(key, None)

                else:
                    tempRow.append(subjectID)
                    tempRow.append("")
                    tempRow.append("")
                    tempRow.append(groupNum)
                    tempRow.append(key)
                    tempRow.append(temp[0])
                    tempRow.append("1")    
                    tempRow.append("3")
                    tempRow.append("")
                    tempRow.append("")

                    #Vot2 List if(temp[1] != ""):
                    tempVot2List.append(key)
                    tempVot2List.append(temp[1])
                    tempVot2List.append("2")  
                    tempVot2List.append("3")
                    categoriesList[2].pop(key, None)

            if(len(tempRow) > 0):
                csvFileWriter.writerow(tempRow)
                for x in range(len(tempVot2List)):
                    vot2List.append(tempVot2List[x])



            categoriesList[3] = SortedDict(categoriesList[3])
            while(len(categoriesList[3]) > 0):
                rowList= []
                key = next(iter(categoriesList[3]))
                temp = categoriesList[3][key]
                
                rowList.append(subjectID)
                rowList.append("")
                rowList.append("")
                rowList.append(groupNum)
                rowList.append(key)
                rowList.append(temp[0])
                rowList.append("1")  
                rowList.append("4")
                rowList.append("")
                rowList.append("")
                csvFileWriter.writerow(rowList)
            
            
                vot2List.append(key)
                vot2List.append(temp[1])
                vot2List.append("2")  
                vot2List.append("4")
                categoriesList[3].pop(key, None)

                

            


            if(len(vot2List) > 0):
                i = 0
                while( i < int(len(vot2List))):
                    rowList = []
                    rowList.append(subjectID)
                    rowList.append("")
                    rowList.append("")
                    rowList.append(groupNum)
                    rowList.append(vot2List[i])
                    rowList.append(vot2List[i+1])
                    rowList.append(vot2List[i+2])
                    rowList.append(vot2List[i+3])
                    rowList.append("")
                    rowList.append("")
                    csvFileWriter.writerow(rowList)
                    i += 4
                    
            
        
                


        
def createCSV(subjectID, categoriesList, avg):
    headerList = ["Subject", "Words:", "Category 1", "VOT 1", "VOT 2", "Category 2", "VOT 1", "VOT 2", "Category 3", "VOT 1", "VOT 2", "Category 4", "VOT 1", "VOT 2"]
    fileName = subjectID + "_Table.csv"

    if(avg[1] != 0):
        with open(fileName, 'w') as csvfile:
            csvFileWriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
            csvFileWriter.writerow(headerList)
            rowList = [subjectID, ""]
            
            
            while(len(categoriesList[0]) > 0 or len(categoriesList[1]) > 0 or len(categoriesList[2]) > 0 or len(categoriesList[3]) > 0):
                
                if(len(categoriesList[0]) > 0):
                    key = next(iter(categoriesList[0]))
                    rowList.append(key)
                    temp = categoriesList[0][key]
                    rowList.append(temp[0])
                    rowList.append(temp[1])
                    categoriesList[0].pop(key, None)
                else:
                    rowList.append("")
                    rowList.append("")
                    rowList.append("")
                
                if(len(categoriesList[1]) > 0):
                    key = next(iter(categoriesList[1]))
                    rowList.append(key)
                    temp = categoriesList[1][key]
                    rowList.append(temp[0])
                    rowList.append(temp[1])
                    categoriesList[1].pop(key, None)
                else:
                    rowList.append("")
                    rowList.append("")
                    rowList.append("")

                if(len(categoriesList[2]) > 0):
                    key = next(iter(categoriesList[2]))
                    rowList.append(key)
                    temp = categoriesList[2][key]
                    rowList.append(temp[0])
                    rowList.append(temp[1])
                    categoriesList[2].pop(key, None)
                else:
                    rowList.append("")
                    rowList.append("")
                    rowList.append("")

                if(len(categoriesList[3]) > 0):
                    key = next(iter(categoriesList[3]))
                    rowList.append(key)
                    temp = categoriesList[3][key]
                    rowList.append(temp[0])
                    rowList.append(temp[1])
                    categoriesList[3].pop(key, None)
                    
                else:
                    rowList.append("")
                    rowList.append("")
                    rowList.append("")
                
                csvFileWriter.writerow(rowList)
                rowList = ["",""]
            
            
            csvFileWriter.writerow(rowList)
            subjectAverage = avg[0]/avg[1]
            rowList = ["Subject Average:", subjectAverage]
            csvFileWriter.writerow(rowList)
        
        


mainDirectory = os.getcwd()

mainDirectoryFiles = os.listdir(mainDirectory)

mode = raw_input("Enter 1 for Table form or 2 for R Format: ").strip()

while(mode != "1" and mode != "2"):
    mode = raw_input("Enter 1 for Table form or 2 for R Format: ").strip()
    


for i in range(len(mainDirectoryFiles)):
    if(os.path.isdir(mainDirectoryFiles[i])):
        blockList = []

        if("-" in str(mainDirectoryFiles[i])):
            subjectID = str(mainDirectoryFiles[i]).split("-")
            groupNum = subjectID[2].strip()
            subjectID = subjectID[0].strip()
            
        else:
            subjectID = mainDirectoryFiles[i]
            groupNum = 0
        print("Subject: " +subjectID)
    
        subjectDirectory = mainDirectory + "/" + mainDirectoryFiles[i]
        subjectDirectoryFiles = os.listdir(subjectDirectory)
        
        categoriesList = getCategories(mainDirectory)
        avg = [0, 0]
        blockDictL = {}
        for j in range(len(subjectDirectoryFiles)):
            blockDirectory = subjectDirectory + "/" + subjectDirectoryFiles[j]
            categoriesList = calculateBlock(blockDirectory, j, categoriesList, avg, blockDictL)


        if(mode == "1"):
            createCSV(subjectID, categoriesList, avg)
            
        else:
            createRFormat(subjectID, categoriesList, avg, blockDictL, groupNum)

        
    else:
        print(str(mainDirectoryFiles[i]) +" isn't a directory.")


