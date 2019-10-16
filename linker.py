import os
from pathlib import Path

def linker(extention, outPutFileName):

    global FINAL_FILE_EXTENTION
    global OUTPUT_FILE_NAME
    FINAL_FILE_EXTENTION = extention
    OUTPUT_FILE_NAME = outPutFileName

    outPutFile = open(OUTPUT_FILE_NAME, 'w', encoding = 'UTF-8')

    # TODO: transfer to json
    # directories in witch files for linking are located
    linkableDirs = {
        "engine" : './engine',
        "graphics" : './graphics',
        "game" : './game'
    }

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
    print(filePath)
