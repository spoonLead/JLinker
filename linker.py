import os
import sys
from pathlib import Path
import json


# Linking params
# Global vars for linking and their default values
LINKABLE_FILES_EXTENSION = ".js"
OUTPUT_FILE = "../main.js"
LINKED_DIRS_FILE_NAME = "default_linked_dirs.json"
LINKING_FOR_FINAL_FILES = False



def linker():
    printHeader()
    toLinkAccordingArgv()
    printFooter()




def printHeader():
    print("  --- Start linking ---")
    print("\n Files have been linked: \n")

def printFooter():
    print("\n --- Linking complete ---")




def toLinkAccordingArgv():
    setLinkingParamFromArgv()
    toLink()


def setLinkingParamFromArgv():
    global LINKABLE_FILES_EXTENSION
    global OUTPUT_FILE
    global LINKED_DIRS_FILE_NAME
    global LINKING_FOR_FINAL_FILES

    if len(sys.argv) >= 4:
        LINKABLE_FILES_EXTENSION = sys.argv[1]
        OUTPUT_FILE = sys.argv[2]
        LINKED_DIRS_FILE_NAME = sys.argv[3]
        if (len(sys.argv) == 5) and (sys.argv[4] == "fl"):
            LINKING_FOR_FINAL_FILES = True


def toLink():
    if LINKING_FOR_FINAL_FILES:
        linkFinalFiles(getFinalFilesDic())
    else:
        linkFilesInDirs(getLinkedDirsDic())







def getFinalFilesDic():
    if os.path.exists(LINKED_DIRS_FILE_NAME):
        finalFiles = getDataFromJSON(LINKED_DIRS_FILE_NAME)
    else:
        print("Json with linkable files not found")
        finalFiles = {}
    return finalFiles




def getLinkedDirsDic():
    # directories in which files for linking are located
    if os.path.exists(LINKED_DIRS_FILE_NAME):
        linkedDirs = getDataFromJSON(LINKED_DIRS_FILE_NAME)
    else:
        print("JSON file with linked directories not found! Default values will be used. \n")
        linkedDirs = getDataFromJSON('default_linked_dirs.json')
    return linkedDirs

def getDataFromJSON(JSON):
    with open(JSON, 'r') as file:
        return(json.load(file))







def linkFinalFiles(finalFiles):
    outPutFile = open(OUTPUT_FILE, 'w', encoding = 'UTF-8')
    for fileAnnotation, filePath in finalFiles.items():
        linkFinalFileWithOutPutFile(filePath, outPutFile)
        printAnnotationAndPathWithSplit(fileAnnotation, filePath, 30)
    outPutFile.close()



def linkFilesInDirs(linkedDirs):
    outPutFile = open(OUTPUT_FILE, 'w', encoding = 'UTF-8')
    for dir in linkedDirs.values():              # iteration for all directories in linkedDirs{}
        for subDir in os.walk(dir):              # iteration for all subdirectories
            for finalFile in subDir[2]:          # iteration for all destination files
                filePath = getFilePathForDirAndName(subDir, finalFile)
                linkFinalFileWithOutPutFile(filePath, outPutFile)
                printRelativeFilePath(filePath)
    outPutFile.close()





def getFilePathForDirAndName(subDir, fileName):
    return str(str(subDir[0]) + "/" + str(fileName))



def linkFinalFileWithOutPutFile(filePath, outPutFile):
    if ((getFileExtension(filePath) == LINKABLE_FILES_EXTENSION) and (os.path.basename(filePath) != OUTPUT_FILE)):
        outPutFile.write(getTextFromFile(filePath))

def getFileExtension(filePath):
    return Path(filePath).suffix

def getTextFromFile(filePath):
    linkableFile = open(filePath, mode='r', encoding='UTF-8')
    fileText = linkableFile.read() + '\n'  # String with all text from file
    linkableFile.close()
    return fileText








def printAnnotationAndPathWithSplit(fileAnnotation, filePath, split):
    printingString = " - "
    printingString += fileAnnotation
    for i in range(0, split-len(fileAnnotation)):
        printingString += " "
    printingString += filePath
    print(printingString)

def printRelativeFilePath(filePath):
    print(" " + filePath)



linker()
