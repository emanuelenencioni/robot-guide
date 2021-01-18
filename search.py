from utils import *
from classes import Node


def best_first_graph_search(problem, f, display=False):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.init_state)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = list()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
            return node
        count = 0
        for state in explored:
            if node.state == state:
                count += 1
        if count == 0:
            explored.append(node.state)
        for child in node.propagation(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None


def astar_search(problem, h=None, display=True):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')

    return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display)


def bfs_graph_search(problem):
    explored = []
    node = Node(problem.init_state)
    frontier = [node]
    if len(frontier) == 0:
        return None
    while True:
        n = frontier.pop(0)
        if problem.goal_test(n.state):
            return n
        count = 0
        for state in explored:
            if n.state == state:
                count += 1
        if count == 0:
            explored.append(n.state)
        for child in n.propagation(problem):
            if child.state not in explored:
                frontier.append(child)

    return None
