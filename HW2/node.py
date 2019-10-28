# The Value of Each Node - Possible Solution
class node:

    # M are the Number of Missionaries on the West Bank
    # C are the Number of Cannibals on the West Bank
    # B is 1 if the boat is on the west bank and 0 on the east bank
    def __init__(self, m , c , b ):

        self.m = m
        self.c = c
        self.b = b

        self.parent = None
        self.children = []

        pass

    ################ GETTERS ###################

    def getM(self):
        return self.m

    def getC(self):
        return self.c

    def getB(self):
        return self.b

    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.children

    ################ SETTERS ###################

    def setM(self , m):
        self.m = m

    def setC(self , c):
        self.c = c

    def setB(self , b):
        self.b = b

    def setParent(self, parentId):
        self.parent = parentId

    def setChildren(self , children):
        self.children = children

    ################ FUNCTIONS ##################
    def getValue(self):
        return self.__str__()

    def __eq__(self, other):

        if (other == None):
            return False

        if (self.m == other.m and self.c == other.c and self.b == other.b):
            return True

        return False

    def __str__(self):

        return "( " + str(self.m) + " , " + str(self.c) + " , " + str(self.b) + " )"
