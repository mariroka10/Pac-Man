



import util, queue

class SearchProblem:
    

    def getStartState(self):
       
        util.raiseNotDefined()

    def isGoalState(self, state):
       
        util.raiseNotDefined()

    def expand(self, state):
        
        util.raiseNotDefined()

    def getActions(self, state):
       
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
      
        util.raiseNotDefined()

    def getNextState(self, state, action):
        
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
       
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem): #profondeur pile
   
    frontier = util.Stack()
    exploredNodes = []
    startState = problem.getStartState()
    startNode = (startState, [])

    frontier.push(startNode)

    while not frontier.isEmpty():
        currentState, actions = frontier.pop()

        if currentState not in exploredNodes:
            exploredNodes.append(currentState)

            if problem.isGoalState(currentState):
                return actions
            else:
               
                successors = problem.expand(currentState)

                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newNode = (succState, newAction)
                    frontier.push(newNode)

    return actions


def breadthFirstSearch(problem):
    visited = set()
    frontier = [(problem.getStartState(), [])]  
    while frontier: 
        state, actions = frontier.pop()
        if problem.isGoalState(state):
            return actions 
   else 
        if state not in visited:
            visited.add(state) 
            for successor, action, cost in problem.expand(state): 
                frontier.append((successor, actions + [action])) 
    return actions

def uniformCostSearch(problem):
   
    return None
    

def nullHeuristic(state, problem=None):

    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
   
    util.raiseNotDefined()


bfs = breadthFirstSearch # meme niveau
dfs = depthFirstSearch # lel asfel tol
astar = aStarSearch 
ucs = uniformCostSearch # makla lmliha 5las 
