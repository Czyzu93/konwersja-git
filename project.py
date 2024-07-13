import sys
import json
import yaml
import xml.etree.ElementTree as ET

def parse_args():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return tree, root

def write_xml(tree, file_path):
    tree.write(file_path)

def convert(input_file, output_file):
    if input_file.endswith('.json'):
        data = read_json(input_file)
    elif input_file.endswith('.yaml') or input_file.endswith('.yml'):
        data = read_yaml(input_file)
    elif input_file.endswith('.xml'):
        data, _ = read_xml(input_file)
    else:
        raise ValueError("Unsupported input file format")

    if output_file.endswith('.json'):
        write_json(data, output_file)
    elif output_file.endswith('.yaml') or output_file.endswith('.yml'):
        write_yaml(data, output_file)
    elif output_file.endswith('.xml'):
        write_xml(data, output_file)
    else:
        raise ValueError("Unsupported output file format")

if __name__ == "__main__":
    input_file, output_file = parse_args()
    convert(input_file, output_file)
