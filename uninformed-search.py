class node ():
    def add_left_right(self, left, right):
        self.left = left
        self.right = right


start, A4, H2, G1, F2, G3, D1, E1, C1, B1, C2, C0, goal = node()

start.add_left_right(H2, A4)
H2.add_left_right(G1, F2)
F2.add_left_right(D1, G3)
D1.add_left_right(E1, C1)
C1.add_left_right(B1, C2)
C2.add_left_right(C0, goal)

open = [start, A4, H2, G1, F2, G3, D1, E1, C1, B1, C2, C0, goal]
queue = []
visited = []
def breadth_first_search(n: node):
    visited.append(n)

