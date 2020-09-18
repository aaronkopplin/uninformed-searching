class Node():
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

finalpath = []


def depth_first_search(n: Node):
    finalpath.append(n.name)
    if n == goal:
        print("Path found!")
        return
    elif not n.left and not n.right:
        finalpath.pop()
        return

    if n.left:
        depth_first_search(n.left)
    if n.right:
        depth_first_search(n.right)


depth_first_search(start)
print(finalpath)
