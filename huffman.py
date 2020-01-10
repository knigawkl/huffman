from itertools import groupby
from node import Node
from heapq import heapify


class Huffman:
    def encode(self, filepath: str) -> str:
        plaintext = self.read_file(filepath)
        res = self.build_tree(plaintext)
        return res

    def read_file(filepath: str) -> str:
        with open(filepath, 'r') as file:
            text = file.read()
        return text

    def build_tree(self, plaintext):
        nodes = [Node(letter, len(list(grouper))) for letter, grouper in groupby(sorted(plaintext))]

        tree = ''
        return nodes

    def decode(self):
        pass


input_path = 'input.txt'
output_path = 'output.txt'

huff = Huffman()
res = huff.encode(input_path)
print(res)
