import os

def linker():
    outPutFile = open('main.js', 'w', encoding = 'UTF-8')

    # TODO: transfer to json
    # directories in witch files for linking are located
    linkedDirs = {
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



def getFilePathForDirAndName(dir, file):
    return str(str(dir) + '/' + str(file))


def linkFinalFileWithOutPutFile(filePath, outPutFile):
    if( (getFileExtension(filePath) == ".js") and (os.path.basename(filePath) != 'main.js') ):
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

linker()
