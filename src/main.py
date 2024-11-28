import os
import sys

from core.js_to_py_translator import translate_js_to_py
from utils.logging_config import configure_logging
from gui.main_window import MainWindow
from utils.conversion_dict import ConversionDict, get_project_root

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

logger = configure_logging()


def main():
    logger.info("Initializing the application")
    db_path = os.path.join(get_project_root(), '..', 'conversion_dict.db')

    try:
        conversion_instance = ConversionDict(db_path)
        conversion_dict = conversion_instance.get_conversion_dict()
        logger.info(f"Loaded {len(conversion_dict)} conversion entries")
    except Exception as e:
        logger.error(f"An error occurred while loading the conversion dictionary: {e}")
        sys.exit(1)

    js_file_path = '../samples/file.js'

    with open(js_file_path, 'r') as file:
        js_code = file.read()

    py_code = translate_js_to_py(js_code, conversion_dict)
    logger.info(f"Translated JS to Python:\n{py_code}")

    logger.info("Starting the application")
    try:
        window = MainWindow()
        window.mainloop()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    logger.info("Closing the application")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
