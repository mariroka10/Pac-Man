
import util 
class SearchProblem:
    def getStartState(self):
        pass
    def isGoalState(self, state):
        pass
    def expand(self, state):
        pass
    def getCostOfActionSequence(self, actions):
        pass

def depthFirstSearch(prblm):
    exploreed = set() 
    borders = util.Stack()
    
    firstStartState = prblm.getStartState()
    firstStartNode = (firstStartState, []) 

    borders.push(firstStartNode) 

    while not borders.isEmpty():
        actualState, path = borders.pop()
        if prblm.isGoalState(actualState):
            return path

        if actualState not in exploreed:
            exploreed.add(actualState) 
            child = prblm.expand(actualState) 
            for nextState, action, _ in child:
                newActions = path + [action] 
                borders.push((nextState, newActions)) 

    return path

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
    exploreed = set()
    borders = util.PriorityQueue() 

    firstStartState = problem.getStartState()
   
    firstStartNode = (firstStartState, [], 0)  

    borders.push(firstStartNode, 0)  

    while not borders.isEmpty():
        actualState, path, cost = borders.pop()

        if problem.isGoalState(actualState):
            return path

        if actualState not in exploreed:
            exploreed.add(actualState)
            child = problem.expand(actualState)

            for nextState, action, stepCost in child:
                newActions = path + [action]
                newCost = cost + stepCost
                borders.push((nextState, newActions, newCost), newCost)

    return path

def aStarSearch(problem, hrstc=lambda state, problem: 0): 
    exploreed = set()
    borders = util.PriorityQueue()

    firstStartState = problem.getStartState()
    firstStartNode = (firstStartState, [], 0)  
    startHeuristic = hrstc(firstStartState, problem)  #
    borders.push(firstStartNode, startHeuristic) 

    while not borders.isEmpty():
        actualState, path, cost = borders.pop()

        if problem.isGoalState(actualState):
            return path

        if actualState not in exploreed:
            exploreed.add(actualState)
            succ = problem.expand(actualState) 
           
            for nextState, action, stepCost in succ:
                newActions = path + [action] 
                newCost = cost + stepCost   
                
                newHrstc = hrstc(nextState, problem)  #
                prio = newCost + newHrstc 
                borders.push((nextState, newActions, newCost), prio)

    return path
