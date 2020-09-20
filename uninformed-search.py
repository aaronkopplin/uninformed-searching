class Node:
    def __init__(self, name: str):
        self.left = None
        self.right = None
        self.parents = []
        self.name = name

    def add_left_right(self, left, right):
        self.left = left
        self.right = right
        self.parents = []


start = Node("start")
A4 = Node("A4")
H2 = Node("H2")
G1 = Node("G1")
F2 = Node("F2")
G3 = Node("G3")
D1 = Node("D1")
E1 = Node("E1")
C1 = Node("C1")
B1 = Node("B1")
C2 = Node("C2")
C0 = Node("C0")
goal = Node("goal")

start.add_left_right(H2, A4)
H2.add_left_right(G1, F2)
F2.add_left_right(D1, G3)
D1.add_left_right(E1, C1)
C1.add_left_right(B1, C2)
C2.add_left_right(C0, goal)

all_nodes = [start, A4, H2, G1, F2, G3, D1, E1, C1, B1, C2, C0, goal]


def depth_first_search(n: Node):
    if n == goal:
        n.parents.append(goal.name)
        return
    if n.left:
        n.left.parents.extend(n.parents + [n.name])
        depth_first_search(n.left)
    if n.right:
        n.right.parents.extend(n.parents + [n.name])
        depth_first_search(n.right)


depth_first_search(start)
print("Depth first search results:\t\t{0}".format(goal.parents))


def breadth_first_search(n: Node):
    current_layer = [n]
    while True:
        next_layer = []
        for child in current_layer:
            if child.left:
                child.left.parents.extend(child.parents + [child.name])
                next_layer.append(child.left)
            if child.right:
                child.right.parents.extend(child.parents + [child.name])
                next_layer.append(child.right)
        for child in next_layer:
            if child:
                if child == goal:
                    child.parents.append(goal.name)
                    return

        current_layer = next_layer


# Clear nodes parents
for n in all_nodes:
    n.parents = []

breadth_first_search(start)
print("Breadth first search results:\t{0}".format(goal.parents))
