import os
import logging
from typing import List, Dict

def get_project_root() -> str:
    """Returns project root directory"""
    return os.path.dirname(os.path.abspath(__file__))

def configure_logger(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def parse_file(file_path: str) -> List[Dict]:
    try:
        with open(file_path, 'r') as file:
            data = []
            for line in file:
                # assuming each line is a json string
                import json
                data.append(json.loads(line))
            return data
    except FileNotFoundError:
        logger = configure_logger('utils')
        logger.error(f"File {file_path} not found")
        return []
    except Exception as e:
        logger = configure_logger('utils')
        logger.error(f"Error parsing file {file_path}: {str(e)}")
        return []