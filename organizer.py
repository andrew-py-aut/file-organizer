# Automatic File Organizer
#
# This script watches a specified source directory and organizes files
# into destination folders based on their extensions, as defined in a
# configuration file (config.json).
#

import os
import json
import shutil
import logging
from pathlib import Path

# --- Configuration ---
CONFIG_FILE = 'config.json'
LOG_FILE = 'file_organizer.log'

# --- Setup Logging ---
# Configure logging to output to both a file and the console.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def load_configuration(config_path):
    """
    Loads the configuration from a JSON file.
    
    Args:
        config_path (str): The path to the configuration file.
        
    Returns:
        dict: The loaded configuration, or None if an error occurs.
    """
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        logging.info("Configuration loaded successfully.")
        return config
    except FileNotFoundError:
        logging.error(f"Configuration file not found at '{config_path}'. Please create it.")
        return None
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from '{config_path}'. Please check its format.")
        return None

def organize_files(config):
    """
    Organizes files based on the provided configuration.
    
    Args:
        config (dict): The configuration dictionary containing source directory
                       and extension mappings.
    """
    source_dir = Path(config.get('source_directory'))
    mappings = config.get('mappings', {})
    
    # Invert mappings for faster lookup: {'.pdf': 'Documents', '.txt': 'Documents'}
    extension_to_folder = {
        ext: folder 
        for folder, extensions in mappings.items() 
        for ext in extensions
    }
    
    # Default folder for uncategorized files
    others_folder = "Others"

    if not source_dir.exists() or not source_dir.is_dir():
        logging.error(f"Source directory '{source_dir}' does not exist or is not a directory.")
        return

    logging.info(f"Scanning source directory: {source_dir}")

    # Iterate over all items in the source directory
    for item in source_dir.iterdir():
        # Process only files, ignore directories and the script itself
        if item.is_file() and item.name != os.path.basename(__file__):
            file_extension = item.suffix.lower()
            
            # Determine the destination folder
            target_folder_name = extension_to_folder.get(file_extension, others_folder)
            destination_dir = source_dir / target_folder_name
            
            try:
                # Create the destination folder if it doesn't exist
                destination_dir.mkdir(exist_ok=True)
                
                # Move the file
                shutil.move(str(item), str(destination_dir / item.name))
                logging.info(f"Moved: '{item.name}' -> '{destination_dir.name}/'")

            except PermissionError:
                logging.warning(f"Permission denied to move '{item.name}'. The file might be in use.")
            except Exception as e:
                logging.error(f"Failed to move '{item.name}'. Error: {e}")

    logging.info("File organization process completed.")

def main():
    """
    Main function to run the file organizer script.
    """
    logging.info("--- Starting File Organizer Script ---")
    
    config = load_configuration(CONFIG_FILE)
    
    if config:
        organize_files(config)
        
    logging.info("--- Script Finished ---")

if __name__ == "__main__":
    main()