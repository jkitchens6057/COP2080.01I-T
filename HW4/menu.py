from run_bash_cmd_function import *

class Menu:

    '''
    A menu displayed in the terminal

    attributes:
        _options: private list
        _input: private string
    
    methods:
        __init__(self): creates a menu object
        addOption(self,option): adds an option to the _options list
        getInput(self): receives, validates, and processes user input; return True or False to determine program continuation
    '''

    # creates a menu object, with empty string and input attributes
    def __init__(self):
        self._options = []
        self._input = ""

    # takes an input option and adds it to the _options list
    def addOption(self,option):
        self._options.append(option)

    # receives user input and processes it
    def getInput(self):
        # printing of options
        for n in range(len(self._options)):
            print(f"{n+1}. {self._options[n]}")
        # receiving of input
        self._input = input().upper()

        # input validation
        if (self._input != 'Q') and ((not self._input.isdigit()) or (int(self._input) > len(self._options)) or (int(self._input) < 1)):
            print("Please input the integer value corresponding to the option.")
        else:
            # exits the program if the input is quit
            if self._input == 'Q' or int(self._input) == 4:
                return False
            else:
                # runs the matching bash command
                run_bash_cmd(int(self._input))

        return True
    