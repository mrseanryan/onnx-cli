import json

def read_lines_from_file(filepath):
    lines = []
    with open(filepath, encoding='utf-8') as file:
        lines = [line.rstrip() for line in file]
    return lines

def write_to_file(text, filepath):
    with open(filepath, "w") as outfile:
        outfile.write(text)

def read_json_from_file(filepath):
    with open(filepath) as json_file:
        return json.load(json_file)
