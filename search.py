from Node import Node


class Frontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(Frontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


def run_search():
    start = Node(0, None, None)

    frontier = Frontier()

    while True:
        if frontier.empty():
            print("No solution")
            return


class Maze:
    def __init__(self, filename: str):
        with open(filename) as f:
            pass
