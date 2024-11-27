import unittest
from src.core import js_to_py_translator
from src.utils.conversion_dict import ConversionDict


class TestJsToPyTranslator(unittest.TestCase):
    def test_translation(self):
        js_code = "document.querySelector('button').click();"
        expected_py_code = "driver.find_element_by_css_selector('button').click()"
        conversion_dict = ConversionDict('../conversion_dict.db').get_conversion_dict()
        self.assertEqual(js_to_py_translator.translate_js_to_py(js_code, conversion_dict), expected_py_code)


if __name__ == '__main__':
    unittest.main()
