import os
from pathlib import Path




def getFilePath(dir, file):
    return str(str(dir) + '/' + str(file))


def linkFile(filePath):
    if(getFileExtension(filePath) == ".js"):
        toLink(filePath)

def getFileExtension(filePath):
    return Path(filePath).suffix

#LINKER METHOD
def toLink(filePath):
    outCodeString = ''      #output 0615code string which will be placed into ouput file
    if os.path.basename(filePath) != 'main.js':
        linkableFile = open(filePath, mode = 'r',encoding = 'UTF-8')      #open file for link
        outCodeString += linkableFile.read()+'\n'                                       #add to output code string new code from linked file
        linkableFile.close()                                                            #close file for link
    outFile.write(outCodeString)


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
            filePath = getFilePath(dir, finalFile)
            linkFile(filePath)
            printRelativePathForFile(filePath)

outFile.close()         #close output file
