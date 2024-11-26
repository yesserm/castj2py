from src.utils.db_config import load_conversion_dict
import re


def translate_js_to_py(js_cod, conversion_d):
    sorted_keys = sorted(conversion_d.keys(), key=len, reverse=True)
    py_cod = js_cod
    for key in sorted_keys:
        pattern = re.escape(key)
        py_cod = re.sub(pattern, conversion_dict[key], py_cod)

    py_cod = re.sub(r'\bvar\b', '', py_cod)
    py_cod = re.sub(r'(\w+)\(\)\s*{', r'\1():', py_cod)
    py_cod = re.sub(r'\b(\w+)\s*:\s*', r'\1 = ', py_cod)
    return py_cod.strip()


# Ejemplo de uso
js_code = """ 
document.querySelector('button').click(); 
console.log('Hello, World!'); 
let x = 10; 
const y = 20; 
function add(a, b) { 
return a + b; 
} 
"""

conversion_dict = load_conversion_dict('conversion_dict.db')
py_code = translate_js_to_py(js_code, conversion_dict)
