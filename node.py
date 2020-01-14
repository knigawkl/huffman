class Node:
    left = right = item = None
    weight = 0

    def __init__(self, i, w):
        self.item = i
        self.weight = w

    def add_children(self, l, r):
        self.left = l
        self.right = r

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight
