from HW2.nodeArray import nodeArray as na
from HW2.node import node as s

# root = s(3,3,1) # 3 Missionaries, 3 Cannibals, Boat on the West Bank
root = s(3,3,1) # 4 Missionaries, 4 Cannibals, Boat on the West Bank

new_list = na(root, 2)
new_list.createAllStateSpace()
new_list.hasGoalState()
new_list.displayStatesAsATree()
