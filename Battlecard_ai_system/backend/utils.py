import os
import json
import logging

# Function to read API keys from the JSON file
def load_api_keys(filepath="data/api_keys.json"):
    """Loads API keys from a JSON file."""
    try:
        with open(filepath, "r") as file:
            api_keys = json.load(file)
        return api_keys
    except FileNotFoundError:
        logging.error(f"API keys file not found: {filepath}")
        return None

# Function to create directories if they don't exist
def create_directory(directory):
    """Creates a directory if it doesn't already exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to save content to a file
def save_to_file(content, filepath):
    """Saves content to a file."""
    with open(filepath, "w") as file:
        file.write(content)

# Function to load battlecard templates from JSON
def load_battlecard_templates(filepath="data/battlecard_templates.json"):
    """Loads battlecard templates from a JSON file."""
    try:
        with open(filepath, "r") as file:
            templates = json.load(file)
        return templates
    except FileNotFoundError:
        logging.error(f"Battlecard templates file not found: {filepath}")
        return None

# Function to set up basic logging
def setup_logging(logfile="battlecard_system.log"):
    """Sets up logging configuration."""
    logging.basicConfig(
        filename=logfile,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
