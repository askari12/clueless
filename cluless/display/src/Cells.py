# LIST OF CELLS THAT HAVE NUMBER AND CHARACTERS
# IF IT IS A BLACK CELL THE CHARACTER IS BLACK
# IF THERE IS NO NUMBER THEN NUMBER IS BLANK
# NUMBERS ARE CHARACTERS
# YOU CAN USE isBlack() TO SEE IF A CELL IS A BLACK CELL
# YOU CAN USE hasNum() TO SEE IF A CELL HAS A BLACK CELL
import json

class Cells:

    def __init__(self , number, character):

        self.n = number
        self.c = character

    def getChar(self):

        return self.c

    def getNum(self):

        return  self.n

    def toJSON(self):
        x = {"number": self.n , "character": self.c}
        return x