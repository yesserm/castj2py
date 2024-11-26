import json
from .json_loader import load_json_file
from .js_to_py_translator import translate_js_to_py


def convert_json_to_py(json_file_path, output_file_path):
    data = load_json_file(json_file_path)
    for command in data.get('commands', []):
        if 'command' in command:
            command['python_code'] = translate_js_to_py(command['command'])
            with open(output_file_path, 'w') as file:
                json.dump(data, file, indent=4)
