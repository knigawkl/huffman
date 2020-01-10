class Node:
    left = right = item = None
    weight = 0

    def __init__(self, i, w):
        self.item = i
        self.weight = w

    def add_children(self, l, r):
        self.left = l
        self.right = r

    def __cmp__(self, other):
        return (self.weight > other.weight) - (self.weight < other.weight)
