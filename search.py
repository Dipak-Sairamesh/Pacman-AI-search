# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


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

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
   
    Commands to run in terminal:
    python pacman.py -l tinyMaze -p SearchAgent
    python pacman.py -l mediumMaze -p SearchAgent
    python pacman.py -l bigMaze -z .5 -p SearchAgent
    
    """
    "*** YOUR CODE HERE ***"
    
    from util import Stack
    frontier = Stack() # LIFO Stack for storing nodes    
    explored = [] # For storing explored nodes
    actions = [] # For storing explored nodes' actions
    start = problem.getStartState() # Initialize the initial-state node
    frontier.push((start, actions)) # Initialize the frontier
    print("Starting Position : ", start)
    
    while not frontier.isEmpty(): # Loop while frontier is not empty
        next_node = frontier.pop()
        coordinate, path = next_node
        
        if problem.isGoalState(coordinate): # Check for goal state
                return path
        
        if coordinate not in explored: # Check if the next node isn't already explored
            explored.append(coordinate)
            
            for successor in problem.getSuccessors(coordinate):
                node, direction, cost = successor # Triples
                new_actions = path + [direction] # # Adding direction to path
                frontier.push((node, new_actions))
    
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first.
        Commands to run :
            python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
            python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
            python eightpuzzle.py
    
    """
    "*** YOUR CODE HERE ***"
    
    from util import Queue
    frontier = Queue() # FIFO Queue for storing nodes    
    explored = [] # For storing explored nodes
    actions = [] # For storing explored nodes' actions
    start = problem.getStartState() # Initialize the initial-state node
    frontier.push((start, actions)) # Initialize the frontier
    print("Starting Position : ", start)
    
    while not frontier.isEmpty(): # Loop while frontier is not empty
        next_node = frontier.pop()
        coordinate, path = next_node
        
        if problem.isGoalState(coordinate): # Check for goal state
            return path
        
        if coordinate not in explored: # Check if the next node isn't already explored
            explored.append(coordinate)
            
            for successor in problem.getSuccessors(coordinate):
                node, direction, cost = successor # Triples
                new_actions = path + [direction] # Adding direction to path
                frontier.push((node, new_actions)) 
                
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first.
        Commands to run :
            python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
            python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
            python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
    """
    "*** YOUR CODE HERE ***"

    from game import PriorityQueue
    frontier = PriorityQueue() # Replacing FIFO with a priority queue for UCS
    explored = [] # For storing explored nodes
    actions = [] # For storing explored nodes' actions
    start = problem.getStartState() # Initialize the initial-state node
    frontier.push((start, actions), 0) # Initialize the frontier
    print("Starting Position : ", start)
                  
    while not frontier.isEmpty(): # Loop while frontier is not empty
        next_node = frontier.pop()
        coordinate, path = next_node
        
        if problem.isGoalState(coordinate): # Check for goal state 
            return path
        
        if coordinate not in explored: # Check if the next node isn't already explored
            explored.append(coordinate)
            
            for successor in problem.getSuccessors(coordinate):
                node, direction, cost = successor # Triples
                new_actions = path + [direction] # Adding direction to path
                new_cost = problem.getCostOfActions(new_actions) # Calculating new path cost
                frontier.push((node, new_actions), new_cost)
    
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first.
        Commands to run :
            python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
    """
    "*** YOUR CODE HERE ***"
    
    from game import PriorityQueue
    frontier = PriorityQueue() # Replacing FIFO with a priority queue for UCS
    explored = [] # For storing explored nodes
    actions = [] # For storing explored nodes' actions
    start = problem.getStartState() # Initialize the initial-state node
    frontier.push((start, actions), heuristic(start, problem)) # Initialize the frontier
    print("Starting Position : ", start)
                  
    while not frontier.isEmpty(): # Loop while frontier is not empty
        next_node = frontier.pop()
        coordinate, path = next_node
        
        if problem.isGoalState(coordinate): # Check for goal state 
            return path
        
        if coordinate not in explored: # Check if the next node isn't already explored
            explored.append(coordinate)
            
            for successor in problem.getSuccessors(coordinate):
                node, direction, cost = successor # Triples
                new_actions = path + [direction] # Adding direction to path
                new_cost = problem.getCostOfActions(new_actions) # Calculating new path cost
                heuristic_cost = heuristic(node, problem) # Calculating heuristic cost
                cost = heuristic_cost + new_cost # f(s)=g(s)+h(s)
                frontier.push((node, new_actions), cost) #
        
    #util.raiseNotDefined()
    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
