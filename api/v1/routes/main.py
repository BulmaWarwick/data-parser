import argparse
import json
import logging
import os
import sys

from data_parser.parser import DataParser
from data_parser.utils import validate_file

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )

def parse_args():
    parser = argparse.ArgumentParser(description="Data Parser CLI Tool")
    parser.add_argument("input_file", type=str, help="Path to the input file")
    parser.add_argument("output_file", type=str, help="Path to the output file")
    parser.add_argument("--config", type=str, help="Path to the config file", default=None)
    return parser.parse_args()

def main():
    configure_logging()
    logger = logging.getLogger(__name__)
    
    args = parse_args()
    
    if not validate_file(args.input_file):
        logger.error(f"Input file '{args.input_file}' does not exist or is not readable.")
        sys.exit(1)
    
    config = {}
    if args.config and validate_file(args.config):
        with open(args.config, "r") as config_file:
            config = json.load(config_file)
    
    parser = DataParser(config)
    try:
        parsed_data = parser.parse(args.input_file)
        with open(args.output_file, "w") as output_file:
            json.dump(parsed_data, output_file, indent=4)
        logger.info(f"Data successfully parsed and saved to '{args.output_file}'.")
    except Exception as e:
        logger.error(f"An error occurred during parsing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()