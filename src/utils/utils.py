import os
import json
from typing import Dict, List, Any

def load_config(file_path: str) -> Dict[str, Any]:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Config file not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)

def save_config(file_path: str, config: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)

def parse_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    parsed_data = []
    for item in data:
        parsed_item = {}
        for key, value in item.items():
            if isinstance(value, str):
                parsed_item[key] = value.strip()
            else:
                parsed_item[key] = value
        parsed_data.append(parsed_item)
    return parsed_data

def validate_data(data: List[Dict[str, Any]]) -> bool:
    required_keys = ['id', 'name', 'value']
    for item in data:
        if not all(key in item for key in required_keys):
            return False
    return True

def main():
    config_file = 'config.json'
    config = load_config(config_file)
    data = config['data']
    if validate_data(data):
        parsed_data = parse_data(data)
        print(parsed_data)
    else:
        print("Invalid data")

if __name__ == "__main__":
    main()