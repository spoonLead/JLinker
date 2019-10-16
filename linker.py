import os
import sys
from pathlib import Path

# TODO: transfer to json
global linkedDirs       # directories in witch files for linking are located
linkedDirs = {
    "engine" : './engine',
    "graphics" : './graphics',
    "game" : './game'
}


def linker():
    printHeader()
    makeGlobalVarsFromArgv()
    toLink()
    printFooter()

def printHeader():
    print("  --- Start linking ---")
    print("\n *Files have been linked: \n")

def printFooter():
    print("\n --- Linking complete ---")


def makeGlobalVarsFromArgv():
    global FINAL_FILE_EXTENTION
    global OUTPUT_FILE_NAME

    if len (sys.argv) > 2:
        FINAL_FILE_EXTENTION = sys.argv[1]
        OUTPUT_FILE_NAME = sys.argv[2]
    else:
        FINAL_FILE_EXTENTION = ".js"
        OUTPUT_FILE_NAME = "main.js"


def toLink():
    outPutFile = open(OUTPUT_FILE_NAME, 'w', encoding = 'UTF-8')
    for dir in linkedDirs.values():              # iteration for all directories in linkedDirs{}
        for subDir in os.walk(dir):              # iteration for all subdirectories
            for finalFile in subDir[2]:          # iteration for all destination files
                filePath = getFilePathForDirAndName(dir, finalFile)
                linkFinalFileWithOutPutFile(filePath, outPutFile)
                printRelativePathForFile(filePath)
    outPutFile.close()         # close output file



def getFilePathForDirAndName(dir, fileName):
    return str(str(dir) + '/' + str(fileName))


def linkFinalFileWithOutPutFile(filePath, outPutFile):
    if( (getFileExtension(filePath) == FINAL_FILE_EXTENTION) and (os.path.basename(filePath) != OUTPUT_FILE_NAME) ):
        outPutFile.write(getTextFromFile(filePath))

def getFileExtension(filePath):
    return Path(filePath).suffix

def getTextFromFile(filePath):
    linkableFile = open(filePath, mode = 'r',encoding = 'UTF-8')
    codeString = linkableFile.read() + '\n'                                       #add to output code string new code from linkable file
    linkableFile.close()
    return codeString


def printRelativePathForFile(filePath):
    print(' ' + filePath)

linker()
