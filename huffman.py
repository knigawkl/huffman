import typing
from itertools import groupby
from node import Node
from heapq import heapify, heappop, heappush


class Huffman:
    def encode(self, filepath: str) -> str:
        plaintext = self.read_file(filepath)
        root = self.build_tree(plaintext)
        return res

    def read_file(self, filepath: str) -> str:
        with open(filepath, 'r') as file:
            text = file.read()
        return text

    def build_tree(self, plaintext: str) -> typing.List[Node]:
        nodes = [Node(letter, len(list(grouper))) for letter, grouper in groupby(sorted(plaintext))]
        heapify(nodes)
        while len(nodes) > 1:
            l = heappop(nodes)
            r = heappop(nodes)
            new_weight = l.weight + r.weight
            new_node = Node(None, new_weight)
            new_node.add_children(l, r)
            heappush(nodes, new_node)
        return nodes

    def decode(self):
        pass


if __name__ == '__main__':
    input_path = 'input.txt'
    output_path = 'output.txt'

    huff = Huffman()
    res = huff.encode(input_path)
    print(res)
