import sqlite3
import json
import logging
import os

logger = logging.getLogger('app_logger')


def create_db(db_path) -> None:
    """Create the SQLite database if it doesn't exist
    :param db_path: Path to the SQLite database
    :return: None
    """
    db_abs_path = os.path.join(get_project_root(), db_path)
    conn = sqlite3.connect(db_abs_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversion_dict ( 
        js_code TEXT PRIMARY KEY, 
        py_code TEXT NOT NULL 
        )
    """)
    conn.commit()
    conn.close()


def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def insert_conversion(db_path: str, js_code: str, py_code: str) -> int:
    """Insert a new conversion into the database
    :param db_path: Path to the SQLite database
    :param js_code: Code in JavaScript
    :param py_code: Code in Python
    :return: The row ID of the inserted conversion or 0 if it already exists
    """
    db_abs_path = os.path.join(get_project_root(), db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Verificar si la clave y el valor ya existen
    cursor.execute("SELECT 1 FROM conversion_dict WHERE js_code = ? AND py_code = ?", (js_code, py_code))
    result = cursor.fetchone()
    if result is None:
        cursor.execute("INSERT INTO conversion_dict (js_code, py_code) VALUES (?, ?)", (js_code, py_code))
        conn.commit()
        logger.info(f"Inserted: {js_code} -> {py_code}")
        conn.close()
        return cursor.lastrowid
    else:
        logger.info(f"Already exists: {js_code} -> {py_code}")
        conn.close()
        return 0


def load_conversion_dict(db_path: str) -> dict:
    """Load the conversion dictionary from the database
    :param db_path: Path to the SQLite database
    :return: A dictionary with the conversion data
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT js_code, py_code FROM conversion_dict')
    rows = cursor.fetchall()
    conn.close()
    return {row[0]: row[1] for row in rows}


def load_json_to_db(db_path, json_path):
    """Load the JSON data into the database
    :param db_path: Path to the SQLite database
    :param json_path: Path to the JSON file
    :return: None
    """
    json_abs_path = os.path.join(get_project_root(), json_path)
    if not os.path.exists(json_abs_path):
        logger.error(f"File not found: {json_abs_path}")
        return
    with open(json_abs_path, 'r') as file:
        rows_inserted = 0
        data = json.load(file)
        for js_code, py_code in data.items():
            response = insert_conversion(db_path, js_code, py_code)
            if response > 0:
                rows_inserted += 1
        logger.info(f"Inserted {rows_inserted} rows into the database")
