class Node:
    def __init__(self, name: str):
        self.left = None  # children
        self.right = None  # children
        self.parents = []  # to keep track of nodes as we step through the maze
        self.name = name  # literal location / name of the node

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

# create the maze as a tree graph
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
        # note that we passed a node
        n.left.parents.extend(n.parents + [n.name])

        # recursive call uses a the stack (built in to computer architecture) to do 'depth'
        depth_first_search(n.left)
    if n.right:
        # note that we passed a node
        n.right.parents.extend(n.parents + [n.name])
        depth_first_search(n.right)


depth_first_search(start)
print("Depth first search path to goal:\t{0}".format(goal.parents))


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
                    # if the loop terminates at all, we have proven that the algorithm reaches the goal
                    return

        current_layer = next_layer


# Clear nodes parents
for n in all_nodes:
    n.parents = []

breadth_first_search(start)
print("Breadth first search path to goal:\t{0}".format(goal.parents))
