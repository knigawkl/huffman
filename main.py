from huffman import Huffman

if __name__ == '__main__':
    input_path = 'input.txt'
    output_path = 'output.txt'

    huff = Huffman()
    encoded, root = huff.encode(input_path)
    huff.decode(encoded, root, output_path)
