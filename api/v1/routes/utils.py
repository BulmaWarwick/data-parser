import logging
import os
import re
from typing import List, Dict

def configure_logger() -> logging.Logger:
    logger = logging.getLogger('data-parser')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def parse_file_path(file_path: str) -> Dict:
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1]
    file_directory = os.path.dirname(file_path)
    return {
        'file_name': file_name,
        'file_extension': file_extension,
        'file_directory': file_directory
    }

def validate_string_input(input_string: str) -> bool:
    if not isinstance(input_string, str):
        return False
    if not input_string.strip():
        return False
    return True

def extract_numbers_from_string(input_string: str) -> List[float]:
    numbers = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", input_string)
    return [float(num) for num in numbers]

def main():
    logger = configure_logger()
    logger.info('Utils module initialized')

if __name__ == '__main__':
    main()