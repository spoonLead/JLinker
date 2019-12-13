import os
import sys
from pathlib import Path
import json


# Linking params
# Global vars for linking and their default values
LINKABLE_FILES_EXTENSION = ".js"
OUTPUT_FILE = "../main.js"
LINKING_MAP_FILE = "default_linked_dirs.json"
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
    global LINKING_MAP_FILE
    global LINKING_FOR_FINAL_FILES

    if len(sys.argv) >= 4:
        LINKABLE_FILES_EXTENSION = sys.argv[1]
        OUTPUT_FILE = sys.argv[2]
        LINKING_MAP_FILE = sys.argv[3]
    if len(sys.argv) >= 5:
        if sys.argv[4] == "f":
            LINKING_FOR_FINAL_FILES = True


def toLink():
    if LINKING_FOR_FINAL_FILES:
        linkForFinalFiles(getLinkingMapFromFile(LINKING_MAP_FILE))
    else:
        linkForFilesInDirs(getLinkingMapFromFile(LINKING_MAP_FILE))







def getLinkingMapFromFile(filePath):
    try:
        return tryGetLinkingMap(filePath)
    except ValueError:
        logJSONDecodeError()
    except FileNotFoundError:
        logFileNotFoundError()
    return {}

def tryGetLinkingMap(filePath):
    finalFiles = getDataFromJSON(filePath)
    return finalFiles


def logJSONDecodeError():
    print(" Error: Wrong format of JSON file")

def logFileNotFoundError():
    print(" JSON with linking map not found")

def getDataFromJSON(JSON):
    with open(JSON, 'r') as file:
        return(json.load(file))







def linkForFinalFiles(finalFiles):
    outPutFile = open(OUTPUT_FILE, mode = 'w', encoding = "UTF-8")
    for fileAnnotation, filePath in finalFiles.items():
        linkFinalFileWithOutPutFile(filePath, outPutFile)
        printAnnotationAndPathWithSplit(fileAnnotation, filePath, 30)
    outPutFile.close()



def linkForFilesInDirs(linkedDirs):
    outPutFile = open(OUTPUT_FILE, mode = 'w', encoding = "UTF-8")
    for dir in linkedDirs.values():              # iteration for all directories in linkedDirs{}
        for subDir in os.walk(dir):              # iteration for all subdirectories
            for finalFile in subDir[2]:          # iteration for all destination files
                filePath = getFilePathForDirAndName(subDir, finalFile)
                linkFinalFileWithOutPutFile(filePath, outPutFile)
                printRelativeFilePath(filePath)
    outPutFile.close()





def getFilePathForDirAndName(subDir, fileName):
    return str(str(subDir[0]) + '/' + str(fileName))



def linkFinalFileWithOutPutFile(filePath, outPutFile):
    if ((getFileExtension(filePath) == LINKABLE_FILES_EXTENSION) and (os.path.basename(filePath) != OUTPUT_FILE)):
        outPutFile.write(getTextFromFile(filePath))

def getFileExtension(filePath):
    return Path(filePath).suffix

def getTextFromFile(filePath):
    linkableFile = open(filePath, mode='r', encoding = "UTF-8")
    fileText = linkableFile.read() + '\n'  # String with all text from file
    linkableFile.close()
    return fileText








def printAnnotationAndPathWithSplit(fileAnnotation, filePath, split):
    printingString = " - " + fileAnnotation
    for i in range(0, split-len(fileAnnotation)):
        printingString += " "
    printingString += filePath
    print(printingString)

def printRelativeFilePath(filePath):
    print(" " + filePath)



linker()
