"""Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case."""
class ForStrings():
    def __init__(self):
        self.gotstring = ''

    def getString(self):
        self.gotstring = input()

    def printString(self):
        print(self.gotstring.upper())


