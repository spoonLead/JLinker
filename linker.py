import os
import sys
from pathlib import Path
import json


def linker():
    printHeader()
    makeGlobalVarsFromArgv()
    linkFilesInDirs(getLinkedDirsDic())
    printFooter()



def printHeader():
    print("  --- Start linking ---")
    print("\n *Files have been linked: \n")

def printFooter():
    print("\n --- Linking complete ---")





def makeGlobalVarsFromArgv():
    global LINKABLE_FILES_EXTENSION
    global FULL_NAME_OUTPUT_FILE
    global LINKED_DIRS_FILE_NAME

    if len(sys.argv) == 4:
        LINKABLE_FILES_EXTENSION = sys.argv[1]
        FULL_NAME_OUTPUT_FILE = sys.argv[2]
        LINKED_DIRS_FILE_NAME = sys.argv[3]
    else:
        LINKABLE_FILES_EXTENSION = ".js"
        FULL_NAME_OUTPUT_FILE = "main.js"





def getLinkedDirsDic():
    # directories in which files for linking are located
    if os.path.exists(LINKED_DIRS_FILE_NAME):
        linkedDirs = getDataFromJSON('./' + LINKED_DIRS_FILE_NAME)
    else:
        print("JSON file with linked directories not found! Default values will be used. \n")
        linkedDirs = getDataFromJSON('./default_linked_dirs.json')
    return linkedDirs

def getDataFromJSON(JSON):
    with open(JSON, 'r') as file:
        return(json.load(file))





def linkFilesInDirs(linkedDirs):
    outPutFile = open(FULL_NAME_OUTPUT_FILE, 'w', encoding = 'UTF-8')
    for dir in linkedDirs.values():              # iteration for all directories in linkedDirs{}
        for subDir in os.walk(dir):              # iteration for all subdirectories
            for finalFile in subDir[2]:          # iteration for all destination files
                filePath = getFilePathForDirAndName(subDir, finalFile)
                linkFinalFileWithOutPutFile(filePath, outPutFile)
                printRelativePathForFile(filePath)
    outPutFile.close()



def getFilePathForDirAndName(subDir, fileName):
    return str(str(subDir[0]) + "/" + str(fileName))



def linkFinalFileWithOutPutFile(filePath, outPutFile):
    if ((getFileExtension(filePath) == LINKABLE_FILES_EXTENSION) and (os.path.basename(filePath) != FULL_NAME_OUTPUT_FILE)):
        outPutFile.write(getTextFromFile(filePath))

def getFileExtension(filePath):
    return Path(filePath).suffix

def getTextFromFile(filePath):
    linkableFile = open(filePath, mode='r', encoding='UTF-8')
    codeString = linkableFile.read() + '\n'  # add to output code string new code from linkable file
    linkableFile.close()
    return codeString



def printRelativePathForFile(filePath):
    print(' ' + filePath)


linker()
