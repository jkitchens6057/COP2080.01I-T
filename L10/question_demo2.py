##
#  a simple quiz with two choice questions.
#

#from questions import ChoiceQuestion
from questions import *

def main() :
   
   first = Question()
   first.setText("Who was the inventor of Python?")
   first.setAnswer("Guido van Rossum")

   #first = ChoiceQuestion()
   #first.setText("In what year was the Python language first released?")
   #first.addChoice("1991", True)
   #first.addChoice("1995", False)
   #first.addChoice("1998", False)
   #first.addChoice("2000", False)
   

   second = ChoiceQuestion()
   second.setText("In which country was the inventor of Python born?")
   second.addChoice("Australia", False)
   second.addChoice("Canada", False)
   second.addChoice("Netherlands", True)
   second.addChoice("United States", False)

   presentQuestion(first)
   presentQuestion(second)

## Presents a question to the user and checks the response.
#  @param q the question
#
def presentQuestion(q) :
   print(q)
   response = input("Your answer: ")
   print(q.checkAnswer(response))

# Start the program.
# main()

class Menu:
   ## Constructs a menu with no options.
   #
   def __init__(self):
      self._options = []
   ## Adds an option to the end of menu.
   # @param option the option to add
   #
   def addOption(self, option):
      self._options.append(option)
   ## Displays the menu, with options numbered starting with 1, and prompts
   # the user for input. Repeats until a valid input is supplied.
   # @return the number that the user supplied
   #
   def getInput(self):
      done = False
      while not done:
         print('-' * 80, '\n')
         for i in range(len(self._options)):
            print("%d %s" % (i + 1, self._options[i]))
         userChoice = int(input())
         #if userChoice >= 1 and userChoice < len(self._options):
         if userChoice < 1 or userChoice > len(self._options):
            print('Enter a 1-4 only')
            continue
         #place holder
         else:
            done = True
            quit()
            return userChoice
def main():
   mainMenu = Menu()
   def buildOptions():
      mainMenu.addOption("one")
      mainMenu.addOption("two")
      mainMenu.addOption("three")
   buildOptions()
   choice = mainMenu.getInput()

if __name__ == '__main__':
   main()
