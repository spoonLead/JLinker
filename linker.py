import os

#output file
outFile = open('main.js', 'w', encoding = 'UTF-8')

#dictionary of start directories of link files
linkedDirs = {
    "engine" : './engine',
    "graphics" : './graphics',
    "game" : './game'
}

#LINKER METHOD
def toLink(dir, file):
    outCodeString = ''      #output 0615code string which will be placed into ouput file
    if file != 'linker.py' and file!= 'main.js':
        openFile = open(str(dir)+'/'+str(file), mode = 'r',encoding = 'UTF-8')      #open file for link
        outCodeString += openFile.read()+'\n'                                       #add to output code string new code from linked file
        openFile.close()                                                            #close file for link
    outFile.write(outCodeString)


def linkFile(dir, file):
    fileExtension = file.split('.')[1]       #split file name to name and extension for '.'
    #link files with only "js" destination
    if(fileExtension == "js"):
        toLink(subDir[0], file)
        print(str(dir)+'/'+str(file))


for dir in linkedDirs.values():             #iteration for all directories in linkedDirs{}
    for subDir in os.walk(dir):             #iteration for all subdirectories
        for finalFile in subDir[2]          #iteration for all destination files
            linkFile(dir, finalFile)

outFile.close()         #close output file
