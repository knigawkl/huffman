def write_file(output_path, decoded):
    with open(output_path, 'w+') as file:
        file.write(decoded)


def read_file(filepath: str) -> str:
    with open(filepath, 'r') as file:
        text = file.read()
    return text