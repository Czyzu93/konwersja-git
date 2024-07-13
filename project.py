import sys
import json
import yaml
import xml.etree.ElementTree as ET

def parse_args():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        input("Press Enter to exit...")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

def read_json(file_path):
    try:
        print(f"Reading JSON file: {file_path}")
        with open(file_path, 'r') as file:
            data = json.load(file)
        print(f"Successfully read JSON file: {file_path}")
        return data
    except Exception as e:
        print(f"Failed to read JSON file: {file_path} with error: {e}")
        raise

def write_json(data, file_path):
    try:
        print(f"Writing JSON file: {file_path}")
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Successfully wrote JSON file: {file_path}")
    except Exception as e:
        print(f"Failed to write JSON file: {file_path} with error: {e}")
        raise

def read_yaml(file_path):
    try:
        print(f"Reading YAML file: {file_path}")
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        print(f"Successfully read YAML file: {file_path}")
        return data
    except Exception as e:
        print(f"Failed to read YAML file: {file_path} with error: {e}")
        raise

def write_yaml(data, file_path):
    try:
        print(f"Writing YAML file: {file_path}")
        with open(file_path, 'w') as file:
            yaml.dump(data, file)
        print(f"Successfully wrote YAML file: {file_path}")
    except Exception as e:
        print(f"Failed to write YAML file: {file_path} with error: {e}")
        raise

def read_xml(file_path):
    try:
        print(f"Reading XML file: {file_path}")
        tree = ET.parse(file_path)
        root = tree.getroot()
        print(f"Successfully read XML file: {file_path}")
        return tree, root
    except Exception as e:
        print(f"Failed to read XML file: {file_path} with error: {e}")
        raise

def write_xml(tree, file_path):
    try:
        print(f"Writing XML file: {file_path}")
        tree.write(file_path)
        print(f"Successfully wrote XML file: {file_path}")
    except Exception as e:
        print(f"Failed to write XML file: {file_path} with error: {e}")
        raise

def convert(input_file, output_file):
    try:
        print(f"Converting {input_file} to {output_file}")
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
    except Exception as e:
        print(f"Conversion failed with error: {e}")
        raise

if __name__ == "__main__":
    try:
        input_file, output_file = parse_args()
        convert(input_file, output_file)
        print("Conversion successful!")
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to exit...")
