def translate_js_to_py(js_code):
    py_code = js_code.replace('document.querySelector', 'driver.find_element_by_css_selector')
    py_code = py_code.replace(';', '')
    return py_code
