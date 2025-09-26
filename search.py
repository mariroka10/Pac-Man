
# CHAIMA TALHI 

import util #which contains utility classes and functions for the search algorithms.

class SearchProblem:
    # returns the start state of the search problem.
    def getStartState(self):
        pass
    #returns True if the state is a goal state, False otherwise.
    def isGoalState(self, state):
        pass
    #It takes a state as input and returns a list of successor states, actions, and step costs from that state.    
    def expand(self, state):
        pass
    #It takes a list of actions as input and returns the total cost of the action sequence.
    def getCostOfActionSequence(self, actions):
        pass

def depthFirstSearch(prblm):
    exploreed = set() #empty set to store visited states
    borders = util.Stack() #to implement the frontier for the search algorithm.
    
    firstStartState = prblm.getStartState()# the start state of the problem is obtained using the getStartState method
    firstStartNode = (firstStartState, []) #created with the start state and an empty list of actions.

    borders.push(firstStartNode) #The start node is pushed onto the frontier stack

    while not borders.isEmpty():
        actualState, path = borders.pop() # node is popped from the frontier, and its state and actions are extracted.
        #If the current state is a goal state, the list of actions is returned as the solution.
        if prblm.isGoalState(actualState):
            return path

        if actualState not in exploreed:
            exploreed.add(actualState) #If the current state has not been visited, it is marked as visited
            child = prblm.expand(actualState) # and the successors of the current state are expanded using the expand method
            #. For each successor
            for nextState, action, _ in child:
                newActions = path + [action] #a new list of actions is created by appending the current action,
                borders.push((nextState, newActions)) #and the successor node is pushed onto the frontier stack.

    return path #If no goal state is found, the list of actions is returned as the solution.

def breadthFirstSearch(problem):
    visited = set()
    frontier = util.Queue()

    startState = problem.getStartState()
    startNode = (startState, [])

    frontier.push(startNode)

    while not frontier.isEmpty():
        currentState, actions = frontier.pop()

        if problem.isGoalState(currentState):
            return actions
        

        if currentState not in visited:
            visited.add(currentState)
            successors = problem.expand(currentState)

            for nextState, action, _ in successors:
                newActions = actions + [action]
                frontier.push((nextState, newActions))

    return actions

def uniformCostSearch(problem):
    exploreed = set() #empty set
    borders = util.PriorityQueue() #file fifo

    firstStartState = problem.getStartState()
    # a start node is created with the start state, an empty list of actions, and a cost of 0
    firstStartNode = (firstStartState, [], 0)  # Include the cost in the start node tuple

    borders.push(firstStartNode, 0)  # Initialize the priority with the cost

    while not borders.isEmpty():
        #a node is popped from the frontier, and its state, actions, and cost are extracted.
        actualState, path, cost = borders.pop()

        if problem.isGoalState(actualState):
            return path

        if actualState not in exploreed:
            exploreed.add(actualState)
            child = problem.expand(actualState)

            for nextState, action, stepCost in child:
                newActions = path + [action]
                newCost = cost + stepCost #The cost of the successor is updated by adding the step cost to the current cos
                borders.push((nextState, newActions, newCost), newCost) # the successor node, along with its new actions and cost,
                # is pushed onto the frontier priority queue with a priority equal to the new cost
                # This ensures that nodes with lower costs are explored first.

    return path

def aStarSearch(problem, hrstc=lambda state, problem: 0): #takes a problem and an optional heuristic function as input
    exploreed = set()
    borders = util.PriorityQueue()

    firstStartState = problem.getStartState()
    # the start state, an empty list of actions, and a cost of 0
    firstStartNode = (firstStartState, [], 0)  # Include the cost in the start node tuple
    #The heuristic for the start state is calculated by calling 
    #the heuristic function with the start state and the problem as arguments
    startHeuristic = hrstc(firstStartState, problem)  # Calculate the heuristic for the start state
    #the sum of the cost and the heuristic f= h+g
    borders.push(firstStartNode, startHeuristic) #This ensures that nodes with lower costs and more promising heuristic values are explored first.

    while not borders.isEmpty():
        actualState, path, cost = borders.pop()

        if problem.isGoalState(actualState):
            return path

        if actualState not in exploreed:
            exploreed.add(actualState)
            succ = problem.expand(actualState) 
            # the successors of the current state are expanded using the expand() method of the problem.
            for nextState, action, stepCost in succ:
                newActions = path + [action] #For each successor, a new list of actions is created by appending the current action to the existing actions.
                newCost = cost + stepCost    #cost men problem 
                
                newHrstc = hrstc(nextState, problem)  # Calculate the heuristic for the successor state
                # The heuristic for the successor state is calculated by calling 
                # the heuristic function with the successor state and the problem as arguments
                prio = newCost + newHrstc #The priority of the successor is calculated as the sum of the new cost and the new heuristic
                borders.push((nextState, newActions, newCost), prio) #pushed onto the frontier priority queue with the calculated priority.

    return path

#The breadthFirstSearch, uniformCostSearch, and aStarSearch functions follow a 
# similar structure to the depthFirstSearch function, but use a different data structure 
# for the frontier (queue for BFS, priority queue for UCS and A*) 
# and may consider the cost and heuristic values when expanding and prioritizing nodes.

# CHAIMA TALHI