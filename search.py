# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
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

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"

  print("Start:", problem.getStartState())
  print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
  print("Start's successors:", problem.getSuccessors(problem.getStartState()))

  explored = []
  fringe = util.Stack() #define the fringe as a Stack. You can check util.py
  fringe.push([(problem.getStartState(), "Stop", 0)]) # adding the first node into the fringe
  #please note that each node is represented using the path from the starting node to the it
  while not fringe.isEmpty():
      # print ("fringe: ", fringe.heap)
      path = fringe.pop() # pop a node from the fringe
      # print "path len: ", len(path)
      # print "path: ", path

      s = path[len(path) - 1]
      s = s[0]
      # print "s: ", s
      if problem.isGoalState(s):
          # print "FOUND SOLUTION: ", [x[1] for x i------------------------------------------------------------------------------------------------n path]
          return [x[1] for x in path][1:]

      if s not in explored:
          # append the state to explored
          # print "EXPLORING: ", ========
          explored.append(s)
          for successor in problem.getSuccessors(s):
              # print "SUCCESSOR: ", successor
              if successor[0] not in explored:
                  successorPath = path[:]
                  successorPath.append(successor)
                  # print "successorPath: ", successorPath
                  fringe.push(successorPath) # push the sucessorPath into fringe
          # else:
          # print successor[0], " IS ALREADY EXPLORED!!"

  return []

  util.raiseNotDefined()

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  print("Start:", problem.getStartState())
  print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
  print("Start's successors:", problem.getSuccessors(problem.getStartState()))

  explored = []
  fringe = util. Queue()  # define the fringe as a Queue. You can check util.py
  fringe.push([(problem.getStartState(), "Stop", 0)])  # adding the first node into the fringe
  # please note that each node is represented using the path from the starting node to the it
  while not fringe.isEmpty():
      # print ("fringe: ", fringe.heap)
      path = fringe.pop()  # pop a node from the fringe
      # print "path len: ", len(path)
      # print "path: ", path

      s = path[len(path) - 1]
      s = s[0]
      print ("s: ", s)
      if problem.isGoalState(s):
          # print "FOUND SOLUTION: "
          return [x[1] for x in path][1:]

      if s not in explored:
          # append the state to explored
          # print "EXPLORING: ", ========
          explored.append(s)
          for successor in problem.getSuccessors(s):
              print ("SUCCESSOR: ", successor)
              if successor[0] not in explored:
                  successorPath = path[:]
                  successorPath.append(successor)
                  # print "successorPath: ", successorPath
                  fringe.push(successorPath)  # push the sucessorPath into fringe
                  # else:
                  # print successor[0], " IS A>LREADY EXPLORED!!"

  return []
  python
  pacman.py - l
  mediumMaze - p
  SearchAgent - a
  fn = ucs


  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  explored = []
  cost = lambda apath: problem.getCostOfActions(x[1] for x in apath)
  fringe = util.PriorityQueueWithFunction(cost)  # define the fringe as a Queue. You can check util.py

  fringe.push([(problem.getStartState(), "Stop", 0)])  # adding the first node into the fringe
  # please note that each node is represented using the path from the starting node to the it
  while not fringe.isEmpty():
      # print ("fringe: ", fringe.heap)
      path = fringe.pop()  # pop a node from the fringe
      # print "path len: ", len(path)
      # print "path: ", path

      s = path[len(path) - 1]
      s = s[0]
      print("s: ", s)
      if problem.isGoalState(s):
          # print "FOUND SOLUTION: ", [x[1] for x i---n path]
          return [x[1] for x in path][1:]

      if s not in explored:
          # append the state to explored
          # print "EXPLORING: ", ========
          explored.append(s)
          for successor in problem.getSuccessors(s):
              print("SUCCESSOR: ", successor)
              if successor[0] not in explored:
                  successorPath = path[:]
                  successorPath.append(successor)
                  # print "successorPath: ", successorPath
                  fringe.push(successorPath)  # push the sucessorPath into fringe
                  # else:
                  # print successor[0], " IS A>LREADY EXPLORED!!"

  return []

  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  cost = lambda apath: problem.getCostOfActions(x[1] for x in apath) + heuristic(aPath[len(aPath)-1][0], problem)
  fringe = util.PriorityQueueWithFunction(cost)
  explored = []
  fringe.push([(problem.getStartState(), "Stop", 0)])
  while not fringe.isEmpty():
      # print ("fringe: ", fringe.heap)
      path = fringe.pop()
      s = path[len(path) - 1]
      s = s[0]
      if problem.isGoalState(s):
          # print "FOUND SOLUTION: ", [x[1] for x in path]
          return [x[1] for x in path][1:]

      if s not in explored:
          explored.append(s)  # append the state to explored
          # print "EXPLORING: ", s
          for successor in problem.getSuccessors(s):
              # print "SUCCESSOR: ", successor
              if successor[0] not in explored:
                  successorPath = path[:]
                  successorPath.append(successor)
                  print("successorPath: ", successorPath)
                  fringe.push(successorPath)  # push the sucessorPath into fringe
          # else:
          # print successor[0], " IS ALREADY EXPLORED!!"

  return []


  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
