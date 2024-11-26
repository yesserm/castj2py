import unittest
from src.core import js_to_py_translator


class TestJsToPyTranslator(unittest.TestCase):
    def test_translation(self):
        js_code = "document.querySelector('button').click();"
        expected_py_code = "driver.find_element_by_css_selector('button').click()"
        self.assertEqual(js_to_py_translator.translate_js_to_py(js_code), expected_py_code)


if __name__ == '__main__':
    unittest.main()
