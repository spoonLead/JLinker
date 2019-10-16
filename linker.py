import os
from pathlib import Path




def getFilePathForDirAndName(dir, file):
    return str(str(dir) + '/' + str(file))


def linkFile(filePath):
    if( (getFileExtension(filePath) == ".js") and (os.path.basename(filePath) != 'main.js') ):
        toLink(filePath)

def getFileExtension(filePath):
    return Path(filePath).suffix


def getTextFromFile(filePath):
    codeString = ''
    linkableFile = open(filePath, mode = 'r',encoding = 'UTF-8')
    codeString += linkableFile.read()+'\n'                                       #add to output code string new code from linked file
    linkableFile.close()
    return codeString

#LINKER METHOD
def toLink(filePath):
    outFile.write(getTextFromFile(filePath))


def printRelativePathForFile(filePath):
    print(filePath)



#output file
outFile = open('main.js', 'w', encoding = 'UTF-8')

#dictionary of start directories of link files
linkedDirs = {
    "engine" : './engine',
    "graphics" : './graphics',
    "game" : './game'
}

for dir in linkedDirs.values():             #iteration for all directories in linkedDirs{}
    for subDir in os.walk(dir):             #iteration for all subdirectories
        for finalFile in subDir[2]:          #iteration for all destination files
            filePath = getFilePathForDirAndName(dir, finalFile)
            linkFile(filePath)
            printRelativePathForFile(filePath)

outFile.close()         #close output file
