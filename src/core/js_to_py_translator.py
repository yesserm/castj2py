import re
import logging
import js2py

logger = logging.getLogger('app_logger')


def translate_js_to_py(js_cod, conversion_d):
    sorted_keys = sorted(conversion_d.keys(), key=len, reverse=True)
    py_cod = js_cod
    for key in sorted_keys:
        pattern = re.escape(key)
        py_cod = re.sub(pattern, conversion_d[key], py_cod)

    py_cod = re.sub(r'\bvar\b', '', py_cod)
    py_cod = re.sub(r'(\w+)\(\)\s*{', r'\1():', py_cod)
    py_cod = re.sub(r'\b(\w+)\s*:\s*', r'\1 = ', py_cod)
    return py_cod.strip()


def translate_js_to_py_js2py(js_cod):
    file_path = js_cod
    with open(file_path, 'r') as file:
        js_cod = file.read()
    logger.info(f"Translating JS to Python with JS2PY code: {js_cod}")
    py_code = js2py.translate_js(js_cod)
    logger.info(f"JS2PY code: {py_code}")
    return py_code
