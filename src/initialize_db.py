import os
import logging
from utils.db_config import create_db, load_json_to_db

logger = logging.getLogger('app_logger')


def main():
    db_path = '../conversion_dict.db'
    json_path = '../conversion_dict.json'
    if not os.path.exists(db_path) or not os.path.exists(json_path):
        create_db(db_path)
        load_json_to_db(db_path, json_path)
        logger.info(f"Database created at {db_path}")
        logger.info(f"Database created and loaded with data from {json_path}")
    else:
        logger.info(f"Database already exists at {db_path}")
        logger.info(f"Loading data from {json_path} to database")
        load_json_to_db(db_path, json_path)


if __name__ == '__main__':
    main()
