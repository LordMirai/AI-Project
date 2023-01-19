class Node:
    nodes = []

    def __init__(self, value: int = 0, parent: 'Node' = None, child: 'Node' = None):
        self.value: int = value
        self.parent: Node = parent
        self.child: Node = child

        if parent is None:
            self.parent = self
        else:
            parent.child = self

        Node.nodes.append(self)
        self.index = Node.nodes.index(self)

    def construct_path(self):
        path = []
        ind = self
        while ind.parent != ind:
            path.append(ind)
            ind = ind.parent

        return path.reverse()

    def display(self):
        print("Node info: [{}] Val:{} Parent:{} Child:{}".format(self.index, self.value,
                                                                 self.parent.index if self.parent != self else "Self",
                                                                 self.child.index if self.child is not None else None))
