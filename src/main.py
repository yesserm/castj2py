import os
import sys
from utils.logging_config import configure_logging
from gui.main_window import MainWindow

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

logger = configure_logging()


def main():
    logger.info("Starting the application")
    window = MainWindow()
    window.mainloop()
    logger.info("Closing the application")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
