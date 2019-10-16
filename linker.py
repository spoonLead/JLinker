import os
from pathlib import Path


#LINKER METHOD
def toLink(dir, file):
    outCodeString = ''      #output 0615code string which will be placed into ouput file
    if file != 'linker.py' and file!= 'main.js':
        linkableFile = open(str(dir)+'/'+str(file), mode = 'r',encoding = 'UTF-8')      #open file for link
        outCodeString += linkableFile.read()+'\n'                                       #add to output code string new code from linked file
        linkableFile.close()                                                            #close file for link
    outFile.write(outCodeString)



def linkFile(dir, file):
    if(getFileExtension(file) == ".js"):
        toLink(subDir[0], file)

def getFileExtension(file):
    return Path(file).suffix



def printRelativePathForFile(dir, file):
    print(str(dir)+'/'+str(file))



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
            linkFile(dir, finalFile)
            printRelativePathForFile(dir, finalFile)

outFile.close()         #close output file
