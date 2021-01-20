import math

import skgeom as sg
from skgeom.draw import draw
import matplotlib.pyplot as plt

from matplotlib import pyplot as plt
import matplotlib.patches as patches


class Node:
    """classe che definisce un nodo in un grafo"""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def propagation(self, problem):
        """funzione che effettua la propagazione del nodo, ritorna la lista dei figli"""

        return [self.child_node(action, problem)
               for action in problem.actions(self.state)]

    def child_node(self, action, problem):
        """funzione che  crea un nodo partendo dal risultato di una azione dello stato corrente"""

        new_state = problem.result(action, self.state)
        next_node = Node(new_state, self, action, problem.path_cost(self.path_cost, self.state, action))
        return next_node

    def solution(self):
        """ritorna una sequenza di azione per andare da inizio, a fine"""

        return [node.action for node in self.path()[1:]]

    def path(self):
        """ritorna la lista dei nodi che formano un cammino dalla radice fino a questo nodo"""

        node = self
        path = []
        while node:
            path.append(node)
            node = node.parent
        return list(reversed(path))

    def __eq__(self, other):
        return self.state == other.state and self.path_cost == other.path_cost \
               and self.action == other.action and self.parent == other.parent

    def __lt__(self, other):
        return self.state < other.state


class RobotRoute:
    """classe che definisce il problema della guida del robot"""

    def __init__(self, init_state, goal_state, map_):
        self.init_state = init_state
        self.goal_state = goal_state
        self.map = map_  # mappa degli ostacoli che si deve superare

    def actions(self, state):
        """funzione che mappa tutti i vertici raggiungibili da un punto state ad un insieme di vertici di poligoni
        convessi o allo stato di goal"""

        actions = list()
        for i in range(0, len(self.map)):
            segments = self.__segment_of_pol(state, self.map[i])
            if segments is not None:
                for j in range(0, len(self.map)):
                    if j != i:
                        length = len(segments)
                        idx = 0
                        while idx < length:
                            if self.__intersection_pol(segments[idx], self.map[j]):
                                segments.remove(segments[idx])
                                idx -= 1
                                length -= 1
                            idx += 1
            for x in segments:
                actions.append(x)
        idx = 0
        while idx < len(self.map):
            if self.__intersection_pol(sg.Segment2(state, self.goal_state), self.map[idx]):
                break
            idx += 1
        if idx == (len(self.map)):
            actions.append(sg.Segment2(state, self.goal_state))

        return actions

    def result(self, action, state):
        """ritorna un nuovo stato partendo dall'azione e dallo stato dati"""
        if state == action[0]:
            return action[1]
        return action[0]

    def goal_test(self, state):
        """dato uno stato, controlla se questo è o meno il goal"""

        return state == self.goal_state

    def path_cost(self, cost, state, action):
        seg = sg.Segment2(state, action[1])
        return cost + math.sqrt(seg.squared_length())

    def h(self, node):
        """si utilizza euristica della distanza manhattan"""

        seg = sg.Segment2(node.state, self.goal_state)
        return math.sqrt(seg.squared_length())

    def __segment_of_pol(self, start, poly):
        """ ritorna una lista di tutti i possibili vettori dal punto start a vertici del poligono poly"""

        seg_vector = list()  # lista di ritorno con tutti i possibili vettori
        vertices = list(poly.vertices)
        if start in vertices:
            for i in range(0, len(vertices)):
                if start == vertices[i]:
                    seg_vector.append(sg.Segment2(vertices[i], vertices[(i + 1) % len(vertices)]))
                    seg_vector.append(sg.Segment2(vertices[i], vertices[(i - 1)]))
            return seg_vector

        for coord in poly.vertices:
            ps = sg.Segment2(start, coord)
            i = -1
            while i < len(vertices) - 1:

                if vertices[i + 1] != coord and vertices[i] != coord:
                    if sg.intersection(ps, sg.Segment2(vertices[i], vertices[i + 1])) is not None:
                        break
                i += 1
            if i == (len(vertices) - 1):
                seg_vector.append(ps)

        return seg_vector

    def __intersection_pol(self, seg, poly):
        """funzione che controlla se un segmento passa attraverso un poligono"""
        vertices = list(poly.vertices)

        for i in range(-1, len(vertices) - 1):
            p_int = sg.intersection(seg, sg.Segment2(vertices[i], vertices[i + 1]))

            if p_int is not None:
                if p_int != seg[0]:
                    return True

        return False
