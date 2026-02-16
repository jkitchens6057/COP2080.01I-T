from menu import *

# menu object
mainMenu = Menu()

# adding options to the menu
mainMenu.addOption("Check Available Memory")
mainMenu.addOption("View Network Connections")
mainMenu.addOption("Display Free RAM and Swap")
mainMenu.addOption("Quit")

# runs the program until told to stop
run = True
while run:
    run = mainMenu.getInput()