import json
import logging
from .json_loader import load_json_file
from .js_to_py_translator import translate_js_to_py
from src.utils.db_config import load_conversion_dict

logger = logging.getLogger('app_logger')


def convert_json_to_py(json_file_path, output_file_path):
    logger.info(f"Converting {json_file_path} to Python code and saving to {output_file_path}")
    try:
        data = load_json_file(json_file_path)
        commands = data['project']['commands']
        conversion_dict = load_conversion_dict('conversion_dict.db')
        for command in data['project']['commands']:
            if 'command' in command:
                command['python_code'] = translate_js_to_py(command['command'])
                with open(output_file_path, 'w') as file:
                    json.dump(data, file, indent=4)
                logger.info(f"Conversion complete. Saved to {output_file_path}")
    except Exception as e:
        logger.error(f"Error converting JSON to Python: {e}")
        raise e


def convert_js_file_to_py(js_file_path, output_file_path, db_path):
    logger.info(f"Converting {js_file_path} to Python code and saving to {output_file_path}")
    try:
        with open(js_file_path, 'r') as file:
            js_code = file.read()
            conversion_dict = load_conversion_dict('conversion_dict.db')
            py_code = translate_js_to_py(js_code, conversion_dict)
            with open(output_file_path, 'w') as file_output:
                file_output.write(py_code)
            logger.info(f"Conversion complete. Saved to {output_file_path}")
    except Exception as e:
        logger.error(f"Error converting JS to Python: {e}")
        raise e
