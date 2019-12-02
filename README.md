# JLinker
Linker for JavaScipt files

### What Linker do?
Linker puts the text of multiple files into a single output file 

### For what?
For example, if you want to split your large JS file into several small files. This can be useful if you have a large project that needs to be sorted into files. You can put your classes in their own files. This allows you to create a more clear project structure.

However you can use this as you like

## How to install Linker to your project?
Just download archive from github and unzip them into your project

For example:
```
├─ index.html/      
├─ style.css/
├─ Game/
│  ├─ GameLevels/
│  ├─ Objects/
├─ ZEngine/     
│  ├─ EngObject/         
│  ├─ Tools/        
│  ├─ Init.js   
│  ├─ Scene.js          
└─ JLinker/
   ├─ linker.py/         
   ├─ default_linked_dirs.py/         
   └─ README.md/
```

## How to use Linker?
In default Linker links files in directories(dirs) 'engine', 'graphics', 'game' and their subdirectories. Linker have to be in same dirs as the 'engine', 'graphics' and 'game'. If you want to change this, you have to edit linkedDirs in linker.py.

To start the linker you have to install python and write in the console: "python3 *path to your linker.py*" (for linux|Mac) or "py *path to your linker.py*" (for Windows). You can use absolute or relative path. 
```
py GCup/source/game/linker.py.
```
## How to set your linking parametres?
### Setting directories with files for linking
**In this way Linker will use default params for directories** 
You can use console arguments at starting linker this way: py 'linker.py path' 'extention of files you should link' 'name with extention of output file'. 
```
py GCup/JLinker/linker.py. .js ../myOutPutFile.js
```
In this example linker will make GCup/myOutOutFile.js and put all code from js files in default linking directories

**For use your custom directories** you have to make .json file in JLinker dir and fill it like this:
```
{
     "engine": "../ZEngine",          In the first " " you can write anything. That just for your comfort in search
     "game": "../Game"
}
```
And then starting linker as in the previous example but with the specified of .json file with your dirs for linking
```
py GCup/JLinker/linker.py. .js ../myOutPutFile.js my_linking_dirs.json
```
