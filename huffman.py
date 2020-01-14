from itertools import groupby
from typing import Tuple
from node import Node
from heapq import heapify, heappop, heappush


class Huffman:
    def write_file(self, output_path, decoded):
        with open(output_path, 'w+') as file:
            file.write(decoded)

    def read_file(self, filepath: str) -> str:
        with open(filepath, 'r') as file:
            text = file.read()
        return text

    def encode(self, filepath: str) -> Tuple[str, Node]:
        plaintext = self.read_file(filepath)
        root = self.build_tree(plaintext)
        codes = self.binarize(root)
        encoded = "".join([codes[sign] for sign in plaintext])
        return encoded, root

    def build_tree(self, plaintext: str) -> Node:
        nodes = [Node(letter, len(list(grouper))) for letter, grouper in groupby(sorted(plaintext))]
        heapify(nodes)
        while len(nodes) > 1:
            l = heappop(nodes)
            r = heappop(nodes)
            new_weight = l.weight + r.weight
            new_node = Node(None, new_weight)
            new_node.add_children(l, r)
            heappush(nodes, new_node)
        return nodes[0]

    def binarize(self, root: Node) -> dict:
        codes = {}
        self.create_code("", root, codes)
        return codes

    def create_code(self, prev, node, codes):
        if node.item:
            if not prev:
                codes[node.item] = "0"
            else:
                codes[node.item] = prev
        else:
            self.create_code(prev + "0", node.left, codes)
            self.create_code(prev + "1", node.right, codes)

    def decode(self, encoded: str, root: Node, output_path: str):
        current = root
        decoded = ''
        for code in encoded:
            if int(code) == 0:
                current = current.left
            else:
                current = current.right
            if current.left is None and current.right is None:
                decoded += current.item
                current = root
        self.write_file(output_path, decoded)
