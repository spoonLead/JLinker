import os
import sys
from pathlib import Path
import json


def linker():
    printHeader()
    makeGlobalVarsFromArgv()
    linked_dirs = makeLinkedDirsDic(LINKED_DIRS_PATH)
    toLink(linked_dirs)
    printFooter()


def printHeader():
    print("  --- Start linking ---")
    print("\n *Files have been linked: \n")


def printFooter():
    print("\n --- Linking complete ---")


def makeGlobalVarsFromArgv():
    global FINAL_FILE_EXTENTION
    global OUTPUT_FILE_NAME
    global LINKED_DIRS_PATH

    if len(sys.argv) > 2:
        FINAL_FILE_EXTENTION = sys.argv[1]
        OUTPUT_FILE_NAME = sys.argv[2]
        LINKED_DIRS_PATH = sys.argv[3]
    else:
        FINAL_FILE_EXTENTION = ".js"
        OUTPUT_FILE_NAME = "main.js"
        LINKED_DIRS_PATH = './linked_dirs'


def makeLinkedDirsDic(LINKED_DIRS_PATH):
    # directories in which files for linking are located
    if os.path.exists(LINKED_DIRS_PATH):
        with open(LINKED_DIRS_PATH, 'r') as fh:
            linkedDirs = json.load(fh)
    else:
        print("Linked dir file not found! default values will be used.")

        linkedDirs = {
            "engine": './engine',
            "graphics": './graphics',
            "game": './game'
        }
    return linkedDirs


def toLink(linkedDirs):
    outPutFile = open(OUTPUT_FILE_NAME, 'w', encoding='UTF-8')
    for dir in linkedDirs.values():  # iteration for all directories in linkedDirs{}
        for subDir in os.walk(dir):  # iteration for all subdirectories
            for finalFile in subDir[2]:  # iteration for all destination files
                filePath = getFilePathForDirAndName(dir, finalFile)
                linkFinalFileWithOutPutFile(filePath, outPutFile)
                printRelativePathForFile(filePath)
    outPutFile.close()


def getFilePathForDirAndName(dir, fileName):
    return str(str(dir) + '/' + str(fileName))


def linkFinalFileWithOutPutFile(filePath, outPutFile):
    if ((getFileExtension(filePath) == FINAL_FILE_EXTENTION) and (os.path.basename(filePath) != OUTPUT_FILE_NAME)):
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
