from utils import *
from classes import Node


def best_first_graph_search(problem, f, display=False):

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
