import json
import logging
from .json_loader import load_json_file, get_js_code
from .js_to_py_translator import translate_js_to_py, translate_js_to_py_js2py
from ..utils.conversion_dict import ConversionDict

logger = logging.getLogger('app_logger')


def convert_json_to_py(json_file_path, output_file_path):
    logger.info(f"Converting {json_file_path} to Python code and saving to {output_file_path}")
    try:
        data = load_json_file(json_file_path)
        json_code = get_js_code()
        conversion_dict = ConversionDict().get_conversion_dict()
        for code in json_code:
            if code is not None:
                python_code = translate_js_to_py(code, conversion_dict)
                python_code = python_code.strip()
                with open(output_file_path, 'w') as file:
                    file.write(python_code)
                generate_python_code(python_code)
                logger.info(f"Conversion complete. Saved to {output_file_path}")
    except Exception as e:
        logger.error(f"Error converting JS to Python: {e}")
        raise e


def convert_js_file_to_py(js_file_path, output_file_path, db_path):
    logger.info(f"Converting {js_file_path} to Python code and saving to {output_file_path}")
    try:
        with open(js_file_path, 'r') as file:
            js_code = file.read()
            conversion_dict = ConversionDict().get_conversion_dict()
            py_code = translate_js_to_py(js_code, conversion_dict)
            with open(output_file_path, 'w') as file_output:
                file_output.write(py_code)
            logger.info(f"Conversion complete. Saved to {output_file_path}")
    except Exception as e:
        logger.error(f"Error converting JS to Python: {e}")
        raise e


def convert_js_to_py_js2py(js_code, output_file_path):
    logger.info(f"Converting JS code to Python code with JS2PY and saving to {output_file_path}")
    try:
        logger.info(f"JS code: {js_code}")
        py_code = translate_js_to_py_js2py(js_code)
        with open(output_file_path, 'w') as file_output:
            file_output.write(py_code)
        logger.info(f"Conversion complete. Saved to {output_file_path}")
    except Exception as e:
        logger.error(f"Error converting JS to Python: {e}")
        raise e


def generate_python_code(pycode):
    # generate python file from pycode
    pass
