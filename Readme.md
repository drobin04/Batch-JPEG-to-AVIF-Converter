# Batch JPEG To Avif Context Menu Script

## Setup

* Right click the 'install context menu item.bat' file and select 'Run as Administrator'. This will add the right-click-menu / context menu item for this script. 

* Install Python if you don't already have it installed. 

* Install the ' pillow-avif-plugin ' package ( i.e ' pip install pillow-avif-plugin ' in a python manager window such as Anaconda3). This script references ' pillow_avif ', and needs to be installed via the ' pillow-avif-plugin ' name. 

That's it! Run the script!


## Important Notes 

* The context menu item WILL reference the location of the python script in this folder (And as such it references the current directory that the .bat file runs from ). This means that later deleting or moving the python file will break the context menu item. 

