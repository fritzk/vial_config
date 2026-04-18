import json
import yaml
import sys
import os

def load_file(filepath):
    with open(filepath, 'r') as f:
        if filepath.endswith('.yaml') or filepath.endswith('.yml'):
            return yaml.safe_load(f)
        return json.load(f)

def save_file(data, filepath, minify=False):
    with open(filepath, 'w') as f:
        if filepath.endswith('.yaml') or filepath.endswith('.yml'):
            yaml.dump(data, f, sort_keys=False, indent=2)
        else:
            if minify:
                json.dump(data, f, separators=(',', ':'))
            else:
                json.dump(data, f, indent=4)

def main():
    if len(sys.argv) < 3:
        print("Usage: python vial_vc.py <input_file> <output_file>")
        print("Example: python vial_vc.py layout.vil layout.yaml (Export to VC)")
        print("Example: python vial_vc.py layout.yaml layout.vil (Import to Vial)")
        return

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        data = load_file(input_path)
        # If the output is .vil, we minify it. Otherwise, we pretty-print.
        minify = output_path.endswith('.vil')
        save_file(data, output_path, minify=minify)
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
