from HW1.node import node as s # States

class nodeArray:

    def __init__(self , root):

        self.root = root
        self.seen_states = []
        self.bad_states = []

        self.states_to_expand = [self.root]
        self.counter = 0
        pass

    # Move from the West Bank to the East Bank if b = 1
    # Move from the East Bank to the West Bank if b = 0
    def move(self , current_root):

        # Check if the State is possible to expand
        if (not self.checkState(current_root)):
            return None

        current_m = current_root.getM()
        current_c = current_root.getC()
        current_b = current_root.getB()
        posssible_states = []

        # Move From West Coast to East Coast
        if (current_b == 1):
            # Form all possible connections
            if current_m >= 2:
                posssible_states.append(s(current_m - (2)  , current_c , 0))

            if current_c >= 2:
                posssible_states.append(s(current_m , current_c - (2) , 0))

            if current_m >= 1:
                posssible_states.append(s(current_m - (1) , current_c , 0))

            if current_c >= 1:
                posssible_states.append(s(current_m , current_c - (1), 0))

            if (current_m >= 1 and current_c >= 1):
                posssible_states.append(s(current_m - (1) , current_c - (1) , 0))

        # Move from East Coast to West Coast
        if (current_b == 0):

            current_m_onEast = self.root.getM() - current_m
            current_c_onEast = self.root.getC() - current_c

            if (current_m_onEast >= 2):
                posssible_states.append(s(current_m + 2 , current_c , 1))

            if (current_c_onEast >= 2):
                posssible_states.append(s(current_m , current_c + 2 , 1))

            if (current_m_onEast >= 1):
                posssible_states.append(s(current_m + 1 , current_c , 1))

            if (current_c_onEast >= 1):
                posssible_states.append(s(current_m , current_c + 1, 1))

            if (current_m_onEast >= 1 and current_c_onEast >= 1):
                posssible_states.append(s(current_m + 1 , current_c + 1 , 1))

            pass

        return  posssible_states

    # False if state is not to be expanded further
    def checkState(self, state):

        if state in self.seen_states:
            return False

        if self.isBadState(state):
            return False

        if (self.isGoalState(state)):
            return False

        return True

    # Create all State Space
    def createAllStateSpace(self):

        # To create all possible paths, we need to store the nodes
        # that need to be expanded and do so in a stack

        while(self.states_to_expand != []):

            # Remove The Current State to Expand
            current_root = self.states_to_expand.pop()

            # Make an action and add to the states to expand
            possible_nodes = self.move(current_root)

            # Add it to the seen states list
            self.seen_states.append(current_root)

            # Connect the new states with its parent
            current_root.setChildren(possible_nodes)

            # Add the new states to the States to Expand List
            if (possible_nodes != None):
                for state in possible_nodes:
                    self.counter = self.counter + 1
                    self.states_to_expand.append(state)


        # Print Done to Indicate All Possible Nodes are made
        print("DONE")
        print(self.counter)

    def displayStatesAsATree(self):

        # Collect All Elements and their connections
        # A list of all nodes that need to be viewed
        to_be_viewed_states = [self.root]
        all_states = []
        nodes = []
        edges = []

        import dash
        import dash_cytoscape as cyto
        import dash_html_components as html

        app = dash.Dash(__name__)
        app.layout = html.Div([
            cyto.Cytoscape(
                id='cytoscape',
                elements= nodes + edges,
                layout={'name': 'dagre'},
                style={'width': '100%', 'height': '1000px'},
            ),
            html.Button('Add next node', id='button', style={'position': 'fixed', 'bottom': '500px'})
        ])

        @app.callback(dash.dependencies.Output('cytoscape', 'elements'),
                      [dash.dependencies.Input('button', 'n_clicks')])
        def update_output(n_clicks):
            id = 1 + n_clicks
            if (to_be_viewed_states != []):
                # Pop the next state from the states
                current_state = to_be_viewed_states.pop()

                # Add the current_state to the already viewed state if not added yet
                if (not current_state in all_states):
                    all_states.append(current_state)

                # Add the node to the nodes and increment the id
                nodes.append({'data': {'id': str(id), 'label': current_state.getValue()}})
                id = id + 1

                # Add the edge from child to parent
                if current_state.getParent() != None:
                    edges.append({'data': {'source': str(current_state.getParent())
                        , 'target': str(id - 1)}})
                    pass

                # Find the Children of the states and add them to the to_be_viewed_state
                children = current_state.getChildren()
                if (children != None):
                    for state in children:
                        state.setParent(id - 1)
                        # to_be_viewed_states.append(state)
                        if not self.isBadState(state):
                            to_be_viewed_states.append(state)
            return nodes + edges

        # Load extra layouts
        cyto.load_extra_layouts()

        # Run the server
        app.run_server(debug=True)

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
                    state.setParent(current_state)
                    to_be_viewed_states.append(state)

        # Seen Everything and still no solution
        print("############################################")
        print("No Solution Found")
        print("############################################")

    def displayGoalState(self , state):

        path = [state]
        current_state = state

        # Does not reach Root
        while (current_state.getParent() != None):
            current_state = current_state.getParent()
            path.append(current_state)

        path.reverse()

        print("############################################")
        print("Solution Path is: ")
        for a_state in path:
            print(a_state)
        print("############################################")
