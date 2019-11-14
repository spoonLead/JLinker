# JLinker
Linker for JavaScipt files

### What Linker do?
Linker puts the text of multiple files into a single output file 

### For what?
For example, if you want to split your large JS file into several small files. This can be useful if you have a large project that needs to be sorted into files. You can put your classes in their own files. This allows you to create a more clear project structure.

However you can use this as you like

## How to use Linker?
In default Linker links files in directories(dirs) 'engine', 'graphics', 'game' and their subdirectories. Linker have to be in same dirs as the 'engine', 'graphics' and 'game'. If you want to change this, you have to edit linkedDirs in linker.py.

To start the linker you have to install python and write in the console: "python3 *path to your linker.py*" (for linux|Mac) or "py *path to your linker.py*" (for Windows). You can use absolute or relative path. 

For example: "py GCup/source/game/linker.py."

## How to set your linking parametres?
You can use console arguments at starting linker this way: "py *linker.py path* *extention of files you should link* *name with extention of output file*".

For example: "py GCup/source/game/linker.py. .js myOutPutFile.js"

For example: "py GCup/source/game/linker.py. .txt myFile.txt"

For example: "py GCup/source/game/linker.py. .js codeText.txt"
