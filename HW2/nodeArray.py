from HW2.node import node as s # States
from collections import deque

class nodeArray:

    def __init__(self , root , bSize):

        self.root = root
        self.bSize = bSize
        self.bad_states = []

        self.seen = []
        self.states_to_expand = deque([self.root])
        self.goalStateLevel = 0
        self.foundGoalState = False
        self.counter = 0
        pass

    # Move from the West Bank to the East Bank if b = 1
    # Move from the East Bank to the West Bank if b = 0
    def move(self , current_root):

        if (self.isGoalState(current_root)):
            if self.foundGoalState == False:
                self.goalStateLevel = self.getLevel(current_root)
                self.foundGoalState = True
                return

        # self.i = self.i + 1;
        # print(self.i)

        current_m = current_root.getM()
        current_c = current_root.getC()
        current_b = current_root.getB()
        posssible_states = []

        # Move From West Coast to East Coast
        if (current_b == 1):
            for a_bSize in range (1 , self.bSize + 1):

                # All of the Missionaries move
                if (current_m >= a_bSize):
                    posssible_states.append(s(current_m - a_bSize , current_c , 0))

                # All of the Cannibals move
                if (current_c >= a_bSize):
                    posssible_states.append(s(current_m , current_c - a_bSize , 0))

                # Some combination of them move in the boat
                for m_in_boat in range(1, a_bSize):

                    # Check if they can be added
                    # A_bSize - m_in_boat is c_in_boat
                    # The number of missionaries should be greater or equal to the number of cannibals left on land
                    if ( current_m >= m_in_boat and current_c >= (a_bSize - m_in_boat) ):
                        posssible_states.append(s(current_m - m_in_boat , current_c - (a_bSize - m_in_boat) , 0))

        # Move from East Coast to West Coast
        if (current_b == 0):

            current_m_onEast = self.root.getM() - current_m
            current_c_onEast = self.root.getC() - current_c

            for a_bSize in range(1, self.bSize + 1):

                # All of the Missionaries move
                if (current_m_onEast >= a_bSize):
                    posssible_states.append(s(current_m + a_bSize, current_c, 1))

                # All of the Cannibals move
                if (current_c_onEast >= a_bSize):
                    posssible_states.append(s(current_m, current_c + a_bSize, 1))

                # Some combination of them move in the boat
                for m_in_boat in range(1, a_bSize):

                    # Check if they can be added
                    # A_bSize - m_in_boat is c_in_boat
                    if (current_m_onEast >= m_in_boat and current_c_onEast >= (a_bSize - m_in_boat)):
                        posssible_states.append(s(current_m + m_in_boat, current_c + (a_bSize - m_in_boat), 1))

        return  posssible_states

    # False if state is not to be expanded further
    def checkIfStateIsBad(self, state):

        # if state in self.seen :
        #     return True

        if (self.hasLoops(state)):
            return True

        if self.isBadState(state):
            return True

        if (self.isGoalState(state)):
            return True

        return False

    # Create all State Space
    def createAllStateSpace(self):

        # To create all possible paths, we need to store the nodes
        # that need to be expanded and do so in a stack

        while(self.states_to_expand):

            # Remove The Current State to Expand
            current_root = self.states_to_expand.popleft()

            if (self.goalStateLevel != 0 and self.getLevel(current_root) >= self.goalStateLevel):
                continue

            # print (current_root)

            # Make an action and add to the states to expand
            possible_nodes = self.move(current_root)

            # Connect the new states with its parent
            current_root.setChildren(possible_nodes)

            self.seen.append(current_root)

            states_to_remove = []
            # Add the new states to the States to Expand List
            if (possible_nodes != None):
                for state in possible_nodes:

                    state.parent.append(current_root)
                    state.parent += current_root.parent

                    if (self.checkIfStateIsBad(state) and not self.isGoalState(state)):
                        states_to_remove.append(state)
                        continue

                    self.counter = self.counter + 1
                    self.states_to_expand.append(state)

                if (states_to_remove != None):
                    for state in states_to_remove:
                        possible_nodes.remove(state)

        # Print Done to Indicate All Possible Nodes are made
        print("DONE")
        print(self.counter)

    def hasLoops(self, state):

        # tempNode = copy.deepcopy(state.parent)
        # if (tempNode == None): #This is the root node
        #     return False
        #
        # while tempNode != None:
        #     if tempNode == state:
        #         return True
        #
        #     tempNode = copy.deepcopy(tempNode.parent)

        if (state in state.parent):
            return True

        return False

    def isBadState(self , state):

        if (state.getM() < 0 or state.getC() < 0):
            return True

        # Same number of Missionaries and Cannibals
        if (state.getM() == state.getC()):
            return False

        # Maximum Number of Missionaries on one side with none on the other side
        if (state.getM() == 0 or state.getM() == self.root.getM()):
            return False

        return True

    def isGoalState(self , state):

        if (state.getM() == 0 and state.getC() == 0 and state.getB() == 0):
            return True
        return False

    def hasGoalState(self):

        # A list of all nodes that need to be viewed
        to_be_viewed_states = [self.root]
        all_states = []

        id = 0

        while (to_be_viewed_states != []):

            # Pop the next state from the states
            current_state = to_be_viewed_states.pop()

            # Check if the state is a Goal State
            isGoalState = self.isGoalState(current_state)
            if (isGoalState):
                # The Current State is a Goal State
                # Move Up the states from this one to get the Path
                self.displayGoalState(current_state)
                return

            # Add the current_state to the already viewed state if not added yet
            if (not current_state in all_states):
                all_states.append(current_state)

            # Find the Children of the states and add them to the to_be_viewed_state
            children = current_state.getChildren()
            if (children != None):
                for state in children:
                    to_be_viewed_states.append(state)

        # Seen Everything and still no solution
        print("############################################")
        print("No Solution Found")
        print("############################################")

    def displayGoalState(self , state):

        path = state.getParent()
        # current_state = state
        #
        # # Does not reach Root
        # while (current_state.getParent() != None):
        #     current_state = current_state.getParent()
        #     path.append(current_state)

        path.reverse()

        print("############################################")
        print("Solution Path is: ")
        for a_state in path:
            print(a_state)
        print("############################################")

    def getLevel(self, state):
        return len(state.parent)