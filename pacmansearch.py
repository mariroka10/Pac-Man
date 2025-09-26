# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter 
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util, queue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem): #profondeur pile
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    # states to be explored (LIFO). holds nodes in form (state, action)
    frontier = util.Stack()
    # previously explored states (for path checking), holds states
    exploredNodes = []
    # define start node
    startState = problem.getStartState()
    startNode = (startState, [])

    frontier.push(startNode)

    while not frontier.isEmpty():
        # begin exploring last (most-recently-pushed) node on frontier
        currentState, actions = frontier.pop()

        if currentState not in exploredNodes:
            # mark current node as explored
            exploredNodes.append(currentState)

            if problem.isGoalState(currentState):
                return actions
            else:
                # get list of possible successor nodes in
                # form (successor, action, stepCost)
                successors = problem.expand(currentState)

                # push each successor to frontier
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newNode = (succState, newAction)
                    frontier.push(newNode)

    return actions


def breadthFirstSearch(problem):
    #file largeur 
    visited = set() #collection
    frontier = [(problem.getStartState(), [])]  #frontier is a list  #tulipe est collection comme liste ms ne peut pas le modifier 
     # fi lfrontier thaz list fiha node lowel 
    while frontier: # while frontiere not empty
        state, actions = frontier.pop() # tna7i elem lowl 
        #actions list # pop remove and return the first element from a file
       # frontier.pop tna7i men la pile hadik lelemnt lkhr w trj3olna fi actions 
       # actions fiha les elements li n7iwhom b  pop men frentiere w rj3thom fi action w t7othom fi state
        if problem.isGoalState(state):
            return actions # idha kan goal treternih  beh t9dr t3rf chemin ta3o parente haka 
   #else 
        if state not in visited: # state like a node 
            visited.add(state) # ajouter dans visited nodes jdod 
            for successor, action, cost in problem.expand(state): #dictionery #succ is the brother
                frontier.append((successor, actions + [action])) # y7km node yna7ih w succ li hoa broth t3o yzido fi frnt 
                #yfiziti l point ki yvizitiha yna7iha hia w y7ot child t3ha fi list 
    return actions

def uniformCostSearch(problem):
    # visited = set()
    # frontier = [(problem.getStartState(), [], 0)]
    # while frontier:
    #     state, actions, cost = frontier.pop(0)
    #     if problem.isGoalState(state):
    #         return actions
    #     if state not in visited:
    #         visited.add(state)
    #         for successor, action, nextCost in problem.expand(state):
    #             frontier.append((successor, actions + [action], cost + nextCost))
    #         frontier.sort(key=lambda x: x[2])
    return None
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch # meme niveau
dfs = depthFirstSearch # lel asfel tol
astar = aStarSearch 
ucs = uniformCostSearch # makla lmliha 5las 
